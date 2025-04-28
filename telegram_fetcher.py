from crewai import Agent
from telethon import TelegramClient
from telethon.tl.types import Message, Channel
from telethon.tl.functions.channels import GetChannelsRequest
from typing import List, Dict
import config
from datetime import datetime, timezone
from tools import clean_text

class TelegramFetcher(Agent):
    role = 'Telegram Fetcher'
    goal = 'Fetch messages from Telegram channels'
    backstory = "You are a Telegram fetcher who can retrieve messages from subscribed channels."
    verbose = True

    def __init__(self):
        self.client = TelegramClient(
            'telegram_digest_session',
            config.TELEGRAM_API_ID,
            config.TELEGRAM_API_HASH
        )

    async def get_user_channels(self) -> List[Dict]:
        """Get all channels the user is subscribed to, excluding private chats and groups"""
        channelNames = ["Топор Live"]
        channels = []
        async for dialog in self.client.iter_dialogs():
            # Check if it's a channel (not a group or private chat)
            if isinstance(dialog.entity, Channel) and dialog.is_channel:
                try:
                    # Get detailed channel info
                    channel_info = await self.client(GetChannelsRequest([dialog.entity]))
                    if channel_info.chats:
                        channel = channel_info.chats[0]
                        if channel.title in channelNames:
                            channels.append({
                                'id': channel.id,
                                'title': channel.title,
                                'username': channel.username,
                                'participants_count': channel.participants_count if hasattr(channel, 'participants_count') else 0
                            })
                except Exception as e:
                    print(f"Error getting info for channel {dialog.title}: {e}")
                    continue
        
        print(f"Found {len(channels)} channels")
        return channels

    async def fetch_messages(self) -> List[Message]:
        """Fetch today's messages from all user's channels"""
        messages = []
        channels = await self.get_user_channels()
        print(f"Found {len(channels)} channels to process")
        
        # Get today's date in UTC
        today = datetime.now(timezone.utc).date()
        
        for channel in channels:
            try:
                print(f"Processing channel: {channel['title']} (participants: {channel['participants_count']})")
                async for message in self.client.iter_messages(
                    channel['id'],
                    limit=config.PROCESSING_SETTINGS['max_messages_per_channel'],
                    offset_date=datetime.combine(today, datetime.min.time()).replace(tzinfo=timezone.utc)
                ):
                    if message.text and len(message.text) >= config.PROCESSING_SETTINGS['min_message_length']:
                        messages.append(message)
            except Exception as e:
                print(f"Error processing channel {channel['title']}: {e}")
                continue
        
        return messages

    async def fetch_cleaned_messages(self) -> List[Dict]:
        """Fetch messages and return cleaned message dicts with id and cleaned text"""
        raw_messages = await self.fetch_messages()
        cleaned_messages = []
        for msg in raw_messages:
            cleaned_text = clean_text(msg.text or "")
            cleaned_messages.append({'id': msg.id, 'text': cleaned_text})
        return cleaned_messages
