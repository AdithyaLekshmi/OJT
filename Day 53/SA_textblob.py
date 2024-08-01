#textblob library
#create a sample text

from textblob import TextBlob
texts=["I Love NLP works great and I'am very satisfied",
       "This is my first experience on doing sentiment analysis",
       "The NLP Sentiment analysis is quient interesting it is neither good or bad"]

#create a function to do the sentiment analysis
def analyze_sentiment(text):
    analysis=TextBlob(text)
    polarity= analysis.sentiment.polarity
    if polarity>0:
        sentiment='Positive'
    elif polarity<0:
        sentiment='Negative'
    else:
        sentiment='Neutral'
    return sentiment

for text in texts:
    sentiment=analyze_sentiment(text)
    print(f"Text:{text}")
    print(f"Sentiment: {sentiment}")