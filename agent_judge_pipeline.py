#!/usr/bin/env python3
"""
AJ-Bench  ·  Unified Evaluation Entry Point
============================================

Dispatches to the appropriate domain pipeline based on the first positional
argument.  All subsequent arguments are forwarded verbatim to the underlying
pipeline script.

Usage
-----
  python agent_judge_pipeline.py <domain> [domain-specific args...]

Domains
-------
  ds      Data-Science  –  agent_judge_ds_pipeline.py
  gui     GUI           –  agent_judge_gui_pipeline.py
  search  Web-Search    –  agent_judge_search_pipeline.py

Examples
--------
  python agent_judge_pipeline.py ds     --models gpt-4o --mcp filesystem
  python agent_judge_pipeline.py gui    --model  gpt-4o --pairs-root-dir src/data/GUI
  python agent_judge_pipeline.py search --models gpt-4o --mcp filesystem
  python agent_judge_pipeline.py ds     --help          # show ds-specific help
"""

import sys
import textwrap

# ──────────────────────────────────────────────────────────────────────────────
# ANSI colour helpers  (no third-party dependencies required)
# ──────────────────────────────────────────────────────────────────────────────

_NO_COLOR = not sys.stdout.isatty()


def _c(code: str, text: str) -> str:
    """Wrap *text* in the given ANSI *code*, unless output is not a tty."""
    if _NO_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def bold(t: str)    -> str: return _c("1",      t)
def dim(t: str)     -> str: return _c("2",      t)
def cyan(t: str)    -> str: return _c("36",     t)
def green(t: str)   -> str: return _c("32",     t)
def yellow(t: str)  -> str: return _c("33",     t)
def magenta(t: str) -> str: return _c("35",     t)
def red(t: str)     -> str: return _c("31",     t)
def blue(t: str)    -> str: return _c("34",     t)
def bcyan(t: str)   -> str: return _c("1;36",   t)
def bgreen(t: str)  -> str: return _c("1;32",   t)
def byellow(t: str) -> str: return _c("1;33",   t)


# ──────────────────────────────────────────────────────────────────────────────
# Banner / Help
# ──────────────────────────────────────────────────────────────────────────────

# "A" uses a proper triangular peak (/\) so it reads clearly as "A".
# "J" has the characteristic descending tail (\___/).
_BANNER = r"""
    _         _         ____                  _
   / \       | |       | __ )  ___ _ __   ___| |__
  / _ \   _  | |  ___  |  _ \ / _ \ '_ \ / __| '_ \
 / ___ \ | |_| | |___/ | |_) |  __/ | | | (__| | | |
/_/   \_\ \___/        |____/ \___|_| |_|\___|_| |_|
"""

_DOMAIN_TABLE = [
    ("ds",     "Data-Science",  "agent_judge_ds_pipeline.py",     "green"),
    ("gui",    "GUI",           "agent_judge_gui_pipeline.py",     "cyan"),
    ("search", "Web-Search",    "agent_judge_search_pipeline.py",  "yellow"),
]

_EXAMPLES = [
    ("ds",     "--models gpt-4o --mcp filesystem"),
    ("gui",    "--model  gpt-4o --pairs-root-dir src/data/GUI"),
    ("search", "--models gpt-4o --mcp filesystem"),
    ("ds",     "--help   (domain-specific help)"),
]

_SCRIPT = "agent_judge_pipeline.py"


def _color_for(domain: str) -> str:
    for d, _, _, col in _DOMAIN_TABLE:
        if d == domain:
            return col
    return "cyan"


def _paint(domain: str, text: str) -> str:
    mapping = {"green": bgreen, "cyan": bcyan, "yellow": byellow}
    return mapping.get(_color_for(domain), bcyan)(text)


def print_help() -> None:
    width = 72

    # Header
    print(bcyan(_BANNER))
    print(bold("  AJ-Bench  ·  Unified Agent-Judge Evaluation Pipeline"))
    print(dim("  " + "─" * (width - 2)))
    print()

    # Domains table
    print(bold("  Domains"))
    print()
    col_w = 10
    header = (
        "  "
        + cyan(f"{'DOMAIN':<{col_w}}")
        + cyan("SCRIPT")
    )
    print(header)
    print("  " + dim("─" * (width - 2)))
    for d, _label, script, _ in _DOMAIN_TABLE:
        row = (
            "  "
            + _paint(d, f"{d:<{col_w}}")
            + dim(script)
        )
        print(row)
    print()

    # Usage
    print(bold("  Usage"))
    print()
    usage = f"python {_SCRIPT} <domain> [domain-args ...]"
    print(f"  {green(usage)}")
    print()
    print(
        textwrap.fill(
            "All arguments after <domain> are forwarded verbatim to the "
            "underlying pipeline script.  Pass --help as the first domain "
            "argument to see per-domain options.",
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
# Domain registry
# ──────────────────────────────────────────────────────────────────────────────

_VALID_DOMAINS = {d for d, *_ in _DOMAIN_TABLE}

_MODULE_MAP = {
    "ds":     "agent_judge_ds_pipeline",
    "gui":    "agent_judge_gui_pipeline",
    "search": "agent_judge_search_pipeline",
}


def _dispatch(domain: str, remaining_argv: list[str]) -> None:
    """Import the target pipeline module and call its ``main()``."""
    module_name = _MODULE_MAP[domain]

    # Replace sys.argv so that the target parser sees only its own arguments.
    sys.argv = [module_name + ".py"] + remaining_argv

    label = _paint(domain, domain.upper())
    print(bold(f"\n  ┌─ AJ-Bench · {label} pipeline ─────────────────────────"))
    print(dim(f"  │  module  : {module_name}.py"))
    if remaining_argv:
        print(dim(f"  │  args    : {' '.join(remaining_argv)}"))
    print(bold("  └" + "─" * 55 + "\n"))

    import importlib
    mod = importlib.import_module(module_name)
    mod.main()


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    args = sys.argv[1:]

    # No arguments → print help
    if not args or args[0] in ("-h", "--help"):
        print_help()
        sys.exit(0)

    domain = args[0].lower()

    if domain not in _VALID_DOMAINS:
        print(
            f"\n  {red('✗')} Unknown domain {bold(repr(domain))}. "
            f"Valid choices: {', '.join(_paint(d, d) for d in sorted(_VALID_DOMAINS))}\n"
        )
        print_help()
        sys.exit(1)

    remaining = args[1:]
    _dispatch(domain, remaining)


if __name__ == "__main__":
    main()
