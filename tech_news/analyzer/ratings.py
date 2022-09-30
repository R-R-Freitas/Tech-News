from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    # solução baseada em uma das apresentadas no artigo seguinte:
    # http://stygianvision.net/updates/python-sort-list-object-dictionary-multiple-key/
    top_5 = sorted(
        news_list,
        key=lambda news: (-news["comments_count"], news["title"].lower()),
    )[:5]
    results = [(news["title"], news["url"]) for news in top_5]
    return results


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
