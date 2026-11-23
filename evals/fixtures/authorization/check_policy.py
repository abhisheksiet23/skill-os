"""Independent checks for the fictional expense brief; not production assurance."""
import argparse
import importlib.util


USERS = {
    "kim": (True, {"Reader", "Approver"}),
    "lou": (True, {"Approver"}),
    "mina": (True, {"Reader"}),
    "noah": (False, {"Reader", "Approver"}),
}
EXPENSES = {
    1: ("mina", "north", "Pending"),
    2: ("sam", "south", "Pending"),
    3: ("kim", "north", "Pending"),
    4: ("mina", "north", "Approved"),
}


def check_policy(path):
    spec = importlib.util.spec_from_file_location("evaluated_policy", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    db = module.create_demo()
    checks = 0

    def check(user, action, expense, expected):
        nonlocal checks
        actual = module.can(db, user, action, expense)
        if actual is not expected:
            raise AssertionError(
                f"{user!r}, {action!r}, expense {expense}: expected {expected}, got {actual!r}"
            )
        checks += 1

    try:
        for user, (active, roles) in USERS.items():
            for action in ("expenses.read", "expenses.approve"):
                required = "Reader" if action == "expenses.read" else "Approver"
                for expense, (owner, department, state) in EXPENSES.items():
                    expected = (
                        active and required in roles and department == "north"
                        and (action == "expenses.read" or (state == "Pending" and owner != user))
                    )
                    check(user, action, expense, expected)

        for user, action, expense in (
            ("absent", "expenses.read", 1),
            ("kim", "unknown", 1),
            ("kim", "expenses.read", 999),
            ("kim; DROP TABLE Users", "expenses.read", 1),
            ("kim", None, 1),
            (None, "expenses.read", 1),
            ("kim", "", 1),
        ):
            check(user, action, expense, False)

        module.revoke_role(db, "kim", "Reader")
        check("kim", "expenses.read", 1, False)
        check("kim", "expenses.approve", 1, True)
        check("mina", "expenses.read", 1, True)
        module.revoke_role(db, "kim", "Approver")
        check("kim", "expenses.approve", 1, False)

        db.close()
        check("mina", "expenses.read", 1, False)
    finally:
        db.close()
    return checks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("policy", help="Path to the generated policy.py; importing it executes code")
    args = parser.parse_args()
    count = check_policy(args.policy)
    print(f"{count} expense decision, revocation and failure assertions passed.")
