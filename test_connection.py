import asyncio
from telethon import TelegramClient
import config

async def test_connection():
    client = TelegramClient(
        'telegram_digest_session',
        config.TELEGRAM_API_ID,
        config.TELEGRAM_API_HASH
    )
    
    try:
        print("Connecting to Telegram...")
        await client.start()
        print("Successfully connected!")
        
        # Test fetching messages from the first channel
        channel = config.CHANNELS_TO_MONITOR[0]
        print(f"\nFetching messages from {channel}...")
        
        messages = []
        async for message in client.iter_messages(channel, limit=5):
            messages.append(message)
            print(f"\nMessage from {message.date}:")
            print(f"Text: {message.text[:100]}...")
        
        print(f"\nSuccessfully fetched {len(messages)} messages")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.disconnect()
        print("\nDisconnected from Telegram")

if __name__ == "__main__":
    asyncio.run(test_connection()) 