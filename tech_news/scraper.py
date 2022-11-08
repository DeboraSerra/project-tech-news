import requests
from requests import ReadTimeout
from parsel import Selector
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        result = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if result.status_code == 200:
            return result.text
        else:
            return None
    except ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    anchor_tags = selector.css("h2.entry-title a::attr(href)").getall()
    return anchor_tags


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next::attr(href)").get()
    if next_page:
        return next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    article = Selector(text=html_content)
    title = article.css("div.entry-header-inner h1.entry-title::text").getall()
    title = "".join(title).strip()
    timestamp = article.css("ul.post-meta li.meta-date::text").get()
    writer = article.css(
        "ul.post-meta li.meta-author span.author a::text"
    ).get()
    comments_count = article.css(
        "div.post-comments h5.title-block::text"
    ).re_first(r"\d")
    summary = article.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()
    summary = "".join(summary).strip()
    tags = article.css("section.post-tags li a[rel=tag]::text").getall()
    category = article.css("div.meta-category a span.label::text").get()
    url = article.css("link[rel=canonical]::attr(href)").get()
    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count or 0,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return news


# Requisito 5
def get_tech_news(amount):
    content = fetch("https://blog.betrybe.com/")
    links = scrape_novidades(content)
    while len(links) < amount:
        next_page = scrape_next_page_link(content)
        content = fetch(next_page)
        new_links = scrape_novidades(content)
        for new_link in new_links:
            links.append(new_link)
    news = []
    for index in range(amount):
        news_request = fetch(links[index])
        news.append(scrape_noticia(news_request))
    create_news(news)
    return news
