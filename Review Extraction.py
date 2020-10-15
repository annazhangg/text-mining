from imdbpie import Imdb
import csv
### extracts content from Mulan 2020 page ###
imdb = Imdb()
movie = "Mulan"
url = imdb.search_for_title(movie)[0]
reviews = imdb.get_title_user_reviews(url["imdb_id"])
### creates list of all reviews present on the front page###
csv_list = []
for i in range(len(reviews["reviews"])):
    csv_list.append([reviews["reviews"][i]["reviewText"]])
### stores list into csv###
with open(f"{movie}.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_list)