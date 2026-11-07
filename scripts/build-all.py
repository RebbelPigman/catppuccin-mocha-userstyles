#!/usr/bin/env python3
"""Regenerate all-catppuccin-mocha.user.css from the per-site styles."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "all-catppuccin-mocha.user.css"
VERSION = "1.2.0"

FILES = [
    "kick-catppuccin-mocha.user.css",
    "rumble-catppuccin-mocha.user.css",
    "youtube-catppuccin-mocha.user.css",
    "youtube-music-catppuccin-mocha.user.css",
    "google-catppuccin-mocha.user.css",
    "teams-catppuccin-mocha.user.css",
    "onedrive-catppuccin-mocha.user.css",
    "github-catppuccin-mocha.user.css",
    "grok-catppuccin-mocha.user.css",
    "discord-catppuccin-mocha.user.css",
    "spotify-catppuccin-mocha.user.css",
    "quillbot-catppuccin-mocha.user.css",
    "claude-catppuccin-mocha.user.css",
]

META_RE = re.compile(r"/\*\s*==UserStyle==.*?==/UserStyle==\s*\*/", re.S)

HEADER = f"""/* ==UserStyle==
@name         Catppuccin Mocha — Everything
@namespace    github.com/RebbelPigman
@version      {VERSION}
@description  One-click install of every Catppuccin Mocha userstyle in this repo (Kick, Rumble, YouTube, YouTube Music, Google, Teams, OneDrive, GitHub, Grok, Discord, Spotify, QuillBot, Claude). Use this OR the per-site styles — not both. Mocha base #1e1e2e, peach primary, mauve links, sky names.
@author       Rebbel
@license      MIT

@preprocessor less
@var select lightFlavor "Light Flavor" ["latte:Latte", "frappe:Frappé", "macchiato:Macchiato", "mocha:Mocha*"]
@var select darkFlavor "Dark Flavor" ["latte:Latte", "frappe:Frappé", "macchiato:Macchiato", "mocha:Mocha*"]
@var select accentColor "Primary accent (progress, subscribe, live)" ["rosewater:Rosewater", "flamingo:Flamingo", "pink:Pink", "mauve:Mauve", "red:Red", "maroon:Maroon", "peach:Peach*", "yellow:Yellow", "green:Green", "teal:Teal", "blue:Blue", "sapphire:Sapphire", "sky:Sky", "lavender:Lavender", "subtext0:Gray"]
@var checkbox logo "Enable YouTube logo" 1
@var checkbox oled "Enable black bars" 0
@var checkbox sponsorBlock "Enable SponsorBlock segments" 1
@updateURL    https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/all-catppuccin-mocha.user.css
@downloadURL  https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/all-catppuccin-mocha.user.css
==/UserStyle== */

/* Bundled build — regenerate with: python3 scripts/build-all.py */
"""


def main() -> None:
    parts = [HEADER]
    for name in FILES:
        path = ROOT / name
        if not path.is_file():
            raise SystemExit(f"missing {path}")
        body = META_RE.sub("", path.read_text(), count=1).lstrip("\n")
        parts.append(f"\n/* ===== {name} ===== */\n")
        parts.append(body)
        if not body.endswith("\n"):
            parts.append("\n")
    text = "".join(parts)
    markers = text.count("==UserStyle==")
    if markers != 1:
        raise SystemExit(f"expected 1 UserStyle block, found {markers}")
    OUT.write_text(text)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(text)} bytes)")


if __name__ == "__main__":
    main()
