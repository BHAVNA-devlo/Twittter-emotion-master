import re


_URL_PATTERN = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
_MENTION_PATTERN = re.compile(r"@[A-Za-z0-9_]+")
_HASHTAG_PATTERN = re.compile(r"#([A-Za-z0-9_]+)")
_WHITESPACE_PATTERN = re.compile(r"\s+")


def clean_text(text: str) -> str:
    """Remove URLs and mentions while keeping hashtag words readable."""
    cleaned = _URL_PATTERN.sub("", text)
    cleaned = _MENTION_PATTERN.sub("", cleaned)
    cleaned = _HASHTAG_PATTERN.sub(r"\1", cleaned)
    return _WHITESPACE_PATTERN.sub(" ", cleaned).strip()
