import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from alpha_vantage.foreignexchange import ForeignExchange
import logging
from dotenv import load_dotenv

# Loading environment variables from a .env file
load_dotenv()

# Setting up logging to track bot's activity and debug issues
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Retrieving API tokens from environment variables
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# Defining the list of forex trading pairs you want to track
PAIRS = [('USD', 'EUR'), ('USD', 'JPY'), ('GBP', 'USD'), ('AUD', 'USD'), ('USD', 'CHF')]

def start(update: Update, context: CallbackContext) -> None:
    """
    Handles the /start command.
    Sends a welcome message to the user with instructions.
    """
    update.message.reply_text('Hello! Use /forex to get real-time forex prices.')

def forex(update: Update, context: CallbackContext) -> None:
    """
    Handles the /forex command.
    Fetches real-time forex prices for predefined trading pairs
    and sends the rates to the user.
    """
    # Initialize the ForeignExchange object with your Alpha Vantage API key
    fx = ForeignExchange(key=ALPHA_VANTAGE_API_KEY)
    message = ''
    # Iterating through the list of forex trading pairs
    for base, target in PAIRS:
        try:
            # Fetching the exchange rate data from Alpha Vantage
            data, _ = fx.get_currency_exchange_rate(from_currency=base, to_currency=target)
            # Extracting the exchange rate value from the response
            rate = float(data['5. Exchange Rate'])
            # Appending the formatted rate to the message
            message += f'{base}/{target}: {rate:.4f}\n'
        except Exception as e:
            # Handling any errors that occur during data fetching
            message += f'Error fetching rate for {base}/{target}: {e}\n'
    
    # Sending the constructed message with exchange rates to the user
    update.message.reply_text(message)

def main() -> None:
    """
    Main function to start the Telegram bot.
    Initializes the Updater and Dispatcher,
    registers command handlers, and starts polling.
    """
    # Creating an Updater object with your Telegram bot token
    if not TELEGRAM_API_TOKEN:
        raise ValueError('Telegram API token not set in environment variables.')
    updater = Updater(TELEGRAM_API_TOKEN)
    dispatcher = updater.dispatcher

    # Registering command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('forex', forex))

    # Starts polling for updates from Telegram
    updater.start_polling()

    # Keeping the bot running until interrupted
    updater.idle()

if __name__ == '__main__':
    # Entry point of the script
    main()
