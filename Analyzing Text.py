import csv
from textblob import TextBlob
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

with open('Mulan.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile)
    sentiment = [[SentimentIntensityAnalyzer().polarity_scores(row[0]),
TextBlob(row[0]).sentiment] for row in readCSV]
    print(type(sentiment[0][1]))
    for items in sentiment:
        print(items)