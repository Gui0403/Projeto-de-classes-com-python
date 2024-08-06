from classes import* 
from Views import*
from function import*

close = True
while close:

    main_menu()
    option = input('Digite uma opção: ')
# 0 - Encerrar Programa
    if option == '0':
        close = False

# 1 - Criar Cachorro
    elif option == '1':
        make_dog()

# 2 - Criar Pessoa
    elif option == '2':
        make_person()
    
# 3 - Consultar lista de Cachorros
    elif option == '3':
        if len(lista_cachorros) > 0:
            listar_dogs()
            sub_menu = input('Quer ver as informações do seu cachorro: (sim ou nao)')
            if sub_menu.lower() == 'sim':
                mostraInformacao_dog()
        else:
            print('Lista está vazia!')

# 4 - Consultar lista de Pessoas
    elif option == '4':
        if len(lista_pessoas) > 0:
            listar_person()
            sub_menu = input('Quer ver as informações da pessoa: (sim ou nao)')
            if sub_menu.lower() == 'sim':
                mostraInformacao_person()
        else:
            print('Lista está vazia!')

# 5 - Excluir Cachorro
    elif option == '5':
        excluir_dog()
    
# 6 - Excluir Pessoa
    elif option == '6':
        excluir_person()

# 7 - Editar Cachorro
    elif option == '7':
        upload_dog()

# 8 - Editar Pessoa
    elif option == '8':
        upload_person()