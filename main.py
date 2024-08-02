from classes import* 
from Views import*

# Criar cachorro
def make_dog():
    nome = input('Digite o Nome do cachorro: ') 
    idade = input('Digite a Idade do cachorro: ')
    raca = input('Digite a Raca do cachorro: ')
    peso = input('Digite o Peso do cachorro: ')
    tamanho = input('Digite o Tamanho do cachorro: ')
    dog = Cachorro(nome, idade, raca, peso, tamanho)
    Cachorro.lista_cachorros.append(dog)


# Criar pessoa
def make_person():
    nome = input('Digite o Nome do Humano: ') 
    idade = input('Digite o Idade do Humano: ') 
    peso = input('Digite o Peso do Humano: ')
    altura = input('Digite a Altura do Humano: ')
    person = Humano(nome, idade, peso, altura)
    Humano.lista_pessoas.append(person)

# Atualizar informações
def upload_dog():
    nome = input('Digite o nome do Cachorro que deseja: ')
    opcao = input('Digite a opção para alterar\n(escreva assim)-->[nome, idade, peso, tamanho, raca]') 

    if opcao == 'nome':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_nome = input('Digite o novo nome: ')
                dog.nome = new_nome   

    elif opcao == 'idade':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_idade = input('Digite a nova idade: ')
                dog.idade = new_idade   
                    
    elif opcao == 'peso':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_peso = input('Digite o novo peso: ')
                dog.peso = new_peso   
        
    elif opcao == 'tamanho':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_tamanho = input('Digite o novo tamanho: ')
                dog.tamanho = new_tamanho  
                    
    elif opcao == 'raca':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_raca = input('Digite a nova raça: ')
                dog.raca = new_raca   
                
def upload_person():
    nome = input('Digite o nome do Cachorro que deseja: ')
    opcao = input('Digite a opção para alterar\n(escreva assim)-->[nome, idade, peso, tamanho, raca]') 

    if opcao == 'nome':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_nome = input('Digite o novo nome: ')
                dog.nome = new_nome   

    elif opcao == 'idade':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_idade = input('Digite a nova idade: ')
                dog.idade = new_idade   
                    
    elif opcao == 'peso':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_peso = input('Digite o novo peso: ')
                dog.peso = new_peso   
        
    elif opcao == 'tamanho':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_tamanho = input('Digite o novo tamanho: ')
                dog.tamanho = new_tamanho  
                    
    elif opcao == 'raca':
        for dog in Cachorro.lista_cachorros:
            if nome == dog.nome:
                new_raca = input('Digite a nova raça: ')
                dog.raca = new_raca   


close = True
while close:
    main_menu()
    option = input('Digite uma opção: ')

    if option == '1':
        make_dog()

    elif option == '2':
        make_person()
    
    elif option == '3':
        listar_dogs()
        sub_menu = input('Quer ver as informações do seu cachorro: ')
        if sub_menu.capitalize == 'sim':
            mostraInformacao_dog()


    elif option == '4':
        listar_person()
        sub_menu = input('Quer ver as informações da pessoa: ')
        if sub_menu.capitalize == 'sim':
            mostraInformacao_dog()

    elif option == '7':
        listar_dogs()
        sub_menu = input('Quer ver as informações do cachorro:\n1 - sim 2 - não')
        if sub_menu == '1':
            mostraInformacao_dog()
        upload_dog()