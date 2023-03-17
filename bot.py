import os
import telegram
import openai
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

load_dotenv() # load environment variables from .env file

# set up Telegram bot
bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])

# set up OpenAI API
openai.api_key = os.environ['OPENAI_API_KEY']

# define command handlers
def start(update, context):
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Hi! I am a bot powered by OpenAI. Send me a message and I will try to generate a response.')

def generate_response(update, context):
    """Generate a response using OpenAI API."""
    message = update.message.text
    response = openai.Completion.create(engine="davinci", prompt=message, max_tokens=60)
    update.message.reply_text(response.choices[0].text)

def unknown(update, context):
    """Handle unknown commands."""
    update.message.reply_text("Sorry, I don't understand that command.")

# set up handlers
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_response))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

def main():
    """Start the bot."""
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
