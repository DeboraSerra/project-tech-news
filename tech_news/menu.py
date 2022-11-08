from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


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
    if option == "0":
        amount = input("Digite quantas notícias serão buscadas:")
        return get_tech_news(amount)
    elif option == "1":
        title = input("Digite o título:")
        return search_by_title(title)
    elif option == "2":
        date = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(date)
    elif option == "3":
        tag = input("Digite a tag:")
        return search_by_tag(tag)
    elif option == "4":
        category = input('Digite a categoria:')
        return search_by_category(category)
    elif option == '5':
        return top_5_news()
    elif option == '6':
        return top_5_categories()
    elif option == '7':
        return
    else:
        print('Opção inválida')
        return
