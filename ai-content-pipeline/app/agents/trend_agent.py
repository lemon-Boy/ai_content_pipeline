from app.services.news_service import get_trending_news


class TrendAgent:

    def run(self, keyword="AI"):

        articles = get_trending_news(keyword)

        trends = []

        for article in articles:
            trends.append({
                "title": article["title"],
                "description": article.get("description", ""),
                "url": article.get("url")
            })

        return trends