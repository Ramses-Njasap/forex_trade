# Forex Telegram Bot

This project is a simple Telegram bot that provides real-time forex prices for a predefined list of trading pairs. It uses the Alpha Vantage API for fetching forex rates and Telegram's Bot API for interacting with users.

## Features

- Responds to the `/start` command with a welcome message.
- Responds to the `/forex` command with real-time forex prices for selected currency pairs.

## Setup

### 1. Obtain API Keys

#### Telegram Bot API Key

1. Open Telegram and search for the `BotFather` bot.
2. Start a chat with `BotFather` and use the `/newbot` command to create a new bot.
3. Follow the instructions and note down the API token provided.

#### Alpha Vantage API Key

1. Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
2. Sign up for a free API key and note it down.

### 2. Create Python Virtual Environment (preferably in the same directory as your script)

```bash
virtualenv env
```

### 3. Install Dependencies

Ensure you have Python installed, then install the required packages:

```bash
pip install python-telegram-bot alpha_vantage python-dotenv
```

OR

```bash
pip3 install -r requirements.txt
```