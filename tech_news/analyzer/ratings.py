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
    news_list = find_news()
    categories = [news["category"] for news in news_list]
    categories_count = dict()
    for category in categories:
        if category in categories_count:
            categories_count[category] += 1
        else:
            categories_count[category] = 1
    rankings = sorted(
        categories_count,
        key=lambda category: (-categories_count.get(category), category),
    )
    return rankings[:5]
