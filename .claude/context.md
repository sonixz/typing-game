# Claude Code - Typing War Context

## Project Overview
**Typing War** - A cyberpunk-themed typing defense game built with pure HTML/CSS/JS.

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

## Current State (v0.1.0)

### Implemented Features
- Core typing mechanics with real-time input handling
- Wave system with progressive difficulty
- 3 enemy types: Normal, Fast, Tank
- 4 word difficulty tiers (easy/medium/hard/boss)
- Combo system for consecutive perfect kills
- WPM calculation and speed-based damage multipliers
- Speed tier announcements (Lightning 60+, Blazing 80+, God-like 100+ WPM)
- Shop system between waves (3 upgrades)
- HUD with health, gold, score, combo display
- Game over screen
- Cyberpunk UI with animations (scanlines, glitch, glow effects)

### Architecture Notes
- Main file: `typing-war.html` (~2900 lines)
- Word pools: `words.json` (357 lines)
- State management: Single `state` object
- Game loop: requestAnimationFrame-based
- Enemy spawning: Random positioning with collision avoidance

### Known Technical Details
- Enemies fall at speed: `0.3 * (1 + waveNum * 0.05)` px/frame
- Fast enemies: 2x speed, less HP
- Tank enemies: 0.5x speed, more HP
- Perfect kill: No mistakes in word typing
- Combo breaks: After 3 seconds of no perfect kills
- Base HP: 100 (upgradeable)
- Starting gold: 50

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
- Phase 2: Boss waves, new enemy types, achievements
- Phase 3: Endless mode, daily challenges, stats dashboard
- Phase 4: Deploy to itch.io and GitHub Pages

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
│   ├── context.md           # This file
│   └── settings.local.json  # Claude Code settings
├── .gitignore
├── CHANGELOG.md
├── README.md
├── typing-war.html          # Main game file
└── words.json               # Word pools
```

## Useful Commands
- Test game: Open `typing-war.html` in browser
- Check git: `git status`, `git log --oneline`
- Line count: `wc -l typing-war.html`

## Notes
- User prefers conversational French communication
- Keep commits professional and descriptive
- Maintain cyberpunk aesthetic consistency
- Prioritize features that "feel good" over optimization
- Single-file architecture is intentional for easy deployment

---
Last updated: 2026-02-12 (Initial setup)
