# UnshortyBot

![UnshortyBot Icon](icon.png)

UnshortyBot is a Telegram bot that unshortens shortened URLs and removes tracking data.

## Features

- Unshortens shortened URLs and provides the original long URL.
- Removes tracking parameters from the unshortened URL.
- Works with popular URL shortening services.
- Provides a simple and convenient way to unshorten URLs directly in Telegram.

## How to Use

1. Start a chat with the UnshortyBot Bot on Telegram.
2. Send a message containing a shortened URL to the bot.
3. The bot will reply with the unshortened URL and any tracking parameters removed.

## Installation and Setup

1. Clone this repository or download the source code.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain a bot token from the BotFather on Telegram.
4. Set the bot token in a `config.yaml` or `config.yml` file in the following format:

   ```yaml
   telegram_bot_token: YOUR_BOT_TOKEN
   ```
Alternatively, you can set the TELEGRAM_BOT_TOKEN environment variable.

Run the bot using `python main.py`.

## Docker Installation

1. Clone this repository or download the source code.

2. Make sure you have Docker installed on your system. If not, you can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

3. Navigate to the project directory.

4. Set your Telegram bot token in .env file

5. Build and start the Docker containers using the following command:

    `docker-compose up -d`

    This will build the Docker image and start the container in detached mode.

6. Verify that the bot is running by sending a message to the UnshortyBot Bot on Telegram.

Also you can use prebuilt image:

```yaml
---
services:
  app:
    image: nett00n/unshortybot
    environment:
      TELEGRAM_BOT_TOKEN: $TELEGRAM_BOT_TOKEN
version: "3"
```

Set your Telegram bot token in .env file or replace in in `docker-compose.yaml` file.

## Links

- [Telegram Bot](https://t.me/unshortybot)
- [Github Project](https://github.com/nett00n/UnshortyBot)
- [DockerHub Page](https://hub.docker.com/r/nett00n/unshortybot)

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
License

## License

All code in this repository is licensed under the terms of the MIT License. For further information please refer to the LICENSE file.

## Authors

- Vladimir Budylnikov aka [@nett00n](https://github.com/nett00n)

---

2023, Tbilisi, Sakartvelo
