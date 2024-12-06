from transformers import pipeline
import torch

def analyze_sentiment(headlines):
  device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

  analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest", device=device)
  raw_sentiments = analyzer(headlines)

  sentiments = []

  for sentiment in raw_sentiments:
    if sentiment["label"] == "negative":
      sentiments.append(sentiment["score"])
    elif sentiment["label"] == "neutral":
      sentiments.append(1 + sentiment["score"])
    elif sentiment["label"] == "positive":
      sentiments.append(2 + sentiment["score"])

  return sentiments