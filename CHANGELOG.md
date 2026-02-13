# Changelog

All notable changes to Typing Lab will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Massively enriched word pool from 357 to 5,023 unique words
  - Tech/gaming vocabulary (500+ terms): programming languages, frameworks, tools
  - Common English words: 2000+ nouns, 1000+ verbs/adjectives
  - Themed categories: science, space, nature, action words
  - Distribution: 980 easy, 2,018 medium, 1,488 hard, 537 boss words
- Python word generation scripts for reproducibility and future expansion

### Planned
- Sound effects and music
- Particle effects for enemy destruction
- Power-ups system
- Boss waves
- Local leaderboard with persistence

## [0.2.0] - 2026-02-12

### Added
- Footer navigation bar with external links
  - GitHub repository link
  - Leaderboards placeholder (coming soon)
  - Author credit link
- MIT License for open source release
- CONTRIBUTING.md guide for contributors
- Enhanced README with badges and better structure
- Azure Static Web Apps deployment configuration
- Development context documentation (.claude/context.md)
- Deployment guides (DEPLOY.md, azure-static-webapp.md)

### Changed
- **BREAKING**: Renamed `typing-war.html` to `index.html` for cleaner URLs
- Updated all documentation references to use index.html
- Simplified Azure static web app configuration
- Rebranded from "Typing War" to "Typing Lab"
- Improved footer styling with cyberpunk animations

### Fixed
- Azure deployment configuration pointing to old filename
- Root URL now properly serves index.html

### Technical
- Repository prepared for public release
- CI/CD pipeline configured via GitHub Actions
- Auto-deploy on push to main branch

## [0.1.0] - 2026-02-12

### Added
- Initial game release
- Core typing mechanics
- Wave-based gameplay system
- Three enemy types (Normal, Fast, Tank)
- Four word difficulty tiers (Easy, Medium, Hard, Boss)
- Shop system with three upgrades
- Combo system for consecutive perfect kills
- WPM-based damage multipliers
- Speed tier announcements (Lightning, Blazing, God-like)
- Cyberpunk-themed UI with animations
- HUD displaying health, gold, score, and combo
- Game over screen with final stats
- Wave announcements

### Technical
- Single-file HTML architecture
- Embedded CSS with advanced animations
- Vanilla JavaScript game engine
- JSON-based word pool system
