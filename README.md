# Catppuccin Mocha userstyles

Stylus userstyles for Kick, Rumble, YouTube, YouTube Music, Google, and Teams. Mocha base `#1e1e2e`, peach primary, mauve links/chips, sky channel names.

Install with Stylus. Leave **Check for updates** ticked. Stylus updates when `@version` in the raw file is higher than the installed copy.

## Install

[![Install Kick](https://img.shields.io/badge/Install-Kick-116b59)](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/kick-catppuccin-mocha.user.css)
[![Install Rumble](https://img.shields.io/badge/Install-Rumble-116b59)](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/rumble-catppuccin-mocha.user.css)
[![Install YouTube](https://img.shields.io/badge/Install-YouTube-116b59)](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/youtube-catppuccin-mocha.user.css)
[![Install YouTube Music](https://img.shields.io/badge/Install-YouTube_Music-116b59)](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/youtube-music-catppuccin-mocha.user.css)
[![Install Google](https://img.shields.io/badge/Install-Google-116b59)](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/google-catppuccin-mocha.user.css)
[![Install Teams](https://img.shields.io/badge/Install-Teams-116b59)](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/teams-catppuccin-mocha.user.css)

| Style | Version | Raw |
| --- | --- | --- |
| Kick Catppuccin Mocha | 1.0.3 | [kick-catppuccin-mocha.user.css](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/kick-catppuccin-mocha.user.css) |
| Rumble Catppuccin Mocha | 1.0.1 | [rumble-catppuccin-mocha.user.css](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/rumble-catppuccin-mocha.user.css) |
| YouTube Catppuccin Mocha | 1.1.3 | [youtube-catppuccin-mocha.user.css](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/youtube-catppuccin-mocha.user.css) |
| YouTube Music Catppuccin Mocha | 1.0.0 | [youtube-music-catppuccin-mocha.user.css](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/youtube-music-catppuccin-mocha.user.css) |
| Google Catppuccin Mocha | 1.0.0 | [google-catppuccin-mocha.user.css](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/google-catppuccin-mocha.user.css) |
| Teams Catppuccin Mocha | 1.0.0 | [teams-catppuccin-mocha.user.css](https://raw.githubusercontent.com/RebbelPigman/catppuccin-mocha-userstyles/main/teams-catppuccin-mocha.user.css) |

YouTube imports the Catppuccin library from `userstyles.catppuccin.com` at apply time. YouTube Music is self-contained and only matches `music.youtube.com`. Google is one file: a shared Material token layer for `*.google.com` (login at `accounts.google.com` excluded), plus product blocks for Drive and Gemini. Gmail, Docs, Calendar, Keep, Photos, Meet, and Chat are next.

Teams matches `teams.cloud.microsoft` and `teams.microsoft.com`. It overrides Fluent v9 tokens (peach primary, mauve links and mentions, sky chat and channel names) and includes a small classic-shell block. Sign-in at `login.microsoftonline.com` is not themed. Set Teams to Dark, and enable Stylus CSP patching if the shell stays blue.
