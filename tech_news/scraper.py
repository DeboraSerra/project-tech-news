import requests
from requests import ReadTimeout
from parsel import Selector
import time


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
    anchor_tags = selector.css('h2.entry-title a::attr(href)').getall()
    return anchor_tags


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
