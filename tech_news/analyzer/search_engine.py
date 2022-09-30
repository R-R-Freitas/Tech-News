from tech_news.database import search_news
from re import compile, IGNORECASE


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": compile(title, flags=IGNORECASE)})
    results = [(news["title"], news["url"]) for news in news_list]
    return(results)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
