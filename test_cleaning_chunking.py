import asyncio
from main import TelegramDigestAgent

async def test_cleaning_and_chunking():
    agent = TelegramDigestAgent()
    await agent.client.start()
    messages = await agent.fetch_messages()
    print(f"Fetched {len(messages)} messages")

    # Take first 10 messages for testing
    test_messages = messages[:10]

    # Print raw messages
    print("Raw messages:")
    for msg in test_messages:
        print(f"- {msg.text[:100]}")

    # Clean messages
    cleaned_messages = []
    for msg in test_messages:
        cleaned_text = agent._clean_text_raw(msg.text or "")
        cleaned_messages.append({'id': msg.id, 'text': cleaned_text})

    # Print cleaned messages
    print("Cleaned messages:")
    for msg in cleaned_messages:
        print(f"- {msg['text'][:100]}")

    # Estimate tokens (assuming 4 chars per token)
    def estimate_tokens(text: str) -> int:
        return len(text) // 4

    total_tokens = 0
    for msg in cleaned_messages:
        total_tokens += estimate_tokens(msg['text'])

    print(f"Total estimated tokens for 10 messages: {total_tokens}")

    await agent.client.disconnect()

if __name__ == "__main__":
    asyncio.run(test_cleaning_and_chunking())
