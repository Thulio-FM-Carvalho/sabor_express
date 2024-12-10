import os

restaurantes = [{'nome': 'Praca', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]


def exibir_nome_do_programa():
    """
    Exibe o nome estilizado do programa no terminal
    """

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)


def exibir_opcoes():
    """
    Exibe as opções estilizadas no terminal
    """

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def voltar_ao_menu_principal():
    """
    Solicita uma tecla no terminal para voltar ao menu principal
    Outputs:
    - Retorna ao menu principal
    """

    input('\nDigite uma tecla para voltar ao menu ')
    main()


def escolher_opcao():
    """
    Função responsável por tratar as opções de escolha do usuário no menu principal
    Outputs:
    - Executa a opção escolhida pelo usuário
    """

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def cadastrar_novo_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Lista os restaurantes no terminal
    Outputs:
    - Exibe a lista de restaurantes no terminal
    - Retorna ao menu principal
    """

    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Essa função é responsável por alternar o estado restaurante, como: ativo ou não ativo
    Outputs:
    - Exibe a mensagem no terminal informando o status de ativo ou não ativo
    """

    exibir_subtitulo('Alternar estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante[
                'ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    voltar_ao_menu_principal()


def finalizar_app():
    """
    Exibe uma mensagem de finalização do aplicativo
    """

    exibir_subtitulo('Finalizar aplicativo')


def opcao_invalida():
    """
    Exibe uma mensagem de opção inválida e volta ao menu principal
    Outputs:
    - Retorna ao menu principal
    """

    print('Opção Inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo estilizado na tela
    Inputs:
    - texto: str - o texto do subtitulo
    """

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def main():
    """
    Função principal que inicia o programa.
    """

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
