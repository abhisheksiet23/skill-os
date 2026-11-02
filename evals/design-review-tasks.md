# Design review comparison

Run these offline requests against the merged pre-change skills and the candidate with comparable models and tools. Give performers only this task file and their variant's skill descriptions/paths. Let them choose between `app-analyze` and `app-solution-design`, loading relevant local references only. Do not give them the assessment key, authoring conversation or peer outputs. Treat each case as a separate user request; record when cases share a performer context.

No browsing, installation, production edits, deployment or external integration is authorized. The source excerpts below are the complete synthetic source evidence for these tasks, not a live application. Do not invent execution results. Return a useful assessment of at most 250 words per case, including the skill/reference paths actually read and any limitations. Preserve verbatim outputs and variant snapshots in ignored `.eval-runs/design-review/`.

## 1. Portal requirements

User: Review this requirements draft for readiness to hand to another engineer. Use the project records below. Findings only; do not rewrite the draft or implement anything.

`decisions.md`, accepted owner decision:

> Modernize only Login, Home and Menu. Keep the existing credentials, shared database schema and 100 retained pages. Signing in through the new Login must also authenticate access to retained pages through their current session mechanism. Home widgets remain outside this increment. No separate sign-in step is acceptable.

`portal-requirements.md`, current draft:

> Replace Login, Home and Menu with the new UI. Login verifies credentials and stores a signed-in state for the new shell. Menu preserves links to all retained pages. Home displays a welcome panel. A successful credential check redirects to Home; an invalid check shows an inline error. Acceptance: valid and invalid sign-in, Home rendering and all Menu URLs. Use the current users table without schema changes. The existing application's session behavior is not described here.

## 2. Account-disable plan

User: Review this technical plan against the supplied repository excerpts. Decide whether implementation can begin and identify consequential corrections. Do not implement.

Requirement: after an administrator disables a user, every subsequent protected request must reject that account, including requests carrying an existing session. Preserve the current one-role-per-user model and database schema.

`disable-account-plan.md`:

> Add `POST /admin/users/{id}/disable`. Call the existing `UserRepository.DisableAsync(id)`, then `SessionRegistry.RevokeAllForUserAsync(id)`. Existing middleware calls `UserRepository.FindActiveAsync` on every protected request, so authorization needs no changes. Test disabling a user and attempting a protected request with their old session. The route is a proposed addition; all named repository and registry methods already exist.

Complete relevant source excerpts:

```csharp
// UserRepository.cs
public Task<User?> FindAsync(int id) => db.Users.FindAsync(id).AsTask();
public async Task SetEnabledAsync(int id, bool enabled) {
    var user = await db.Users.FindAsync(id);
    if (user is null) throw new KeyNotFoundException();
    user.Enabled = enabled;
    await db.SaveChangesAsync();
}
// SessionRegistry.cs
public Task RemoveAsync(string sessionId) => cache.RemoveAsync(sessionId);
// AuthMiddleware.cs -- executed for every protected request
var user = await users.FindAsync(session.UserId);
if (user is null) return Unauthorized();
return Next(user);
```

There are no other repository, registry or middleware methods in this fixture. Source inspection is available; a running application and test runner are not.

## 3. Revised report design

User: Assess this revised solution after review feedback. Recommend what should remain in the scoped implementation and explain the important trade-offs. Do not implement.

Accepted requirements: an existing internal report serves 40 staff, normally 20 requests/day. Fix occasional stale results after editing a record. The existing monolith reads SQL Server directly; its next request already returns committed updates. The stale result was reproduced in a browser tab because the UI retained its prior result. Explicit refresh after saving is acceptable. No offline use, background processing or new freshness/performance target is required. Existing measured query latency is 120 ms; nobody has reported slow queries.

Initial solution: invalidate the report view's local result after a successful edit, fetch the report again, and show a retry action on fetch failure. Preserve the current endpoint and access checks.

Review feedback: clarify how the page behaves if the refresh fails and how repeated refreshes avoid showing an older response over a newer response.

Revised design: add Redis as a shared report cache, an event broker to invalidate Redis entries, and a background refresh worker. Keep a separate cache of each user's last response in the browser. The UI still fetches after saving. The revised text says this architecture future-proofs freshness, but does not specify error/retry presentation or response ordering.

## 4. Settled correction

User: Change only the existing report API to clamp negative remaining quota to zero, preserving its integer response and existing validation. Architecture and requirements are settled. Explain the implementation and verification approach; do not edit code in this exercise.

```python
def remaining_quota(limit, used):
    validate_counts(limit, used)
    return limit - used
```

Existing tests cover invalid counts and the ordinary positive result. No execution environment is supplied.
