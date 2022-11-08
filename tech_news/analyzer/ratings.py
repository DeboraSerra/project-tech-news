from tech_news.database import find_news

# , find_news, insert_or_update, get_collection


# Requisito 10
def top_5_news():
    all_news = find_news()
    sorted_news = sorted(
        all_news, key=lambda news: news["comments_count"], reverse=True
    )
    return [
        (news["title"], news["url"])
        for news in sorted_news
        if sorted_news.index(news) < 5
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
