# def author_data_fetch(author):
#     url = "https://www.googleapis.com/books/v1/volumes"
#     params = {
#         'q': f'inauthor:{author}',
#         'maxResults': 10
#     }

# sample_date=input("Enter Author Name :")
# author_data_fetch(sample_date)


import requests
# API endpoint
url = "https://www.googleapis.com/books/v1/volumes"

# Parameters: we search for books by "Agatha Christie"
params = {
    "q": "inauthor:Agatha Christie",
    "maxResults": 5
}

# Make the GET request
response = requests.get(url, params=params)

# Print the raw JSON response
print(response.json())

