import os
import yaml
import requests
import urllib.parse
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the URL unshortener bot! Send me a shortened URL, and I will unshorten it for you.')


def handle_message(update: Update, context: CallbackContext) -> None:
    url = update.message.text

    # Follow redirects and retrieve the final URL
    final_url = requests.get(url).url

    # Remove tracking parameters if present
    untracked_url = urllib.parse.urlparse(final_url)
    untracked_url = urllib.parse.urlunparse(untracked_url._replace(query=''))

    update.message.reply_text(f"Unshortened URL: {untracked_url}")


def get_bot_token() -> str:
    # Check for bot token in config.yaml or config.yml
    for config_file_name in ['config.yaml', 'config.yml']:
        if os.path.isfile(config_file_name):
            with open(config_file_name, 'r') as config_file:
                config = yaml.safe_load(config_file)
                bot_token = config.get('telegram_bot_token')
                if bot_token:
                    return bot_token

    # Check for bot token in environment variable
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if bot_token:
        return bot_token

    raise ValueError("Bot token not found. Please provide it in the config.yaml, config.yml file, or set the TELEGRAM_BOT_TOKEN environment variable.")


def main() -> None:
    bot_token = get_bot_token()

    # Initialize the Telegram Bot
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Register the command handlers
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()