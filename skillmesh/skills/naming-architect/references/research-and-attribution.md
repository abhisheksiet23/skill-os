# Naming-skill research and attribution

Inspected directly on GitHub on 2026-11-10. These are selected examples, not an exhaustive survey or an endorsement of their results. Git blob hashes bind the inspected contents; default-branch links may change.

| Source | Verified license | Useful contribution / adaptation |
| --- | --- | --- |
| [sonwr/mcp-domain-radar: naming skill](https://github.com/sonwr/mcp-domain-radar/blob/main/.claude/skills/brand-naming/SKILL.md) | [MIT](https://github.com/sonwr/mcp-domain-radar/blob/main/LICENSE) | Adapted checking candidate domains before recommending, then iterating when the required domains fail. Kept tool choice portable rather than requiring its MCP server. |
| [dbknv/brand-name-generator-skill: availability skill](https://github.com/dbknv/brand-name-generator-skill/blob/main/.claude/skills/name-availability-check/SKILL.md) | [MIT](https://github.com/dbknv/brand-name-generator-skill/blob/main/LICENSE) | Adapted explicit uncertainty, lookup evidence and a compact per-name matrix. Did not import its script, fixed platform sweep, artifact handoff or sibling-skill workflow. |
| [fcoury/brand-naming-codex-skill](https://github.com/fcoury/brand-naming-codex-skill/blob/main/skills/brand-naming/SKILL.md) | [MIT](https://github.com/fcoury/brand-naming-codex-skill/blob/main/LICENSE) | Adapted a concise feature-to-benefit-to-aspiration prompt for creative directions. Did not adopt mandatory large candidate counts, anti-descriptive defaults or scoring. |
| [coreyhaines31/makerskills: domain](https://github.com/coreyhaines31/makerskills/blob/main/skills/domain/SKILL.md) | [MIT](https://github.com/coreyhaines31/makerskills/blob/main/LICENSE) | Useful corroboration for budget/availability constraints, reserved-name handling and unknown errors. No text or code imported. Did not adopt its tool/account setup, purchase/negotiation sequence or universal .com preference. |

Important disagreement: dbknv's [platform reference](https://github.com/dbknv/brand-name-generator-skill/blob/main/.claude/skills/name-availability-check/references/platforms.md) maps an RDAP 404 directly to available. This skill retains the stricter distinction between no registration record and confirmed registrability. A reserved, restricted, unsupported or failed lookup must not become an available verdict. The [IANA bootstrap](https://data.iana.org/rdap/dns.json) locates registry services; [ICANN's RDAP overview](https://www.icann.org/rdap) explains registration-data scope.

Public visibility and a catalog's license label alone do not establish reusable permissions. Inspect the actual repository and any file-specific terms before a later import. MIT notices below are retained for adapted contributions; preserve applicable notices with future copied code/text. No third-party executable was installed or vendored for this change.

## Inspected content identities

| Repository | Skill/reference blob SHA | LICENSE blob SHA |
| --- | --- | --- |
| sonwr/mcp-domain-radar | `c46e6b08590be9b5cc45a0c71e16385f1d6de1bd` | `78617eed81731baa97940859599f80433becdb54` |
| dbknv/brand-name-generator-skill | `b3b9ae58242ee0bfb57b7fca3e09c7c6092b59a5`; platforms `558c1035ae61fa48c03c3974fd67bffdb1c42f14` | `b49629bbae300e41087d48de0a9d210132ce5c46` |
| fcoury/brand-naming-codex-skill | `781269cbacdf52c94d755f3c9d7f33df296bcfd3` | `93e6a343d95383d47f50bfb1e4f6f8fb93fff015` |
| coreyhaines31/makerskills | `a81f1c4398e6a933a78cda900bebf058384ade49` | `29d8e7b039c2bb49681073a8a0b52976c53accd1` |

## MIT notices for adapted contributions

MIT License

Copyright (c) 2026 sonwr

Copyright (c) 2026 Denis Bakanov

Copyright (c) 2026 Fabio Coury

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
