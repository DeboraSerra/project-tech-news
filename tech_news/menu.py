from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys


def function_0():
    amount = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(amount)


def function_1():
    title = input("Digite o título:")
    return search_by_title(title)


def function_2():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def function_3():
    tag = input("Digite a tag:")
    return search_by_tag(tag)


def function_4():
    category = input("Digite a categoria:")
    return search_by_category(category)


# Requisito 12
def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """
    )
    if int(option) < 5:
        eval(f"function_{option}")()
    elif option == "5":
        return top_5_news()
    elif option == "6":
        return top_5_categories()
    elif option == "7":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
