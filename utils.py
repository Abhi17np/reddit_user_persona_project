import re

def clean_text(text: str) -> str:
    """
    Cleans Reddit text content by removing unnecessary whitespace, links, and emojis.
    """
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"[\u2000-\uFFFF]", "", text)  # remove non-ASCII characters
    text = re.sub(r"\s+", " ", text)  # normalize whitespace
    return text.strip()

def truncate_text(text: str, max_chars: int = 12000) -> str:
    """
    Trims the text to avoid hitting the token limit of OpenAI models.
    """
    return text[:max_chars]

def sanitize_filename(username: str) -> str:
    """
    Sanitize usernames to be valid filenames.
    """
    safe_username = re.sub(r'[^a-zA-Z0-9_-]', '_', username)
    return f"user_persona_{safe_username}.txt"

