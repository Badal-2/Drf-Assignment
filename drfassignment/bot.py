import os
import django

# Django environment setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfassignment.settings')  # ✅ settings ka path
django.setup()

from telegram.ext import Updater, CommandHandler
from mysite.models import TelegramUser  # ✅ app ka naam

def start(update, context):
    username = update.message.from_user.username
    telegram_id = update.message.from_user.id

    TelegramUser.objects.get_or_create(
        username=username,
        telegram_id=telegram_id
    )

    update.message.reply_text(f"👋 Hello {username}, you're now registered!")

def main():
    # ⚠️ Replace this with your actual token
    updater = Updater("PASTE_YOUR_BOT_TOKEN_HERE", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("✅ Bot is running... waiting for /start")
    updater.idle()

if __name__ == '__main__':
    main()
