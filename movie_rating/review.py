import extracttext as extract
import analyze_text as analyze
import os


def analyze_movie(movie):
    """shows stats for movie reviews"""
    if not os.path.isfile(f"{movie}.pickle"):
        extract.review_extracter(movie)

    hist = analyze.process_file(movie)
    t = analyze.most_common(hist, excluding_stopwords=True)
    print()
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(f"{word:<10} {freq}")
    analyze.print_most_common(hist, num=10)


def main():
    analyze_movie("The Godfather")


if __name__ == "__main__":
    main()
