#!/usr/bin/env python3
"""Check local Markdown file links and heading anchors; external URLs are skipped."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+)(?:\s+[^)]*)?)\)')
HEAD = re.compile(r'^#{1,6}\s+(.+?)\s*#*\s*$', re.M)

def slug(s):
    s = re.sub(r'[`*_~]', '', s).lower().strip()
    s = re.sub(r'[^\w\-\s]', '', s)
    return re.sub(r'\s+', '-', s)

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    if len(sys.argv) > 2 or not root.is_dir():
        print('Usage: python check_markdown_links.py [project-root]', file=sys.stderr)
        return 2
    files = sorted(root.rglob('*.md'))
    errors, checked = [], 0
    for source in files:
        text = source.read_text(encoding='utf-8')
        for m in LINK.finditer(text):
            target = m.group(1) or m.group(2) or ''
            u = urlsplit(target)
            if u.scheme or u.netloc or target.startswith('//'):
                continue
            if not u.path and not u.fragment:
                continue
            checked += 1
            dest = (source.parent / unquote(u.path)).resolve() if u.path else source.resolve()
            if dest != root and root not in dest.parents:
                errors.append(f'{source.relative_to(root)}: target escapes root: {target}')
                continue
            if not dest.exists():
                errors.append(f'{source.relative_to(root)}: missing target: {target}')
                continue
            if u.fragment and dest.suffix.lower() == '.md':
                headings = [slug(h) for h in HEAD.findall(dest.read_text(encoding='utf-8'))]
                if unquote(u.fragment) not in headings:
                    errors.append(f'{source.relative_to(root)}: missing anchor: {target}')
    print(f'Markdown files: {len(files)}; local links checked: {checked}')
    print('External URLs are not checked.')
    for err in errors: print(err, file=sys.stderr)
    print('FAIL' if errors else 'PASS')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
