import requests
import os

NEWS_API = "https://newsapi.org/v2/top-headlines"


def get_trending_news(keyword="AI"):
    params = {
        "q": keyword,
        "language": "en",
        "pageSize": 10,
        "apiKey": os.getenv("NEWS_API_KEY")
    }

    response = requests.get(NEWS_API, params=params)

    data = response.json()

    return data.get("articles", [])