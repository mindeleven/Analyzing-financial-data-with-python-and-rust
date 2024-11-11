# filename: search_arxiv.py
import requests

# Define the search query
search_query = "machine learning healthcare"
url = f"http://export.arxiv.org/api/query?search_query=all:{search_query}&start=0&max_results=5"

# Make the request to arXiv
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Papers found:")
    print(response.text)
else:
    print("Failed to retrieve papers.")