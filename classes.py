class Animal:
    nome:str
    idade:int
    peso:float
    coracao:bool
    conciencia:bool
    racionalidade:bool
    bipede:bool
    sexo:bool


    def __init__(self, nome, coracao):
        self.nome = nome
        self.sexo:bool
        self.coracao:coracao


    def comer(self):
        print('Comendo!')

    def acasalar(self):
        print('Acasalando!')

class Cachorro(Animal):
    tamanho:float
    raca:str


    def __init__(self, nome, idade, peso, tamanho, raca):
        self.sexo = True
        self.coracao = True
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tamanho = tamanho
        self.raca = raca

    def latir(self):
        print( 'Latindo!')

class Humano(Animal):
    socializacao:bool

    def __init__(self, nome, idade, peso,altura):
        self.coracao = True
        self.socializacao = True
        self.conciencia = True
        self.racionalidade = True
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura