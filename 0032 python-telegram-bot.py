import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello, welcome to my Telegram bot!')

def help(update, context):
    update.message.reply_text('This is a simple Telegram bot. You can interact with it using the following commands: /start, /help')

def main() -> object:
    # Token for your bot, you can get it from BotFather
    token = 'YOUR_TELEGRAM_BOT_TOKEN'
    updater = Updater(token, use_context=True)

    # Register handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
