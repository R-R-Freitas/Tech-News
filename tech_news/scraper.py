from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news_urls = []
    news_urls.extend(selector.css(".entry-title a::attr(href)").getall())
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(".next::attr(href)").get()
    return next_page_url


# Requisito 4
def format_text_end(text):
    while True:
        if text.endswith("\xa0") or text.endswith(" "):
            text = text[:-1]
        else:
            break
    return(text)


def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.xpath("//link[@rel='canonical']/@href").get()
    title = selector.css(".entry-title::text").get()
    title = format_text_end(title)
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css(".post-comments h5::text").get()
    if comments_count is not None:
        comments_count = int(comments_count.split()[0])
    else:
        comments_count = 0
    summary = selector.xpath(
        "string((//div[@class='entry-content']/p)[1])"
    ).get()
    summary = format_text_end(summary)
    tags = selector.xpath(
        "//a[@rel='tag']/text()"
    ).getall()
    category = selector.css(".label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
