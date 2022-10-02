import sys


# Requisito 12
def analyzer_menu():
    options = {
        "0": input("Digite quantas notícias serão buscadas:"),
        "1": input("Digite o título:"),
        "2": input("Digite a data no formato aaaa-mm-dd:"),
        "3": input("Digite a tag:"),
        "4": input("Digite a categoria:"),
    }
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")
    try:
        if int(option) not in range(0, 7):
            sys.stderr.write("Opção inválida")
        sub_option = options[option]
        return sub_option
    # elif option == 5:
    #     option == input("Digite o título:")
    # elif option == 6:
    #     option == input("Digite o título:")
    # elif option == 7:
    #     option == input("Digite o título:")
    except ValueError:
        sys.stderr.write("Opção inválida")
