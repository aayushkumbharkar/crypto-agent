import random


def analyze_sentiment(coin="bitcoin"):
    sentiments = ["positive", "neutral", "negative"]
    sentiment = random.choice(sentiments)

    score_map = {"positive": 0.7, "neutral": 0.5, "negative": 0.3}

    return {"sentiment": sentiment, "score": score_map[sentiment]}
