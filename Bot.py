from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Logging for debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Your details
my_details = """
👤 Name: Kaushik Aryan
📚 Class: 11th
📍 Location: Bihar, India
👦 Gender: Male
💻 Developer: Yes
😌 Personality: Calm person
🎂 Age: 16
🎯 Goal: Preparing for NEET
"""if __name__ == "__main__":
    main()

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

def main():
    # ⚠️ TOKEN yahan paste karo (env variable recommended)
    TOKEN = "8010414260:AAGCeBZuzLGTzOTJWrXPohsKpeSeQh3Bgdw"

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    updater.start_polling()
    updater.idle()

# ✅ FIXED ENTRY POINT
if __name__ == "__main__":
    main()
