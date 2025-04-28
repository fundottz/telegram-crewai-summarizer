from typing import List, Dict
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram API credentials
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Message processing settings
PROCESSING_SETTINGS = {
    'max_messages_per_channel': 100,  # Maximum number of messages to fetch per channel
    'include_text_only': True,        # Only process text messages
    'min_message_length': 50,         # Minimum length of message to process
    'chunk_size': 400  # Added chunk_size configuration
}

# Summary preferences
SUMMARY_SETTINGS = {
    'max_length': 500,    # Maximum length of summary
    'min_importance': 0.5, # Minimum importance score (0-1)
    'include_links': True, # Whether to include links in summary
    'group_by_topic': True, # Whether to group similar content
}

# Output settings
OUTPUT_SETTINGS = {
    'format': 'markdown',  # 'markdown' or 'plaintext'
    'send_to': 'saved_messages',  # Where to send the digest
    'include_stats': True,  # Include statistics about processed content
}
