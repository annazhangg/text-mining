import pickle
from wordcloud import WordCloud

def wordcloud_draw(data, color='black'):
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()])
    word_cloud = WordCloud(stopwords=STOPWORDS,
                          background_color=color,
                          width=2500,
                          height=2000
                          ).generate(cleaned_word)
    plt.figure(1, figsize=(13, 13))
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()

movie = ('The Godfather')
with open(f"{movie}.pickle", "rb") as input_file:
    copy = pickle.load(input_file)

wordcloud_draw(copy, 'white')