import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
VOICE_FILE = os.path.join(os.path.dirname(__file__), "welcome.opus")
TRIGGER_KEYWORD = "START"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        logging.warning("No message in update")
        return

    text = update.message.text or ""
    logging.info(f"Received: {text}")

    if TRIGGER_KEYWORD in text.upper():
        try:
            if not os.path.exists(VOICE_FILE):
                logging.error(f"File not found: {VOICE_FILE}")
                return

            with open(VOICE_FILE, "rb") as voice:
                await update.message.reply_voice(voice=voice)

            logging.info(f"Voice sent to {update.effective_user.id}")

        except Exception as e:
            logging.error(f"Error sending voice: {e}")

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not set")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
