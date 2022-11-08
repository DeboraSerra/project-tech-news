from tech_news.database import search_news
from datetime import datetime

# , find_news, insert_or_update, get_collection


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    returned_news = search_news(query)
    return [(news["title"], news["url"]) for news in returned_news]


# Requisito 7
def search_by_date(date):
    try:
        parsed_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        returned_news = search_news({"timestamp": parsed_date})
        return [(news["title"], news["url"]) for news in returned_news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    returned_news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(news["title"], news["url"]) for news in returned_news]


# Requisito 9
def search_by_category(category):
    returned_news = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return [(news["title"], news["url"]) for news in returned_news]
