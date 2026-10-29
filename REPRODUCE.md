# How this repository was made (Jordan)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Ministry of Foreign Affairs of Jordan, Constitution of the Hashemite Kingdom of Jordan (2022 edition) | <https://www.mfa.gov.jo/documents/230322%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1%202022.pdf> | 2026-10-29 | No licence stated |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | دستور المملكة الأردنية الهاشمية (Constitution of the Hashemite Kingdom of Jordan) | 1 | 2022-01-31 to 2022-01-31 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Asia/Amman) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: This record dates an amendment by the Official Gazette date the source gives. https://www.mfa.gov.jo

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `24f83593f2cc446039def15c7cc098c8a520bd1089d823417edd3f26347d0305` (99773 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `6229396f41c9d7f1d6f405becfbe4097b35b82da`, `check.py` `5e112e6a33b7e93d00112e55f01fbb4fb3fdd8da`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Language: Arabic, the official language; an official English text was not found in a single clean file.
- No dated past versions are online, so there is one version, credited to the publisher as "oldest version available" and dated 31 January 2022, the Official Gazette date of the latest amendment (issue 5770) shown in the source.
- Cleaning: footnote lines ("by virtue of the amendment published in issue ...") and their in-text markers, page numbers and bidirectional control characters were removed; clause numbers printed as ".1" were written "1."; line breaks within a clause were joined. Chapter headings, the signature block and the amendment table are not kept.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
