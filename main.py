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

    try:
        # Follow redirects and retrieve the final URL
        final_url = requests.get(url).url

        # Remove tracking parameters if present
        untracked_url = urllib.parse.urlparse(final_url)
        untracked_url = urllib.parse.urlunparse(untracked_url._replace(query=''))

        # Disable link preview in the message
        disable_preview = {'disable_web_page_preview': True}

        update.message.reply_text(f"Redirected URL: {final_url}\nUnshortened URL: {untracked_url}", disable_web_page_preview=True)
    except requests.exceptions.RequestException:
        update.message.reply_text("An error occurred while retrieving the URL.")


def get_bot_token() -> str:

    # Check for bot token in environment variable
    for key, value in os.environ.items():
        if key.lower() == 'telegram_bot_token':
            return value

    # Check for bot token in config.yaml or config.yml
    for config_file_name in ['config.yaml', 'config.yml']:
        if os.path.isfile(config_file_name):
            with open(config_file_name, 'r') as config_file:
                config = yaml.safe_load(config_file)
                for key, value in config.items():
                    if key.lower() == 'telegram_bot_token':
                        return value

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