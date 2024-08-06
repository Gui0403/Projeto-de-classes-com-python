from classes import*
from function import*

def main_menu():
    print('''
0 - Encerrar Programa
1 - Criar Cachorro
2 - Criar Pessoa
3 - Consultar lista de Cachorros
4 - Consultar lista de Pessoas
5 - Excluir Cachorro
6 - Excluir Pessoa
7 - Editar Cachorro
8 - Editar Pessoa
''')
    
# def popUp_sair():
#     close = True
#     while close: 
#         sub_menu = input('Deseja Sair?\n1 - sim\n2 - não:')
#         if sub_menu == '1':
#             close = False
#         else:
#             close = True

        
def mostraInformacao_dog():
    nome = input('Digite o nome do Cachorro: ')
    for dog in lista_cachorros:
        if nome == dog.nome:
            print(f'Nome do Cachorro posição -->{dog.nome}')
            print(f'Raça do Cachorro -->{dog.raca}')
            print(f'Idade do Cachorro -->{dog.idade}')
            print(f'Peso do Cachorro -->{dog.peso}')
            print(f'Tamanho do Cachorro -->{dog.tamanho}')
        

def mostraInformacao_person():
    nome = input('Digite o nome da Pessoa: ')
    for pessoa in lista_pessoas:
        if nome == pessoa.nome:
            print(f'Nome da pessoa posição -->{pessoa.nome}')
            print(f'Idade da pessoa -->{pessoa.idade}')
            print(f'Peso da pessoa -->{pessoa.peso}')
            print(f'Altura da pessoa -->{pessoa.altura}')



def listar_dogs():
    num = 1
    for dog in lista_cachorros:
        print(f'Nome do Cachorro posição {num}°-->{dog.nome}')
        num += 1

def listar_person():
    num = 1
    for pessoa in lista_pessoas:
        print(f'Nome da Pessoa posição {num}°-->{pessoa.nome}')
        num += 1