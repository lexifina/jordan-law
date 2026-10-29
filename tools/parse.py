"""Jordan: parse the Constitution (Arabic, MFA copy with all amendments to 2022-01-31) into corpus.json.
Usage: python -X utf8 parse.py <constitution.pdf>   (text comes from pdftotext -layout)."""
import hashlib, json, re, subprocess, sys
from pathlib import Path

PDF = Path(sys.argv[1])
URL = 'https://www.mfa.gov.jo/documents/230322%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1%202022.pdf'
RETRIEVED = '2026-10-29'
sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
raw = subprocess.run(['pdftotext', '-enc', 'UTF-8', '-layout', str(PDF), '-'], capture_output=True, check=True).stdout.decode('utf8')
for ch in '‪‫‬‎‏‭‮\r\f':
    raw = raw.replace(ch, '' if ch != '\f' else '\n')
raw = raw.replace(' ', ' ')
L = raw.split('\n')

starts = []
n = 1
for i, l in enumerate(L):
    if n > 131:
        break
    if re.match(r'^\s*المادة', l) and len(l.strip()) < 30 and n in [int(x) for x in re.findall(r'\d+', l)]:
        starts.append((i, n))
        n += 1
assert len(starts) == 131, len(starts)
end = next(i for i, l in enumerate(L) if i > starts[-1][0] and re.match(r'^\s*1952', l.strip()))

FOOT = re.compile(r'^\s*\(\s*\)\s*\d+\s*بموجب')


def article(lines):
    paras = []
    for l in lines:
        s = l.strip()
        if not s or FOOT.match(s) or re.fullmatch(r'\d{1,3}', s):
            continue
        s = re.sub(r'\)\d+\(', '', s)           # footnote markers
        s = re.sub(r'^(\(\s*\)\d+\s*)+', '', s)   # leading footnote markers before a clause number
        s = re.sub(r'\(\s*\)\s*(\d+)', r'(\1)', s)   # references like ( )29
        s = s.strip()
        if not s:
            continue
        m = re.match(r'^[.\-]\s*(\d+)\s*(.*)$', s)
        if m:
            paras.append('%s. %s' % (m.group(1), m.group(2)))
        elif paras:
            paras[-1] += ' ' + s
        else:
            paras.append(s)
    out = []
    for p in paras:
        p = re.sub(r'\s+([،.:؛])', r'\1', p)
        p = re.sub(r'\s*،\s*', '، ', p).replace(' ،', '،')
        p = re.sub(r'\s{2,}', ' ', p).strip()
        out.append(p)
    return out


units = {}
bounds = starts + [(end, 0)]
for (a, num), (b, _) in zip(bounds, bounds[1:]):
    ps = article(L[a + 1:b])
    assert ps, num
    units['art-%03d' % num] = {'label': 'المادة %d' % num, 'kind': 'article',
                               'text': '# المادة %d\n' % num + '\n'.join(ps) + '\n'}

credits = {k: ['publisher-oldest'] for k in units}
FROM = '2022-01-31'
corpus = {
    'country': {
        'code': 'JO', 'name': 'Jordan', 'slug': 'jordan', 'lang': 'ar', 'tz': 'Asia/Amman', 'future_branch': 'future',
        'publisher': {'name': 'Ministry of Foreign Affairs of Jordan (mfa.gov.jo)', 'email': 'constitution@mfa-gov-jo.invalid'},
        'default_in_force_rule': {'text': 'This record dates an amendment by the Official Gazette date the source gives.',
                                  'source': 'https://www.mfa.gov.jo'},
        'licence_note': 'Text of the Constitution of the Hashemite Kingdom of Jordan, with all amendments to 31 January 2022, as published on mfa.gov.jo. The site states no licence; its robots.txt content signal allows reference use (use=reference) and forbids AI training, and this repository is a reference copy.'},
    'sources': [{'name': 'Ministry of Foreign Affairs of Jordan, Constitution of the Hashemite Kingdom of Jordan (2022 edition)',
                 'url': URL, 'retrieved': RETRIEVED,
                 'licence': 'No licence stated; robots.txt content signal search=yes, ai-train=no, use=reference',
                 'notes': 'PDF sha256 %s; born-digital PDF with an Arabic text layer, read with pdftotext. The Legislation and Opinion Bureau (lob.gov.jo) is a script-driven site and the Ministry of Justice (moj.gov.jo) serves the Constitution in ten partial chapter files, so neither was used.' % sha}],
    'laws': {'publisher-oldest': {'label': 'Ministry of Foreign Affairs', 'title': 'Ministry of Foreign Affairs of Jordan, 2022 edition, oldest version available',
                                  'kind': 'publisher', 'enacted': FROM, 'published': FROM, 'url': URL,
                                  'temporary_until': None, 'restores': None, 'note': None}},
    'acts': [{'slug': 'constitution', 'short': 'الدستور', 'title': 'دستور المملكة الأردنية الهاشمية (Constitution of the Hashemite Kingdom of Jordan)',
              'url': URL, 'first_law': None, 'earlier_laws': [],
              'versions': [{'from': FROM, 'source_url': URL, 'sha256': sha, 'units': units, 'credits': credits,
                            'note': 'Articles 1 to 131 as printed in the Ministry of Foreign Affairs edition, which includes the amendments published in the Official Gazette up to issue 5770 of 31 January 2022. The Constitution was first published on 8 January 1952; the earlier texts and the amendments of 1958, 1965, 1973, 1974, 1976, 1984, 2011, 2014, 2016 and the 2022 amendment are not separately online in text form here.'}]}],
    'applies': [],
    'decisions': [
        'Language: Arabic, the official language; an official English text was not found in a single clean file.',
        'No dated past versions are online, so there is one version, credited to the publisher as "oldest version available" and dated 31 January 2022, the Official Gazette date of the latest amendment (issue 5770) shown in the source.',
        'Cleaning: footnote lines ("by virtue of the amendment published in issue ...") and their in-text markers, page numbers and bidirectional control characters were removed; clause numbers printed as ".1" were written "1."; line breaks within a clause were joined. Chapter headings, the signature block and the amendment table are not kept.'],
    'ai_use': ['none']}
Path(__file__).with_name('corpus.json').write_text(json.dumps(corpus, indent=1, ensure_ascii=False) + '\n', encoding='utf8', newline='\n')
print(len(units), 'units')
