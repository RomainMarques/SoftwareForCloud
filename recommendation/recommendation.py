import random
import pandas as pd
import requests
import json


def recommend_books(user_email):
    url = "http://localhost:3000/server/getbooksfromowner/"+str(user_email)

    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        print("Response content:", response.text)
        return
    user_books = json.loads(response.text)
    # Load all books from the CSV file
    books = pd.read_csv('books.csv', delimiter=',', on_bad_lines='warn')
    list_book = []

    for i in range(10):
        choosen = random.randint(0, len(books) - 1)
        list_book.append(books.iloc[choosen]['title'])
    return list_book
