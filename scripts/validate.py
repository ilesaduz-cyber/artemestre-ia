#!/usr/bin/env python3
"""Dependency-free structural and privacy checks for the ArteMestre IA repo.

Usage: python scripts/validate.py
Exit code 0 when every check passes, 1 otherwise.

Optional private denylist: put one term per line in private/denylist.txt
(the folder is git-ignored) to block personal or client names from leaking
into public files without listing those names in this script.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'artemestre-ia'
TEXT_EXT = {'.md', '.py', '.json', '.yaml', '.yml', '.txt'}
SKIP_DIRS = {'.git', 'private', 'local-references', 'dist', '__pycache__'}
SECRET_PATTERNS = {
    'OpenAI key': r'sk-(?:proj-)?[A-Za-z0-9_-]{20,}',
    'Anthropic key': r'sk-ant-[A-Za-z0-9_-]{20,}',
    'GitHub token': r'gh[pousr]_[A-Za-z0-9]{30,}',
    'AWS key': r'AKIA[0-9A-Z]{16}',
    'private key': r'-----BEGIN [A-Z ]*PRIVATE KEY-----',
    'e-mail': r'[\w.+-]+@(?:gmail|hotmail|outlook|yahoo)\.com',
    'local path': r'[A-Za-z]:\\Users\\',
}
# old folder name: a path with it in install docs no longer works
STALE_NAMES = ('gpt-creative-studio',)

errors = []


def check(ok, msg):
    if not ok:
        errors.append(msg)


def public_files():
    for p in ROOT.rglob('*'):
        if p.is_file() and not SKIP_DIRS.intersection(p.relative_to(ROOT).parts):
            yield p


# 1. SKILL.md frontmatter
entry_path = SKILL / 'SKILL.md'
entry = entry_path.read_text(encoding='utf-8')
check('\r' not in entry, 'SKILL.md must use LF line endings')
fm = re.match(r'---\n(.*?)\n---\n', entry, re.S)
check(fm is not None, 'SKILL.md is missing YAML frontmatter')
if fm:
    meta = dict(re.findall(r'(?m)^(\w[\w-]*): (.+)$', fm.group(1)))
    check(meta.get('name') == SKILL.name, 'frontmatter name must equal the folder name')
    check(re.fullmatch(r'[a-z0-9-]{1,64}', meta.get('name', '')) is not None,
          'name must be lowercase letters, digits and hyphens, max 64')
    desc = meta.get('description', '')
    check(0 < len(desc) <= 1024, f'description must be 1-1024 chars (has {len(desc)})')
    check('<' not in desc and '>' not in desc, 'description must not contain < or >')
check(len(entry.splitlines()) <= 500, 'SKILL.md should stay under 500 lines')

# 2. every referenced module exists, and every module is referenced
refs = set(re.findall(r'`(references/[^`]+\.md)`', entry))
check(bool(refs), 'SKILL.md references no modules')
for r in sorted(refs):
    check((SKILL / r).is_file(), f'missing referenced module: {r}')
for p in sorted((SKILL / 'references').glob('*.md')):
    check(f'references/{p.name}' in refs, f'module not routed from SKILL.md: references/{p.name}')

# 3. key capabilities are still described
combined = '\n'.join(p.read_text(encoding='utf-8') for p in SKILL.rglob('*.md')).lower()
for needed in ('fidelidade', '3d', 'pesquisar', 'qualidade', 'autorizacao'):
    check(needed in combined, f'capability keyword missing: {needed}')

# 4. manifests are valid JSON and agree on name and version
manifests = {}
for name in ('plugin.json', 'marketplace.json'):
    path = ROOT / '.claude-plugin' / name
    try:
        manifests[name] = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        check(False, f'.claude-plugin/{name}: {exc}')
if 'plugin.json' in manifests:
    check(manifests['plugin.json'].get('name') == SKILL.name, 'plugin.json name mismatch')
    version = manifests['plugin.json'].get('version', '')
    changelog = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
    check(f'## {version}' in changelog, f'CHANGELOG.md has no entry for {version}')

# 5. relative links in Markdown point to real files
for p in public_files():
    if p.suffix != '.md':
        continue
    for target in re.findall(r'\]\(([^)#\s]+)', p.read_text(encoding='utf-8')):
        if '://' in target or target.startswith('mailto:'):
            continue
        check((p.parent / target).exists(), f'{p.relative_to(ROOT)}: broken link {target}')

# 6. no secrets, private paths, stale names or denylisted terms in public files
deny_file = ROOT / 'private' / 'denylist.txt'
deny = []
if deny_file.is_file():
    deny = [t.strip().lower() for t in deny_file.read_text(encoding='utf-8').splitlines() if t.strip()]
for p in public_files():
    if p.suffix not in TEXT_EXT or p == Path(__file__).resolve():
        continue
    text = p.read_text(encoding='utf-8')
    rel = p.relative_to(ROOT)
    for label, pat in SECRET_PATTERNS.items():
        check(re.search(pat, text) is None, f'{rel}: looks like a {label}')
    for stale in STALE_NAMES:
        check(stale not in text, f'{rel}: stale name "{stale}"')
    low = text.lower()
    for term in deny:
        check(term not in low, f'{rel}: contains a private denylisted term')

if errors:
    print('FAIL')
    for e in errors:
        print(' -', e)
    sys.exit(1)
extra = f', private denylist ({len(deny)} terms)' if deny else ''
print(f'PASS: frontmatter, {len(refs)} modules, manifests, links, secrets{extra}')
