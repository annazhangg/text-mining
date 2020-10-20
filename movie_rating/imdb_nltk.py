from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle

movie = ("The Godfather")
with open(f"{movie}.pickle", "rb") as input_file:
    copy = pickle.load(input_file)

for line in copy:
    score = SentimentIntensityAnalyzer().polarity_scores(line)
    print(score['compound'])