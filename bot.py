from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging
import os

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Details
my_details = """
👤 Name: Kaushik Aryan
📚 Class: 11th
📍 Location: Bihar, India
👦 Gender: Male
💻 Developer: Yes
😌 Personality: Calm person
🎂 Age: 16
🎯 Goal: Preparing for NEET
"""

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Main ek Telegram Chat Bot hoon 🤖\n\n"
        "Mere creator ke details:\n"
        f"{my_details}\n"
        "Aap mujhse normal chat kar sakte ho 🙂"
    )

# Chat handler
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    if "hello" in user_message or "hi" in user_message:
        reply = "Hi! Kaise ho? 😊"
    elif "neet" in user_message:
        reply = "NEET tough hai, lekin consistency se sab possible hai 💪"
    elif "developer" in user_message:
        reply = "Haan, Kaushik ek developer hai 💻🔥"
    else:
        reply = f"Tumne kaha: {update.message.text}\nMain reply dene ki koshish kar raha hoon 🙂"

    await update.message.reply_text(reply)

def main():
    TOKEN = os.getenv("BOT_TOKEN")

    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
