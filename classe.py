class Animal:
    nome=str
    coracao:bool
    racional:bool
    def __init__(self,nome,coracao,racional):
        self.nome = nome
        self.coracao = coracao
        self.racional = racional

class Humano(Animal):
    tamanho:float
    nacionalidade=''
    cpf:int
    listaps=[]

    def __init__(self,tamanho=None,nome=None,nacionalidade=None,cpf=None):
        self.tamanho = tamanho
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.cpf = cpf
        self.coracao = True
        self.racional =True

    

class Cachorro(Animal):
    tamanho:float
    raca:str
    listach=[]

    def __init__(self,tamanho=None,raca=None,nome=None):
        self.tamanho = tamanho
        self.raca = raca
        self.nome = nome
        self.coracao=True
        self.racional=False

#pessoa = Humano(1.64,"luiz","Brasileiro","123.456.789-00")
#cao = Cachorro(0.58, "Pitbull", "Zeus")

#print(f"Cachorro:\nNome{cao.nome}\nTamanho:{cao.tamanho}\nRaça:{ cao.raca}\n\n\nPessoa:\nNome:{pessoa.nome}\nTamanho{pessoa.tamanho}\nNacionalidade{pessoa.nacionalidade}\nCPF:{pessoa.cpf}")