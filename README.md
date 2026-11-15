# Jordan: law history in git


The law of Jordan as a git history: one file per provision, one commit per version on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every article; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Jordan's national law, which global-law reads at `jordan/national/acts/`.

**What is in it now:** the Constitution of the Hashemite Kingdom of Jordan, Articles 1 to 131 (131 provisions), in one version: the text with its amendments to the Official Gazette of 31 January 2022 (issue 5770), as the Ministry of Foreign Affairs publishes it. No statute, regulation, treaty or court decision is here yet. [`constitution/README.md`](constitution/README.md) lists every article; [`REPRODUCE.md`](REPRODUCE.md) says how the files were made.

Each act is a folder with one file per provision: `constitution/art-001.md` is Article 1 (المادة 1).

The text is in Arabic, the official language, as the Ministry prints it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 1 of the Constitution | `git log -p --word-diff -- constitution/art-001.md` |
| Which act wrote each line of Article 1? | `git blame constitution/art-001.md` |
| Every version of the Constitution, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution ":^constitution/README.md"` |
| Article 1 as in force on 1 January 2026 | `python tools/on.py 2026-01-01 constitution art-001` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Jordanian law](https://global-law.lexifina.com/v1/try_claude?country=jordan)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=jordan)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=%D8%AD%D8%B1%D9%8A%D8%A9+%D8%A7%D9%84%D8%B1%D8%A3%D9%8A&jurisdictions=jordan)**: a search of Jordanian law for "حرية الرأي" (freedom of opinion), returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Arabic or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add jordan/national/acts
python3 tools/law.py show 2026-01-01 jordan/national/acts/constitution/art-001.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Asia/Amman, on the day the version took effect, and carries it in its `In-force:` trailer:

- the Constitution's one version is dated 31 January 2022, the Official Gazette date of the latest amendment (issue 5770) that the Ministry's edition includes, as the oldest version available. The text is older: the Constitution was first published on 8 January 1952, and its earlier texts are not online as separate versions. A date before 31 January 2022 gives no text.

No version is credited to a law. The one version is credited to the publisher, the Ministry of Foreign Affairs of Jordan (mfa.gov.jo), as the "oldest version available" (`Kind: publisher`). The committer is Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before and compares it with the corpus, whose hash is in `data/corpus.sha256`; it also checks that every commit's trailers parse, that `main` has no merge commits and that no commit is dated in the future.
- `tools/build.py` writes the history from that one corpus file, and the same corpus gives the same commit hashes. [`REPRODUCE.md`](REPRODUCE.md) records that the checks were not yet run for this build and that no second build has been compared.
- The sha256 of the PDF the Constitution was parsed from is in `data/versions.json`.

## What it does not show

- **Amendment history.** The Ministry's edition is one text, so the amendments made since 1952 are in it but not as commits of their own, and no earlier text of the Constitution is here.
- **Footnotes, chapter headings, the signature block and the amendment table** of the Ministry's edition; the footnotes named the Gazette issue of each amendment.
- **Statutes, regulations, treaties and case law.** None yet, and no catalogue of laws.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Ministry of Foreign Affairs of Jordan](https://www.mfa.gov.jo/documents/230322%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1%202022.pdf) | Official site: the Constitution with its amendments, in Arabic (PDF, 2022 edition) | no, one text | Amendments to the Official Gazette of 31 January 2022 (issue 5770); read on 29 October 2026 |

## Licence

See [`LICENSE`](LICENSE). The Ministry's site states no licence; its robots.txt content signal allows use as a reference and forbids AI training; this repository is a reference copy and is not used to train models. Lexifina's history, commit messages and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
