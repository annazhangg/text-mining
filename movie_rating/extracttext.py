from imdbpie import Imdb


def review_extracter(movie):
    """input movie name, outputs txt file with reviews on the front page of imdb"""
    ### extracts content from movie page ###
    imdb = Imdb()
    url = imdb.search_for_title(movie)[0]
    reviews = imdb.get_title_user_reviews(url["imdb_id"])

    ### creates list of all reviews present on the front page###
    imdb = Imdb()
    url = imdb.search_for_title(movie)[0]
    reviews = imdb.get_title_user_reviews(url["imdb_id"])
    ### creates txt file for all reviews present on the front page###
    file = open(f"data/{movie}.txt", "w", encoding="utf-8")
    for i in range(len(reviews["reviews"])):
        line = reviews["reviews"][i]["reviewText"]
        file.write(f"{line}\n")
    file.close()


def main():
    review_extracter("Mulan")


if __name__ == "__main__":
    main()
