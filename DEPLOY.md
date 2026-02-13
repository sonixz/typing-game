# Deployment Guide

Quick guide to deploy Typing War online.

## Option 1: GitHub Pages (Recommended)

1. Push this repo to GitHub:
```bash
git remote add origin https://github.com/YOUR_USERNAME/typing-war.git
git push -u origin main
```

2. Enable GitHub Pages:
   - Go to repo Settings > Pages
   - Source: Deploy from branch `main`
   - Folder: `/ (root)`
   - Save

3. Your game will be live at:
   `https://YOUR_USERNAME.github.io/typing-war/typing-war.html`

## Option 2: itch.io (Game Platform)

1. Go to [itch.io/game/new](https://itch.io/game/new)
2. Fill in game details:
   - Title: Typing War
   - Project URL: typing-war
   - Classification: HTML
3. Upload `typing-war.html` and `words.json` as a ZIP
4. Set "This file will be played in the browser" ✓
5. Set index file: `typing-war.html`
6. Publish!

## Option 3: Netlify Drop (Instant)

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag & drop your project folder
3. Get instant URL
4. Optional: Configure custom domain

## Option 4: Vercel (Similar to Netlify)

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow prompts
4. Get instant deployment URL

## Testing Locally

Just open `typing-war.html` in your browser. No server needed!

## Custom Domain

All platforms above support custom domains. Just:
1. Buy domain (Namecheap, Google Domains, etc.)
2. Add CNAME record pointing to your deployment
3. Configure in platform settings

---

**Tip**: For maximum reach, deploy on both GitHub Pages (for portfolio) and itch.io (for gamers).
