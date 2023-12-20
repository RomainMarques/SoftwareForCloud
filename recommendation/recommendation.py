import random
import pandas as pd


def recommend_books(user_email):
    # Load all books from the CSV file
    books = pd.read_csv('books.csv', delimiter=',', on_bad_lines='warn')
    list_book = []

    for i in range(10):
        choosen = random.randint(0, len(books) - 1)
        list_book.append(str(books.iloc[choosen]['title']))
    return list_book
