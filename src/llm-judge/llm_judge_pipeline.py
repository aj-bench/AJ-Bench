#!/usr/bin/env python3
"""
AJ-Bench  ·  LLM-as-a-Judge Unified Entry Point
=================================================

Dispatches to the appropriate judge script in the same directory based on
the domain argument.  All subsequent arguments are forwarded verbatim.

Usage
-----
  python llm_judge_pipeline.py <domain> [domain-args ...]

Domains
-------
  ds                  DS/llm_judge_evaluator.py
  gui                 GUI/llm_judge_evaluator.py
  gui-analyse         GUI/analyse_result.py
  search-deep         Search/deep_llm_judge_pipeline.py
  search-deep-verify  Search/deep_llm_judge_verify.py
  search-wide         Search/wide_llm_judge_pipeline.py
  search-wide-verify  Search/wide_llm_judge_verify.py

Examples
--------
  python llm_judge_pipeline.py ds   --model gpt-4o --env-file .mcp_env
  python llm_judge_pipeline.py gui  --model gpt-4o --env-file .mcp_env
  python llm_judge_pipeline.py search-deep  --judge_model gpt-4o --filter_model Gemini
  python llm_judge_pipeline.py search-wide  --judge_model gpt-4o --filter_model Grok
  python llm_judge_pipeline.py <domain> --help
"""

import runpy
import sys
import textwrap
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────────────
# ANSI colour helpers  (no third-party dependencies)
# ──────────────────────────────────────────────────────────────────────────────

_NO_COLOR = not sys.stdout.isatty()


def _c(code: str, text: str) -> str:
    if _NO_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def bold(t: str)     -> str: return _c("1",    t)
def dim(t: str)      -> str: return _c("2",    t)
def cyan(t: str)     -> str: return _c("36",   t)
def green(t: str)    -> str: return _c("32",   t)
def red(t: str)      -> str: return _c("31",   t)
def bcyan(t: str)    -> str: return _c("1;36", t)
def bgreen(t: str)   -> str: return _c("1;32", t)
def byellow(t: str)  -> str: return _c("1;33", t)
def bmagenta(t: str) -> str: return _c("1;35", t)


# ──────────────────────────────────────────────────────────────────────────────
# Banner  (same "AJ" style as agent_judge_pipeline.py)
# ──────────────────────────────────────────────────────────────────────────────

_BANNER = r"""
    _         _         ____                  _
   / \       | |       | __ )  ___ _ __   ___| |__
  / _ \   _  | |  ___  |  _ \ / _ \ '_ \ / __| '_ \
 / ___ \ | |_| | |___/ | |_) |  __/ | | | (__| | | |
/_/   \_\ \___/        |____/ \___|_| |_|\___|_| |_|
"""

# ──────────────────────────────────────────────────────────────────────────────
# Domain registry  (_BASE is this script's directory)
# ──────────────────────────────────────────────────────────────────────────────

_BASE = Path(__file__).resolve().parent

# (domain_key, path_relative_to_BASE, color_fn)
_DOMAIN_TABLE = [
    ("ds",                 "DS/llm_judge_evaluator.py",             bgreen),
    ("gui",                "GUI/llm_judge_evaluator.py",            bcyan),
    ("gui-analyse",        "GUI/analyse_result.py",                 bcyan),
    ("search-deep",        "Search/deep_llm_judge_pipeline.py",     byellow),
    ("search-deep-verify", "Search/deep_llm_judge_verify.py",       byellow),
    ("search-wide",        "Search/wide_llm_judge_pipeline.py",     bmagenta),
    ("search-wide-verify", "Search/wide_llm_judge_verify.py",       bmagenta),
]

_VALID_DOMAINS = {d for d, *_ in _DOMAIN_TABLE}
_SCRIPT_MAP    = {d: _BASE / p  for d, p, _ in _DOMAIN_TABLE}
_COLOR_MAP     = {d: fn         for d, _, fn in _DOMAIN_TABLE}

_EXAMPLES = [
    ("ds",                 "--model gpt-4o --env-file .mcp_env"),
    ("gui",                "--model gpt-4o --env-file .mcp_env"),
    ("gui-analyse",        "--result_dir ./LLM-as-a-Judge_GUI"),
    ("search-deep",        "--judge_model gpt-4o --filter_model Gemini"),
    ("search-deep-verify", "--result-file results/deep_out.json"),
    ("search-wide",        "--judge_model gpt-4o --filter_model Grok"),
    ("search-wide-verify", "--result-file results/wide_out.json"),
]

_SCRIPT = "llm_judge_pipeline.py"


def _paint(domain: str, text: str) -> str:
    return _COLOR_MAP.get(domain, bcyan)(text)


# ──────────────────────────────────────────────────────────────────────────────
# Help
# ──────────────────────────────────────────────────────────────────────────────

def print_help() -> None:
    width = 76

    print(bcyan(_BANNER))
    print(bold("  AJ-Bench  ·  LLM-as-a-Judge Evaluation Pipeline"))
    print(dim("  " + "─" * (width - 2)))
    print()

    # Domains table
    print(bold("  Domains"))
    print()
    col_w = 24
    print("  " + cyan(f"{'DOMAIN':<{col_w}}") + cyan("SCRIPT"))
    print("  " + dim("─" * (width - 2)))
    for d, p, _ in _DOMAIN_TABLE:
        print("  " + _paint(d, f"{d:<{col_w}}") + dim(p))
    print()

    # Usage
    print(bold("  Usage"))
    print()
    print(f"  {green(f'python {_SCRIPT} <domain> [domain-args ...]')}")
    print()
    print(
        textwrap.fill(
            "All arguments after <domain> are forwarded verbatim to the target "
            "script.  Pass --help as the first domain argument to see per-domain "
            "options.",
            width=width,
            initial_indent="  ",
            subsequent_indent="  ",
        )
    )
    print()

    # Examples
    print(bold("  Examples"))
    print()
    for domain, rest in _EXAMPLES:
        print(f"  {dim('$')} python {_SCRIPT} {_paint(domain, domain)} {rest}")
    print()

    # Footer
    print(dim("  " + "─" * (width - 2)))
    print(dim(f"  Add --help after a domain to see its full argument list.\n"))


# ──────────────────────────────────────────────────────────────────────────────
# Dispatch
# ──────────────────────────────────────────────────────────────────────────────

def _dispatch(domain: str, remaining_argv: list[str]) -> None:
    script_path = _SCRIPT_MAP[domain]

    if not script_path.exists():
        print(
            f"\n  {red('✗')} Script not found: {bold(str(script_path))}\n"
        )
        sys.exit(1)

    # Forward sys.argv so the target script's argument parser sees its own args.
    sys.argv = [str(script_path)] + remaining_argv

    label = _paint(domain, domain.upper())
    print(bold(f"\n  ┌─ AJ-Bench · LLM-as-a-Judge · {label} ──────────────────"))
    print(dim(f"  │  script : {script_path.relative_to(_BASE)}"))
    if remaining_argv:
        print(dim(f"  │  args   : {' '.join(remaining_argv)}"))
    print(bold("  └" + "─" * 57 + "\n"))

    # runpy.run_path works for both:
    #   - scripts with  if __name__ == "__main__": main()
    #   - scripts that execute at module level (e.g. HfArgumentParser-based)
    runpy.run_path(str(script_path), run_name="__main__")


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print_help()
        sys.exit(0)

    domain = args[0].lower()

    if domain not in _VALID_DOMAINS:
        valid = "  ".join(_paint(d, d) for d, *_ in _DOMAIN_TABLE)
        print(
            f"\n  {red('✗')} Unknown domain {bold(repr(domain))}.\n"
            f"  Valid choices:\n\n    {valid}\n"
        )
        print_help()
        sys.exit(1)

    _dispatch(domain, args[1:])


if __name__ == "__main__":
    main()
