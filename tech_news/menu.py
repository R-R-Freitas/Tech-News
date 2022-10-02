import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories

sub_options = {
    "0": "Digite quantas notícias serão buscadas:",
    "1": "Digite o título:",
    "2": "Digite a data no formato aaaa-mm-dd:",
    "3": "Digite a tag:",
    "4": "Digite a categoria:",
}
options = {
    "0": get_tech_news,
    "1": search_by_title,
    "2": search_by_date,
    "3": search_by_tag,
    "4": search_by_category,
    "5": top_5_news,
    "6": top_5_categories,
    "7": "Encerrando script",
}


def menu_functions(option):
    if int(option) == 0:
        print(options[option](int(input(sub_options[option]))))
    if int(option) in range(1, 5):
        print(options[option](input(sub_options[option])))
    if int(option) in range(5, 8):
        print(options[option])


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
 7 - Sair."""
    )
    try:
        if int(option) not in range(0, 8):
            sys.stderr.write("Opção inválida\n")
        else:
            menu_functions(option)
    except ValueError:
        sys.stderr.write("Opção inválida\n")
