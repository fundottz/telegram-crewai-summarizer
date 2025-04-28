from langchain.tools import tool

@tool
def clean_text(content: str) -> str:
    """Clean text by removing emojis, repeated links, images, videos, and unnecessary symbols"""
    import re

    # Remove emojis (basic pattern for common emojis)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub(r'', content)

    # Remove URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    text = url_pattern.sub('', text)

    # Remove image and video tags (common markdown or HTML patterns)
    media_pattern = re.compile(r'!\[.*?\]\(.*?\)|<img.*?>|<video.*?>.*?</video>', flags=re.DOTALL)
    text = media_pattern.sub('', text)

    # Remove repeated whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()

    return text

@tool
def analyze_importance(content: str) -> float:
    """Analyze the importance of a piece of content"""
    # This is a placeholder - in reality, you'd use a more sophisticated
    # analysis method, possibly using OpenAI's API
    return 0.8  # Example importance score

@tool
def create_summary(content: str) -> str:
    """Create a summary of the content"""
    # This is a placeholder - in reality, you'd use OpenAI's API
    # or another summarization service
    return f"Summary of: {content[:100]}..."
