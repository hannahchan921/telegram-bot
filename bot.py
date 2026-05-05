import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ── CONFIG ──────────────────────────────────────────────────────────────────
BOT_TOKEN = "7253954837:AAEa-6b8C7DK6gZe8YqVbCe1HKOWsvd7NCE"
VOICE_FILE = "welcome.opus"   # must be in the same folder as this script
TRIGGER_KEYWORD = "START"     # case-insensitive
# ────────────────────────────────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    if text.strip().upper() == TRIGGER_KEYWORD:
        with open(VOICE_FILE, "rb") as voice:
            await update.message.reply_voice(voice=voice)
        logging.info(f"Voice sent to {update.effective_user.id}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logging.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
