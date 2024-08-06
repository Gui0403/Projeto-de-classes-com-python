from classes import*

lista_cachorros = []
lista_pessoas = []


# Criar cachorro
def make_dog():
    nome = input('Digite o Nome do cachorro: ') 
    idade = input('Digite a Idade do cachorro: ')
    raca = input('Digite a Raca do cachorro: ')
    peso = input('Digite o Peso do cachorro: ')
    tamanho = input('Digite o Tamanho do cachorro: ')
    dog = Cachorro(nome, idade, raca, peso, tamanho)
    lista_cachorros.append(dog)

# Criar pessoa
def make_person():
    nome = input('Digite o Nome do Humano: ') 
    idade = input('Digite o Idade do Humano: ') 
    peso = input('Digite o Peso do Humano: ')
    altura = input('Digite a Altura do Humano: ')
    person = Humano(nome, idade, peso, altura)
    lista_pessoas.append(person)

# Exluir Cachorro    
def excluir_dog():
    name_dog = input('Digite o nome do Cachorro escolhido: ')
    for dog in lista_cachorros:
        if name_dog == dog.nome:
            lista_cachorros.remove(dog)
        print('Cachorro apagado com sucesso!')
    else:
        print('Cachorro não encontrada!')

# Exluir Pessoa    
def excluir_person():
    name_person = input('Digite o nome da Pessoa escolhida: ')
    for person in lista_pessoas:
        if name_person == person.nome:
            lista_pessoas.remove(person)
        print('Pessoa apagado com sucesso!')
    else:
        print('Pessoa não encontrada!')

# Mudar informações Cachorro   
def upload_dog():
    nome = input('Digite o nome do Cachorro que deseja: ')
    close = True
    while close:
        sair = input('\t\tDeseja sair da edição?\nSim -->(sim) \tNão -->(nao)')
        if sair.lower() == 'sim':
            close = False
            
        opcao = input('\tDigite a opção para alterar\n(escreva assim)-->[nome, idade, peso, tamanho, raca]')

        if opcao == 'nome':
            for dog in lista_cachorros:
                if nome == dog.nome:
                    new_nome = input('Digite o novo Nome: ')
                    dog.nome = new_nome   

        elif opcao == 'idade':
            for dog in lista_cachorros:
                if nome == dog.nome:
                    new_idade = input('Digite a nova Idade: ')
                    dog.idade = new_idade   
                        
        elif opcao == 'peso':
            for dog in lista_cachorros:
                if nome == dog.nome:
                    new_peso = input('Digite o novo Peso: ')
                    dog.peso = new_peso   
            
        elif opcao == 'tamanho':
            for dog in lista_cachorros:
                if nome == dog.nome:
                    new_tamanho = input('Digite o novo Tamanho: ')
                    dog.tamanho = new_tamanho  
                        
        elif opcao == 'raca':
            for dog in lista_cachorros:
                if nome == dog.nome:
                    new_raca = input('Digite a nova Raça: ')
                    dog.raca = new_raca  
        else: 
            print('Error, não identificado!') 

# Mudar informações Pessoa   
def upload_person():
    nome = input('Digite o nome da Pessoa que deseja: ')
    opcao = input('Digite a opção para alterar\n(escreva assim)-->[nome, idade, peso, altura]') 

    if opcao == 'nome':
        for person in lista_pessoas:
            if nome == person.nome:
                new_nome = input('Digite o novo Nome: ')
                person.nome = new_nome   

    elif opcao == 'idade':
        for person in lista_pessoas:
            if nome == person.nome:
                new_idade = input('Digite a nova Idade: ')
                person.idade = new_idade   
                    
    elif opcao == 'peso':
        for person in lista_pessoas:
            if nome == person.nome:
                new_peso = input('Digite o novo Peso: ')
                person.peso = new_peso   
        
    elif opcao == 'altura':
        for person in lista_pessoas:
            if nome == person.nome:
                new_altura = input('Digite o novo Altura: ')
                person.altura = new_altura  
    else: 
        print('Error, não identificado!') 