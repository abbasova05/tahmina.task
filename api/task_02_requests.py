import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
    else:
        print("Failed to fetch posts for CSV saving.")

fetch_and_print_posts()
fetch_and_save_posts()