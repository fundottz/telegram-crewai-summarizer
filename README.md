# Telegram News Digest AI Agent

This project uses CrewAI and Telethon to create daily digests from your Telegram channels. It helps you save time by summarizing content and identifying important news items worth deeper reading.

## Features

- Automated daily digest generation from Telegram channels
- AI-powered content summarization
- Priority-based news ranking
- Customizable digest format

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your credentials:
```
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
OPENAI_API_KEY=your_openai_api_key
```

3. Run the agent:
```bash
python main.py
```

## Configuration

- Edit `config.py` to customize:
  - List of channels to monitor
  - Digest generation schedule
  - Summary preferences
  - Output format

## How it works

1. The agent connects to Telegram using Telethon
2. Fetches new messages from specified channels
3. Uses CrewAI to analyze and summarize content
4. Generates a prioritized digest
5. Sends the digest to your specified output channel 