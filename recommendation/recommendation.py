import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from fuzzywuzzy import process, fuzz
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
    print("I have the books")
    print(user_books)
    # Load all books from the CSV file
    books = pd.read_csv('books.csv', delimiter=',', on_bad_lines='warn')

    # Calculate cosine similarities
    tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
    tfidf_matrix = tfidf.fit_transform(books['title'] + ' ' + books['authors'] + ' ' + books['publisher'])
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Function to get the most similar books
    def get_similar_books(title, author):
        closest_title = process.extractOne(title, books['title'])[0]
        queried_books = books[(books['title'] == closest_title) & (books['authors'] == author)]
        if not queried_books.empty:
            index = queried_books.index[0]
            similar_indices = cosine_similarities[index].argsort()[:-6:-1]
            similar_items = [(cosine_similarities[index][i], books.iloc[i]) for i in similar_indices]
            return similar_items[1:]  # Exclude the first item (itself)
        else:
            return []

    # Recommend books for the user based on the books they have read and liked
    all_recommendations = []  # List to store all recommendations
    recommended_books = set()  # Set to keep track of books already recommended
    list_book = []
    for user_book in user_books:
        recommendations = get_similar_books(user_book['title'], user_book['author'])
        unique_recommendations = []
        for rec in recommendations:
            if any(fuzz.ratio(rec[1]['title'], rec_title) > 80 for rec_title in recommended_books):
                continue  # Skip if similar title already recommended
            if rec[1]['title'] == user_book['title']:
                continue  # Skip the book itself
            if fuzz.ratio(rec[1]['title'], user_book['title']) > 80:
                continue  # Skip books with similarity > 80%
            unique_recommendations.append(rec)
            recommended_books.add(rec[1]['title'])
        if unique_recommendations:
            all_recommendations.append((user_book['title'], unique_recommendations))

    for user_book, recommendations in all_recommendations:
        print(f"Because you read {user_book}:")
        for score, book in recommendations:
            print(book['title'])
            list_book.append(book['title'])
    return list_book
