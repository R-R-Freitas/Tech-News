from datetime import datetime
from tech_news.database import search_news
from re import compile, IGNORECASE


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": compile(title, flags=IGNORECASE)})
    results = [(news["title"], news["url"]) for news in news_list]
    return results


# Requisito 7
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        news_list = search_news({"timestamp": formatted_date})
        results = [(news["title"], news["url"]) for news in news_list]
        return results
    except ValueError:
        raise (ValueError("Data inválida"))


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
