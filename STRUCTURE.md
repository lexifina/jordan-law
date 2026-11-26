# Structure of jordan-law

Folder names are in Arabic, the language people search Jordanian law in. Years and numbers use Western digits.
No folder holds more than 1,000 entries.

| Folder | What | One file is |
| --- | --- | --- |
| `الدستور/` | The Constitution of 1952 with its amendments | one article (`art-001.md`) |
| `القوانين/<السنة>/` | Laws and provisional laws, by year | one law (`<الرقم>-<اسم القانون>.md`); later versions are later commits to the same file |
| `الأنظمة/<السنة>/` | Regulations (أنظمة) | one regulation |
| `الجريدة-الرسمية/<السنة>/` | Issues of the Official Gazette | one issue (`العدد-<n>.md`) |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

## Versions and dates

- One commit per version, in the order the versions took effect.
- The author date is 12:00 Amman time on the in-force day: the day the law's own clause gives (its publication in the
  Official Gazette, a stated delay, or the source's "تاريخ العمل به"); a gazette issue on its publication day.
  Before 1970 the date is 1970-01-01 and the real day starts the subject.
- Trailers on every commit: `Kind:`, `In-force:`, `In-force-basis:` (clause and gazette number and date) and `Source:`.
- A version whose in-force day cannot be read is held, not committed.

## Sources

- The Legislation and Opinion Bureau's former plain-HTML site (lob.gov.jo/ui/laws/, 2007 onwards), read from Internet
  Archive copies of its pages (`Source-status: Internet Archive copy`). The current lob.gov.jo is not used.
- The Official Gazette issues published by the Prime Ministry (pm.gov.jo).

`constitution/` was renamed `الدستور/` on 2026-11-26 (a rename only; no text changed).
