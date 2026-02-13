# Claude Code - Typing Lab Context

## Project Overview
**Typing Lab** (formerly "Typing War") - A neon-styled typing defense game built with pure HTML/CSS/JS. Open source (MIT License) and deployed at [typinglab.io](https://typinglab.io).

## Development Guidelines

### Language
- **User communication**: French (user speaks in French)
- **Code & Documentation**: English (all output, docs, comments, commits in English)
- **Commit messages**: English, descriptive, with feature lists

### Code Style
- **Philosophy**: 100% Vibe Coding - prioritize feel, aesthetics, and fun
- **Architecture**: Single-file HTML when possible, keep it simple
- **No frameworks**: Pure vanilla JavaScript
- **Comments**: Minimal, code should be self-explanatory
- **Aesthetic**: Cyberpunk/neon theme (cyan #00ffff, pink #ff0080, purple #8a2be2)

### Git Workflow
- Claude manages all commits
- Descriptive commit messages with bullet points
- CHANGELOG.md updated for each version
- Co-authored by Claude in all commits

### Testing
- Manual browser testing (no automated tests for now)
- Test in Chrome/Firefox
- Check responsiveness as features are added

## Current State (v0.2.0+)

### Implemented Features
- Core typing mechanics with real-time input handling
- Wave system with **arcade-style progressive difficulty** (12% speed increase per wave)
- **Game timer** showing elapsed time in MM:SS format
- 3 enemy types: Normal (0.9 base speed), Fast (1.4 base speed), Tank (0.6 base speed)
- **5,000+ word pool** with random subset loading (~2,200 words per session)
  - Tech/gaming vocabulary (500+ terms)
  - Common English words (2000+ nouns, 1000+ verbs/adjectives)
  - Themed categories (science, space, nature)
  - Distribution: 980 easy, 2018 medium, 1488 hard, 537 boss words
- Combo system for consecutive perfect kills
- WPM calculation and speed-based damage multipliers
- Speed tier announcements (Lightning 60+, Blazing 80+, God-like 100+ WPM)
- Shop system between waves with **balanced economy** (reduced gold, higher upgrade costs)
- HUD with health, gold, score, combo, and **timer** display
- Game over screen with final stats
- Neon-styled UI with animations (scanlines, glitch, glow effects)
- **Footer navigation** with GitHub repo, Discord (coming soon), Leaderboards (coming soon) links
- **Favicon** (neon "T" logo)

### Architecture Notes
- Main file: `index.html` (~2900 lines, single-file architecture)
- Word pools: `words.json` (5,023 words, 76KB)
  - **Random subset loading**: Each session loads 45-50% of total pool using Fisher-Yates shuffle
  - Status message shows: "X random words loaded"
- State management: Single `state` object with timer tracking
- Game loop: requestAnimationFrame-based with timer updates
- Enemy spawning: Random positioning with collision avoidance, **spawn at y: -100** to prevent word cutoff

### Known Technical Details
- **Arcade difficulty scaling**: Base speed × (1 + waveNum × 0.12)
- Enemy base speeds: Normal 0.9, Fast 1.4, Tank 0.6 (increased ~30-40% from original)
- Enemy counts per wave: 5 + waveNum × 2 (increased from 3 + waveNum × 2)
- **Economy balance** (tightened ~40-50%):
  - Gold per enemy: Normal 6, Fast 9, Tank 18 (reduced from 10/15/30)
  - Upgrade costs: Damage 75+40×level, Slow 100+50×level, Heal 50, Gold multiplier 90+30×level
- Perfect kill: No mistakes in word typing
- Combo breaks: After 3 seconds of no perfect kills
- Base HP: 100 (upgradeable)
- Starting gold: 50
- Timer starts when game begins, displayed in MM:SS format

## Development Roadmap

### Next Priority: Phase 1 (Polish & Feel)
1. **Sound System** - Core SFX integration
   - Typing hit sounds
   - Enemy death explosions
   - Combo sound effects
   - Wave complete jingle
   - Game over sound
   - Shop purchase sound

2. **Particle Effects** - Visual juice
   - Enemy explosion particles
   - Damage number animations (already has basic version)
   - Combo streak effects
   - Perfect kill celebrations

3. **Power-ups** - Gameplay variety
   - Slow-mo (slows all enemies temporarily)
   - Nuke (destroys all on-screen enemies)
   - Shield (protects base from next hit)
   - Double gold (temporary 2x gold multiplier)

4. **Local Leaderboard** - Persistence
   - localStorage integration
   - Top 10 scores display
   - Player name input
   - Stats tracking (highest wave, highest combo, etc.)

### Future Phases
- Phase 2: Boss waves, new enemy types, achievements, themes/skins
- Phase 3: Endless mode, daily challenges, stats dashboard, mobile support
- Phase 4: Distribution
  - ✅ Open source release (MIT License)
  - ✅ Deploy to Azure Static Web Apps
  - ⏳ Deploy to itch.io
  - ⏳ Deploy to GitHub Pages (alternative)
  - ⏳ Polish game page with screenshots/GIFs

## Session Workflow

### Starting a Session
1. Check git status and recent commits
2. Review current task from roadmap
3. Confirm direction with user
4. Code the feature
5. Test in browser
6. Commit with descriptive message

### Ending a Session
1. Commit all work
2. Update CHANGELOG.md if significant changes
3. Update this context file if needed
4. Summary of what was accomplished

## File Structure
```
typing-game/
├── .claude/
│   ├── context.md              # This file - development context
│   └── settings.local.json     # Claude Code settings
├── .github/
│   └── workflows/
│       └── azure-static-web-apps-*.yml  # GitHub Actions CI/CD
├── .gitignore
├── CHANGELOG.md                # Version history
├── CONTRIBUTING.md             # Contribution guidelines
├── DEPLOY.md                   # Deployment guide
├── LICENSE                     # MIT License
├── README.md                   # Project documentation
├── index.html                  # Main game file (~2900 lines)
├── staticwebapp.config.json    # Azure Static Web Apps config
└── words.json                  # Word pool (5,023 words, 76KB)
```

### Note on Python Scripts
- `generate_words.py` and `enrich_words_mega.py` exist **locally only** (in .gitignore)
- Used for word pool generation/enrichment
- Not deployed (caused Azure build failures)

## Useful Commands
- Test game: Open `index.html` in browser
- Check git: `git status`, `git log --oneline`
- Line count: `wc -l index.html`
- Word pool stats: `python3 -c "import json; data = json.load(open('words.json')); print(f'Total: {sum(len(v) for v in data.values())}')"`
- Check deployment: Visit [typinglab.io](https://typinglab.io)

## Deployment
- **Platform**: Azure Static Web Apps
- **CI/CD**: GitHub Actions (auto-deploy on push to main)
- **Build**: No build process needed (pure static HTML/CSS/JS)
- **Config**: `staticwebapp.config.json` handles routing
- **Important**: Python scripts excluded from deployment (.gitignore) to prevent build errors

## Notes
- User prefers conversational French communication
- Keep commits professional and descriptive
- Maintain neon/cyberpunk aesthetic consistency (avoid overusing "cyberpunk" in branding)
- Prioritize features that "feel good" over optimization (100% vibe coding)
- Single-file architecture is intentional for easy deployment
- **Repository is PUBLIC** - all commits and docs should be professional
- Open source (MIT License) - welcoming contributions

## Recent Major Changes (Session 2026-02-12)
1. **Rebranded** from "Typing War" to "Typing Lab"
2. **Renamed** main file from `typing-war.html` to `index.html`
3. **Word pool enrichment**: 357 → 5,023 words with random subset loading
4. **Difficulty increase**: 30-40% faster enemies, 12% per wave scaling, more enemies
5. **Economy rebalance**: 40% less gold, 50% higher upgrade costs for arcade feel
6. **Added timer**: MM:SS format showing game duration
7. **Footer navigation**: GitHub, Discord (soon), Leaderboards (soon)
8. **Deployment**: Azure Static Web Apps with auto-deploy via GitHub Actions
9. **Documentation**: Added LICENSE, CONTRIBUTING.md, DEPLOY.md
10. **Fixed**: Enemy spawn position (y: -100), input field alignment, Python scripts causing deployment failures

---
Last updated: 2026-02-12 (v0.2.0+ - Word pool enrichment & documentation)
