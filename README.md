# 🎮 Typing Lab

> A cyberpunk-themed typing defense game where you destroy enemies by typing their words before they reach your base.

[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/sonixz/typing-game/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

**[🎮 Play Now](https://typinglab.io)** | **[📖 Docs](./DEPLOY.md)** | **[🤝 Contributing](./CONTRIBUTING.md)**

## ✨ Features
- **Wave-based gameplay**: Progressive difficulty with enemy waves
- **3 Enemy types**: Normal, Fast, and Tank enemies
- **Dynamic word difficulty**: Easy, Medium, Hard, and Boss word pools
- **Combat system**:
  - Real-time WPM calculation
  - Combo multipliers for consecutive perfect kills
  - Speed-based damage bonuses (Lightning/Blazing/God-like tiers)
- **Shop system**: Buy upgrades between waves
  - Max HP increase
  - Gold multiplier
  - Heal current HP
- **Cyberpunk aesthetic**: Neon colors, scanlines, glitch effects, animated UI

## 🚀 Quick Start

### Play Online
Visit **[typinglab.io](https://typinglab.io)** and start typing!

### Run Locally
1. Clone the repo: `git clone https://github.com/sonixz/typing-game.git`
2. Open `index.html` in your browser
3. Start typing!

No build process, no dependencies. Pure vanilla HTML/CSS/JS.

## 🎯 How to Play

- Type the words on falling enemies to destroy them
- Don't let enemies reach your base
- Perfect kills (no mistakes) build combos and grant bonus rewards
- Survive waves and use gold to buy upgrades in the shop
- Beat your high score!

## 🗺️ Development Roadmap

### Phase 1: Polish & Feel (Quick Wins)
- [ ] Sound design (SFX for hits, explosions, combos)
- [ ] Particle effects and VFX
- [ ] Power-ups system (slow-mo, nuke, shield)
- [ ] Local leaderboard (localStorage)

### Phase 2: More Content
- [ ] Boss waves (every 5 waves)
- [ ] New enemy types (Splitter, Shielder, Cloaker)
- [ ] Achievement system
- [ ] Themes/Skins

### Phase 3: Meta Features
- [ ] Daily challenge mode
- [ ] Endless vs Campaign modes
- [ ] Stats dashboard (WPM, accuracy, reaction time)
- [ ] Mobile support

### Phase 4: Distribution
- [ ] Deploy to itch.io
- [ ] Deploy to GitHub Pages
- [ ] Polish game page with screenshots/GIFs
- [ ] Open source release

## 📦 Project Structure

```
typing-game/
├── index.html              # Main game (all-in-one file)
├── words.json              # Word pools for all difficulties
├── staticwebapp.config.json # Azure deployment config
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
├── DEPLOY.md              # Deployment guide
└── README.md              # You are here
```

## 🎨 Design Philosophy

**100% Vibe Coding** - Building features that feel good, look good, and are fun to code.

Cyberpunk aesthetic with:
- Neon cyan (#00ffff) and hot pink (#ff0080) accents
- Retro scanline effects
- Glitch animations
- Monospace fonts for that terminal vibe

## 🛠️ Tech Stack

- Pure HTML5
- Pure CSS3 (animations, clip-paths, shadows)
- Vanilla JavaScript (no frameworks)

## 🤝 Contributing

We welcome contributions! Whether it's:
- 🐛 Bug fixes
- ✨ New features
- 🎨 Design improvements
- 📝 Documentation
- 🌍 Translations

Check out our [**Contributing Guide**](./CONTRIBUTING.md) to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- Built with 💜 using 100% vibe coding
- Powered by vanilla JavaScript (no frameworks!)
- Deployed on Azure Static Web Apps
- Typography: DM Sans font from Google Fonts

## 📊 Stats

- **Lines of Code**: ~2900+ (single file!)
- **Word Pool**: 1000+ words across 4 difficulty tiers
- **Dependencies**: 0 (pure vanilla)
- **Frameworks**: 0 (just HTML/CSS/JS)

## 🔗 Links

- **Live Game**: [typinglab.io](https://typinglab.io)
- **GitHub Repo**: [github.com/sonixz/typing-game](https://github.com/sonixz/typing-game)
- **Issues**: [Report a bug or request a feature](https://github.com/sonixz/typing-game/issues)
- **Author**: [@sonixz](https://github.com/sonixz)

---

**Made with ⚡ by [@sonixz](https://github.com/sonixz)** | **Star ⭐ this repo if you like it!**
