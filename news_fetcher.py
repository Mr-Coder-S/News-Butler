import requests
import json
from datetime import datetime, timedelta


live = datetime.now() - timedelta(days=7)
date = live.strftime('%Y-%m-%d')

def News():
    queries = ["tech", "world", "india", "science"]
    news_list = []

    for query in queries:
        nws_source = requests.get(f"https://newsapi.org/v2/everything?q={query}&from={date}&language=en&sortBy=publishedAt&apiKey='API'")
        
        news = json.loads(nws_source.text)
        Top_five = news["articles"][:5]
        for article in Top_five:
            news_list.append(article["title"])

    return news_list

