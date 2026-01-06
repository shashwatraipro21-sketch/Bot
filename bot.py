from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
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
def start(update, context):
    update.message.reply_text(
        "Hello! Main ek Telegram Chat Bot hoon 🤖\n\n"
        "Mere creator ke details:\n"
        f"{my_details}\n"
        "Aap mujhse baat kar sakte ho 🙂"
    )

# Chat handler
def chat(update, context):
    text = update.message.text.lower()

    if "hi" in text or "hello" in text:
        reply = "Hi! Kaise ho? 😊"
    elif "neet" in text:
        reply = "NEET tough hai, lekin consistency se ho jayega 💪"
    elif "developer" in text:
        reply = "Haan, Kaushik ek developer hai 💻🔥"
    else:
        reply = f"Tumne kaha: {update.message.text}"

    update.message.reply_text(reply)

def main():
    TOKEN = os.getenv("BOT_TOKEN")

    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable not set")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
