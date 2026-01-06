from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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
def start(update, context):
    update.message.reply_text(
        "Hello! Main ek Telegram Chat Bot hoon 🤖\n\n"
        "Mere creator ke details:\n"
        f"{my_details}\n"
        "Aap mujhse normal chat kar sakte ho 🙂"
    )

# Chat handler
def chat(update, context):
    user_message = update.message.text.lower()

    if "hello" in user_message or "hi" in user_message:
        reply = "Hi! Kaise ho? 😊"
    elif "neet" in user_message:
        reply = "NEET tough hai, lekin consistency se sab possible hai 💪"
    elif "developer" in user_message:
        reply = "Haan, Kaushik ek developer hai 💻🔥"
    else:
        reply = f"Tumne kaha: {update.message.text}\nMain reply dene ki koshish kar raha hoon 🙂"

    update.message.reply_text(reply)



# ... upar ka code (imports, my_details, start(), chat() etc.) ...

def main():
    # 🔐 TOKEN from Environment Variable
    TOKEN = os.getenv("BOT_TOKEN")

    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    updater.start_polling()
    updater.idle()

# 👇 Paste this at the very end of the file
if __name__ == "__main__":
    main()




