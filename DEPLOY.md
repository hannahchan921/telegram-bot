# Telegram Bot — Deployment Guide

## Files needed (keep all 3 together):
- bot.py
- requirements.txt
- welcome.opus

---

## Deploy on Railway (free, runs 24/7)

1. Go to railway.app and sign up with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Create a new GitHub repo and upload all 3 files into it
4. Railway will auto-detect Python and install requirements
5. Click Deploy — done. Bot runs 24/7.

---

## Test locally first (optional)

```
pip install python-telegram-bot==21.3
python bot.py
```

Then message your bot "START" on Telegram — it should reply with the voice message.

---

## To change the trigger keyword
Open bot.py and change: TRIGGER_KEYWORD = "START"

## To use a different voice file
Replace welcome.opus with your new file and update: VOICE_FILE = "your_file.opus"
