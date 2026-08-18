#!/usr/bin/env python3
"""
Small lexical interface to the Socratink Brain.

This helper discovers the vault, finds stable IDs, performs lightweight ranked
text search, assembles a task-scoped path list, shows one object, reports
ontology/code tandem status, and delegates to the Brain's own validator.
It does not decide truth or authority.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Iterable

ROOT_FILES = ("CONSTITUTION.md", "NORTH-STAR.md", "CURRENT STATE.md")
DEFAULT_AREAS = (
    "50 Active",
    "40 Views",
    "20 Canon",
    "30 Procedures",
)
SOURCE_AREA = "10 Sources"
ARCHIVE_AREA = "90 Archive"

ID_RE = re.compile(r"(?mi)^id:\s*([A-Z]+-\d+)\s*$")
ID_TOKEN_RE = re.compile(r"^[A-Z]+-\d+$")
LIVE_COMMIT_RE = re.compile(r"(?mi)^live_repo_commit:\s*([0-9a-f]{7,40})\s*$")

ORIENT_READS = (
    ("CONSTITUTION.md", "invariants"),
    ("NORTH-STAR.md", "direction"),
    ("CURRENT STATE.md", "live-implementation"),
    ("50 Active/Current Milestone.md", "active-execution"),
    ("50 Active/Current Experiments.md", "active-experiment"),
    ("40 Views/Agent/Learner Agent Contract.md", "architecture-view"),
)

BRAIN_CONTRACT_FIELDS = (
    "North-star fit",
    "Current-state boundary",
    "Canon relied on",
    "Active bet/experiment",
    "Procedure",
    "Evidence/proof obligation",
    "Claims this work must NOT make",
)


def is_brain_root(path: Path) -> bool:
    return path.is_dir() and all((path / name).exists() for name in ROOT_FILES)


def git_toplevel(start: Path) -> Path | None:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if proc.returncode != 0:
        return None
    top = proc.stdout.strip()
    return Path(top) if top else None


def add_discovery_roots(candidates: list[Path], start: Path) -> None:
    candidates.append(start)
    candidates.append(start / "socratink-brain")
    for parent in [start, *start.parents]:
        candidates.append(parent / "socratink-brain")
    top = git_toplevel(start)
    if top is None:
        return
    candidates.append(top)
    candidates.append(top / "socratink-brain")
    candidates.append(top.parent / "socratink-brain")


def locate_brain(explicit: str | None = None) -> Path:
    """Locate the Brain without embedding a machine-specific absolute path.

    Resolution order:
    1. --brain / explicit path from the caller
    2. SOCRATINK_BRAIN_PATH (local environment only)
    3. current directory if it is a Brain root
    4. a sibling/ancestor checkout named socratink-brain, discovered from cwd,
       this script's location, or the consuming repository's git toplevel
    """
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    env = os.environ.get("SOCRATINK_BRAIN_PATH")
    if env:
        candidates.append(Path(env).expanduser())

    add_discovery_roots(candidates, Path.cwd())
    add_discovery_roots(candidates, Path(__file__).resolve().parent)

    seen = set()
    for candidate in candidates:
        try:
            candidate = candidate.resolve()
        except FileNotFoundError:
            continue
        if candidate in seen:
            continue
        seen.add(candidate)
        if is_brain_root(candidate):
            return candidate

    raise SystemExit(
        "Could not locate Socratink Brain. Clone it as a sibling named "
        "socratink-brain, set SOCRATINK_BRAIN_PATH locally, or pass --brain."
    )


def git_info(repo: Path | None) -> dict[str, object]:
    if repo is None:
        return {"present": False}
    top = git_toplevel(repo)
    if top is None:
        return {"present": False, "root": str(repo)}
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=top, capture_output=True, text=True
    )
    short = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], cwd=top, capture_output=True, text=True
    )
    dirty = subprocess.run(
        ["git", "status", "--porcelain"], cwd=top, capture_output=True, text=True
    )
    return {
        "present": head.returncode == 0,
        "root": str(top),
        "head": head.stdout.strip() if head.returncode == 0 else None,
        "head_short": short.stdout.strip() if short.returncode == 0 else None,
        "dirty": bool(dirty.stdout.strip()) if dirty.returncode == 0 else None,
    }


def find_app_root(brain: Path) -> Path | None:
    seen: set[Path] = set()
    ordered: list[Path] = []
    for cand in (
        brain.parent / "socratink",
        git_toplevel(Path.cwd()),
        git_toplevel(Path(__file__).resolve().parent),
    ):
        if cand is None:
            continue
        try:
            resolved = cand.resolve()
        except FileNotFoundError:
            continue
        if resolved in seen:
            continue
        seen.add(resolved)
        ordered.append(resolved)
    brain_resolved = brain.resolve()
    for cand in ordered:
        if cand == brain_resolved:
            continue
        if (cand / ".agents" / "skills" / "socratink-brain").is_dir():
            return cand
    return None


def live_repo_commit(brain: Path) -> str | None:
    current = brain / "CURRENT STATE.md"
    if not current.is_file():
        return None
    m = LIVE_COMMIT_RE.search(read_text(current)[:2000])
    return m.group(1) if m else None


def tandem_status(app_head: str | None, named: str | None) -> str:
    if not app_head or not named:
        return "unknown"
    a = app_head.lower()
    n = named.lower()
    if a.startswith(n) or n.startswith(a):
        return "match"
    return "mismatch"


def markdown_files(root: Path, include_sources: bool = False) -> Iterable[Path]:
    areas = list(DEFAULT_AREAS)
    if include_sources:
        areas.append(SOURCE_AREA)
    for area in areas:
        base = root / area
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if ".git" not in path.parts and ".obsidian" not in path.parts:
                yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def stable_id(path: Path) -> str | None:
    m = ID_RE.search(read_text(path)[:4000])
    return m.group(1) if m else None


def score(query: str, path: Path, text: str) -> int:
    terms = [t.lower() for t in re.findall(r"[A-Za-z0-9_-]+", query) if len(t) > 1]
    if not terms:
        return 0
    name = path.name.lower()
    body = text.lower()
    s = 0
    for term in terms:
        s += name.count(term) * 25
        s += body[:6000].count(term) * 3
        s += body[6000:].count(term)
    # Authority-aware lexical bias: discovery aid, not truth.
    parts = set(path.parts)
    if "50 Active" in parts:
        s += 12
    elif "40 Views" in parts:
        s += 9
    elif "20 Canon" in parts:
        s += 8
    elif "30 Procedures" in parts:
        s += 5
    elif "10 Sources" in parts:
        s -= 2
    return s


def excerpt(text: str, query: str, limit: int = 500) -> str:
    terms = [t.lower() for t in re.findall(r"[A-Za-z0-9_-]+", query) if len(t) > 1]
    low = text.lower()
    positions = [low.find(t) for t in terms if low.find(t) >= 0]
    pos = min(positions) if positions else 0
    start = max(0, pos - 160)
    end = min(len(text), start + limit)
    out = re.sub(r"\s+", " ", text[start:end]).strip()
    return out


def find_by_id(root: Path, needle: str) -> list[Path]:
    hits = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        if stable_id(path) == needle:
            hits.append(path)
    return hits


def cmd_locate(args):
    root = locate_brain(args.brain)
    print(json.dumps({"brain_root": str(root)}, indent=2))


def cmd_orient(args):
    root = locate_brain(args.brain)
    app = find_app_root(root)
    brain_git = git_info(root)
    app_git = git_info(app)
    named = live_repo_commit(root)
    app_head = app_git.get("head")
    tandem = tandem_status(app_head if isinstance(app_head, str) else None, named)
    read_now = []
    for rel, role in ORIENT_READS:
        path = root / rel
        read_now.append({"path": rel, "role": role, "exists": path.is_file()})
    print(json.dumps({
        "brain_root": str(root),
        "app_root": str(app) if app else None,
        "brain_git": brain_git,
        "app_git": app_git,
        "current_state_live_repo_commit": named,
        "tandem": tandem,
        "read_now": read_now,
        "brain_contract_fields": list(BRAIN_CONTRACT_FIELDS),
        "next": [
            "Read every existing read_now path from brain_root before planning or coding.",
            'Then run: python .agents/skills/socratink-brain/scripts/brain.py context "<task>"',
            "Then run: python .agents/skills/socratink-brain/scripts/brain.py show <ID>",
            "Fill a Brain Contract before writing product code.",
        ],
        "note": (
            "orient is a map, not authority. Read the files. "
            "tandem=mismatch means CURRENT STATE may not describe this socratink checkout."
        ),
    }, indent=2))


def cmd_lookup(args):
    root = locate_brain(args.brain)
    needle = args.id.upper()
    hits = []
    for path in find_by_id(root, needle):
        hits.append({
            "id": needle,
            "path": str(path.relative_to(root)),
            "title": path.stem,
        })
    print(json.dumps({
        "brain_root": str(root),
        "matches": hits,
        "next": f"python .agents/skills/socratink-brain/scripts/brain.py show {needle}",
    }, indent=2))
    if not hits:
        raise SystemExit(2)


def cmd_show(args):
    root = locate_brain(args.brain)
    token = args.target.strip()
    paths: list[Path] = []
    as_path = root / token
    if as_path.is_file():
        paths = [as_path]
    elif ID_TOKEN_RE.match(token.upper()):
        paths = find_by_id(root, token.upper())
    else:
        paths = find_by_id(root, token.upper())
        if not paths and as_path.exists():
            print(json.dumps({
                "brain_root": str(root),
                "target": token,
                "error": "path exists but is not a file",
            }, indent=2))
            raise SystemExit(2)
    if not paths:
        print(json.dumps({"brain_root": str(root), "target": token, "matches": []}, indent=2))
        raise SystemExit(2)
    if len(paths) > 1:
        print(json.dumps({
            "brain_root": str(root),
            "target": token,
            "matches": [str(path.relative_to(root)) for path in paths],
            "note": "Multiple matches. Pass a Brain-relative path to show.",
        }, indent=2))
        raise SystemExit(2)
    path = paths[0]
    print(json.dumps({
        "brain_root": str(root),
        "id": stable_id(path),
        "path": str(path.relative_to(root)),
        "content": read_text(path),
    }, indent=2))


def search_results(root: Path, query: str, include_sources: bool, limit: int):
    rows = []
    for path in markdown_files(root, include_sources=include_sources):
        text = read_text(path)
        s = score(query, path.relative_to(root), text)
        if s <= 0:
            continue
        rows.append({
            "score": s,
            "id": stable_id(path),
            "path": str(path.relative_to(root)),
            "excerpt": excerpt(text, query),
        })
    rows.sort(key=lambda r: (-r["score"], r["path"]))
    return rows[:limit]


def cmd_search(args):
    root = locate_brain(args.brain)
    rows = search_results(root, args.query, args.include_sources, args.limit)
    print(json.dumps({"brain_root": str(root), "query": args.query, "results": rows}, indent=2))


def cmd_context(args):
    root = locate_brain(args.brain)
    required = []
    for name in ROOT_FILES:
        required.append({
            "path": name,
            "role": "root-authority",
            "exists": (root / name).is_file(),
        })
    rows = search_results(root, args.query, args.include_sources, args.limit)
    print(json.dumps({
        "brain_root": str(root),
        "query": args.query,
        "read_first": required,
        "task_scoped_candidates": rows,
        "next": "Read read_first from brain_root, then show only the IDs required to decide.",
        "note": "Search ranking is lexical discovery only; follow wikilinks into relevant Canon.",
    }, indent=2))


def cmd_validate(args):
    root = locate_brain(args.brain)
    validator = root / "scripts" / "validate_brain.py"
    if not validator.exists():
        raise SystemExit(f"Validator not found: {validator}")
    proc = subprocess.run([sys.executable, str(validator)], cwd=root)
    raise SystemExit(proc.returncode)


def build_parser():
    p = argparse.ArgumentParser(
        description="Socratink Brain lexical interface",
        epilog=(
            "Coding-agent default: orient → read read_now files → context "
            "\"<task>\" → show <ID> → Brain Contract → code."
        ),
    )
    p.add_argument("--brain", help="Path to Socratink Brain root")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("locate", help="Print the Brain root path")
    s.set_defaults(func=cmd_locate)

    s = sub.add_parser(
        "orient",
        help="Tandem status plus the mandatory product-work read set",
    )
    s.set_defaults(func=cmd_orient)

    s = sub.add_parser("lookup", help="Find a stable ID and print its path")
    s.add_argument("id", help="Stable ID, e.g. EVD-0004")
    s.set_defaults(func=cmd_lookup)

    s = sub.add_parser("show", help="Print one Brain object by ID or relative path")
    s.add_argument("target", help="Stable ID or Brain-relative path")
    s.set_defaults(func=cmd_show)

    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--include-sources", action="store_true")
    s.add_argument("--limit", type=int, default=10)
    s.set_defaults(func=cmd_search)

    s = sub.add_parser("context")
    s.add_argument("query")
    s.add_argument("--include-sources", action="store_true")
    s.add_argument("--limit", type=int, default=10)
    s.set_defaults(func=cmd_context)

    s = sub.add_parser("validate")
    s.set_defaults(func=cmd_validate)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
