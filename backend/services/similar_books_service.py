import pickle
import numpy as np

# Load the saved files
# pt = pickle.load(open('pt.pkl', 'rb'))
# books = pickle.load(open('books.pkl', 'rb'))
# similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))


def recommend(book_name):
    # # index fetch
    # index = np.where(pt.index == book_name)[0][0]
    # similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
    #
    # data = []
    # for i in similar_items:
    #     item = []
    #     temp_df = books[books['Book_Title'] == pt.index[i[0]]]
    #     item.extend(list(temp_df.drop_duplicates('Book_Title')['Book_Title'].values))
    #     item.extend(list(temp_df.drop_duplicates('Book_Title')['Author'].values))
    #
    #     data.append(item)
    #
    # return data
    pass


def get_similar_books(book_name: str):
    return recommend(book_name)
