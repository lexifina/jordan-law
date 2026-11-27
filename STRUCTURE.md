# Structure of jordan-law

Folder names are in Arabic, the language people search Jordanian law in. Years and numbers use Western digits.
No folder holds more than 1,000 entries.

| Folder | What | One file is |
| --- | --- | --- |
| `الدستور/` | The Constitution of 1952 with its amendments | one article (`art-001.md`) |
| `القوانين/<السنة>/` | Laws and provisional laws, by year | one law (`<الرقم>-<اسم القانون>.md`); later versions are later commits to the same file |
| `الأنظمة/<السنة>/` | Regulations (أنظمة) | one regulation |
| `التعليمات/<السنة>/` | Instructions (تعليمات) | one set of instructions (`<الرقم>-<الاسم>.md`) |
| `الاتفاقيات/<السنة>/` | Agreements ratified by law (اتفاقيات) | one agreement |
| `الجريدة-الرسمية/<السنة>/` | Issues of the Official Gazette | one issue (`العدد-<n>.md`) |
| `الأحكام/<المحكمة>/<السنة>/<الشهر>/<اليوم>/` | Court decisions (محكمة-التمييز, محكمة-التمييز/الهيئة-العامة, المحكمة-الإدارية-العليا, محكمة-العدل-العليا, المحكمة-الدستورية), one per decision, dated by the decision day | one decision (`<حقوق|جزاء>-<الرقم>-<السنة>.md`) |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

## Versions and dates

- One commit per version, in the order the versions took effect.
- The author date is 12:00 Amman time on the in-force day: the day the law's own clause gives (its publication in the
  Official Gazette, a stated delay, or the source's "تاريخ العمل به"); a gazette issue on its publication day.
  Before 1970 the date is 1970-01-01 and the real day starts the subject.
- Trailers on every commit: `Kind:`, `In-force:`, `In-force-basis:` (clause and gazette number and date) and `Source:`.
- A version whose in-force day cannot be read is held, not committed.
- A text known only in its final, consolidated form (all amendments merged in) is one version dated by the in-force day of the latest amendment it incorporates (`Kind: consolidated`, `Consolidated-through:`, `In-force-basis: latest-amendment ...`); never a bare year or 1 January.

## Court decisions

- `الأحكام/` holds Jordanian court decisions, one file per decision, committed at 12:00 Amman time on the
  decision day the citation gives (`رقم 78/2018 فصل 25/1/2018`). Decisions cited without a full day are
  left out.
- Until an official source is reachable they are read from free public secondary copies (first:
  lawpedia.jo, which quotes the principles of each decision), marked on every commit (`Source-copy:`,
  `Source-copy-status: secondary copy; verification against the official text pending`).
- Personal-status, juvenile, sexual-offence and honour-crime decisions are not published here.

## Sources

- The Legislation and Opinion Bureau's former plain-HTML site (lob.gov.jo/ui/laws/, 2007 onwards), read from Internet
  Archive copies of its pages (`Source-status: Internet Archive copy`). The current lob.gov.jo is not used.
- The Official Gazette issues published by the Prime Ministry (pm.gov.jo).
- LawCodex/jo (github.com/LawCodex/jo), a third-party copy of the Bureau's current database made on 2026-10-13: a secondary copy (`Source-copy`, `Source-copy-status` trailers), pending verification against the official text. Laws and regulations already here from the Bureau's former site are not imported again.

`constitution/` was renamed `الدستور/` on 2026-11-26 (a rename only; no text changed).
