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
    all_news = find_news()
    categories = {news["category"]: 0 for news in all_news}
    ordered_categories = sorted(categories, key=lambda category: category)
    categories = {key: 0 for key in ordered_categories}
    for news in all_news:
        categories[news["category"]] += 1
    sorted_categories = sorted(
        categories.items(), key=lambda category: (category[1]), reverse=True
    )
    return [
        category
        for category, qnt in sorted_categories
        if sorted_categories.index((category, qnt)) < 5
    ]
