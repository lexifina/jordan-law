# Jordan: law history in git

The law of Jordan (JO) as a git history: one file per provision, one commit per law on the day it took effect, and the law that made the change as the commit author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `jo/`.

**First build, deliberately small.** Language: Arabic (the official language), so the text is right-to-left.

| Folder | Text | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Hashemite Kingdom of Jordan, articles 1 to 131 | 1 | Oldest version available: the text with all amendments to the Official Gazette of 31 January 2022 (issue 5770) |

**Why only this.** The Legislation and Opinion Bureau ([lob.gov.jo](https://www.lob.gov.jo)) is a script-driven site with no plain text of the laws, and Jordan publishes no dated past versions of its statutes online. The Ministry of Foreign Affairs publishes the whole Constitution as one born-digital PDF, so that is the first text recorded. The earlier texts (the Constitution of 8 January 1952 and its amendments before 2022) are not available as separate versions here, so the history starts at this version.

**Source:** [Ministry of Foreign Affairs of Jordan](https://www.mfa.gov.jo), official, retrieved 29 October 2026. See `LICENSE` and `REPRODUCE.md`.

Dates are the day the change took effect. This repository is not legal advice; for anything that matters, read the original.
