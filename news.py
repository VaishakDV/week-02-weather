import requests
import os
from dotenv import load_dotenv

load_dotenv()

class NewsService:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"

    def get_headlines(self, topic="technology", count=5):
        params = {
            "q": topic,
            "apikey": self.api_key,
            "pageSize": count,
            "language":"en"
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        headlines = []
        for article in data["articles"]:
            headlines.append({
                "title": article["title"],
                "source": article["source"]["name"]
            })

        return headlines