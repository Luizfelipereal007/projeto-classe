from classe import*
from view import*

def create_person():
    tamanho=input("tamanho:")
    nome=input("nome:")
    nacionalidade=input("nacionalidade:")
    cpf=input("cpf:")
    pessoa=Humano(tamanho,nome,nacionalidade,cpf)
    Humano.listaps.append(pessoa)

def create_dog():
    tamanho=input("tamanho:")
    raca=input("raca:")
    nome=input("nome:")
    cao=Cachorro(tamanho,raca,nome)
    Cachorro.listach.append(cao)

while True:
    menu()
    op = input("Escolha uma opção: ")
    if op=='1' :
        create_person()
    if op== '2' :
        create_dog()
    if op== '3' :
        listar_ps()
    if op== '4' :
        listar_c()
    if op== '5' :
        ()
    if op== '6' :
        ()
    elif op= '7' :
        break