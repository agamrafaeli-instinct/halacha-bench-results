"""Offline checks for the proposal; these do not validate Q&A or run models."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = []
        self.sections = 0
        self.targets = []
        self.proposal_sections = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'section':
            self.sections += 1
            if 'historical' in attrs.get('class', '').split():
                self.proposal_sections.append(attrs)
        if 'href' in attrs:
            self.links.append(attrs['href'])
        if 'src' in attrs:
            self.links.append(attrs['src'])
        if 'data-go' in attrs:
            self.targets.append(attrs['data-go'])


class HistoricalReferenceTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads((ROOT / 'datasets/historical-reference/sources.json').read_text())
        self.html = (ROOT / 'index.html').read_text()

    def test_metadata_only_and_pilot_totals(self):
        c = self.catalog
        self.assertEqual(c['status'], 'proposal_metadata_only')
        self.assertFalse(c['includes_question_or_answer_text'])
        self.assertEqual(c['selected_items'], 0)
        sources = c['sources']
        self.assertEqual(len(sources), 3)
        self.assertEqual(len({s['id'] for s in sources}), 3)
        self.assertEqual(sum(s['proposed_pilot_questions'] for s in sources), 36)
        self.assertEqual(c['proposed_pilot_questions'], 36)
        self.assertEqual(sum(s['proposed_pilot_questions'] for s in sources if s['subject'] == 'issur_veheter'), 24)
        self.assertEqual(sum(s['proposed_pilot_questions'] for s in sources if s['subject'] == 'niddah'), 12)
        for s in sources:
            self.assertEqual(s['proposed_pilot_questions'], 12)
            for field in ('author', 'author_he', 'exam_date_scope', 'source_url', 'listing_url', 'format', 'verified_at'):
                self.assertTrue(s[field], (s['id'], field))
            self.assertRegex(s['source_sha256'], r'^[a-f0-9]{64}$')
            self.assertEqual(s['selected_items'], 0)
            self.assertEqual(s['rights_status'], 'permission_required')
            self.assertIsNone(s['permission_reference'])
            self.assertFalse(s['official_key_verified'])
            self.assertEqual(s['review_status'], 'not_reviewed')
            self.assertEqual(s['overlap_status'], 'unknown')
            self.assertEqual(s['exposure_status'], 'public_historical')
            self.assertEqual(urlsplit(s['source_url']).hostname, 'www.smicha.co.il')
            self.assertNotIn('question_he', s)
            self.assertNotIn('reference_answer_he', s)

    def test_bilingual_pages_navigation(self):
        full = PageParser()
        full.feed(self.html)
        self.assertEqual(len(full.ids), len(set(full.ids)))
        for language in ('en', 'he'):
            start = self.html.index(f'<div id="c-{language}"')
            end = self.html.index('<!-- ============ HEBREW', start) if language == 'en' else self.html.index('<script>', start)
            p = PageParser()
            p.feed(self.html[start:end])
            self.assertEqual(p.sections, 5)
            self.assertEqual(len(p.proposal_sections), 1)
            self.assertEqual(p.proposal_sections[0]['id'], f'historical-{language}')
            self.assertIn(p.proposal_sections[0]['aria-labelledby'], p.ids)
            self.assertIn('3', p.targets)
            self.assertIn('4', p.targets)
            for target in p.targets:
                if target[0] not in '+-':
                    self.assertIn(int(target), range(p.sections))
            for source in self.catalog['sources']:
                self.assertIn(source['source_url'], p.links)

    def test_local_links(self):
        parser = PageParser()
        parser.feed(self.html)
        checks = [(ROOT / 'index.html', link) for link in parser.links]
        for path in (ROOT / 'README.md', ROOT / 'docs/historical-reference.md'):
            checks.extend((path, link) for link in re.findall(r'\]\(([^)]+)\)', path.read_text()))
        for origin, link in checks:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            self.assertTrue((origin.parent / unquote(parsed.path)).exists(), (origin.name, link))

    def test_original_bundle_still_matches_manifest(self):
        bundle = ROOT / 'bundle'
        manifest = json.loads((bundle / 'MANIFEST.json').read_text())
        for name, expected in manifest['files'].items():
            self.assertEqual(hashlib.sha256((bundle / name).read_bytes()).hexdigest(), expected, name)


if __name__ == '__main__':
    unittest.main()
