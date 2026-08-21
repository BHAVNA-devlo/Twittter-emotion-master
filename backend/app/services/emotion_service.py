import re


EMOTION_LABELS = ("Joy", "Sadness", "Anger", "Fear", "Surprise", "Love", "Neutral")

_KEYWORDS = {
    "Joy": {"happy", "excited", "joy", "amazing", "awesome", "great", "love", "celebrate", "win"},
    "Sadness": {"sad", "disappointed", "lonely", "miss", "loss", "lost", "unhappy", "heartbroken"},
    "Anger": {"angry", "furious", "hate", "annoyed", "outrage", "terrible", "frustrating", "scam"},
    "Fear": {"fear", "afraid", "worried", "worry", "risk", "danger", "crash", "concern", "threat"},
    "Surprise": {"surprised", "unexpected", "wow", "shocking", "suddenly", "unbelievable"},
    "Love": {"love", "adore", "favorite", "grateful", "thankful", "support", "care"},
}


def classify_emotion(text: str, sentiment: str) -> str:
    """Lightweight explainable emotion classification; not a trained emotion model."""
    words = set(re.findall(r"[a-z']+", text.lower()))
    scores = {emotion: len(words & keywords) for emotion, keywords in _KEYWORDS.items()}
    best_emotion = max(scores, key=scores.get)
    if scores[best_emotion] == 0:
        return "Neutral" if sentiment == "Neutral" else ("Joy" if sentiment == "Positive" else "Sadness")
    return best_emotion
