import extractimdb
import extracttwitter
import analyze_nltk
import analyze_text
import os


def analyze_movie(movie):
    """shows stats for movie reviews"""
    # if imdb pickle does not exist, extracts pickle
    if not os.path.isfile(f"{movie}_imdb.pickle"):
        extractimdb.review_extracter(movie)
    # if twitter pickle does not exist, extracts pickle
    if not os.path.isfile(f"{movie}_twitter.pickle"):
        extracttwitter.twitter_extracter(movie)

    # process and analyze data
    for source in ["imdb", "twitter"]:
        hist = analyze_text.process_file(movie, source)
        t = analyze_text.most_common(hist, excluding_stopwords=True)
        print()
        print(f"The most common words in {source} reviews:")
        for freq, word in t[0:20]:
            print(f"{word:<10} {freq}")
        print()
        print(f"Histogram of top 10 words in {source} reviews")
        analyze_text.print_most_common(hist, num=10)
        print()
        average, sentiment_list = analyze_nltk.sentiment_analysis(movie, source)
        print(f"The average sentiment on {source} is {average}.")
        print("Individual scores are:")
        print(sentiment_list)


def main():
    movie = "The Mandalorian"
    analyze_movie(movie)


if __name__ == "__main__":
    main()
