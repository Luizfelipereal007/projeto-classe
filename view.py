from classe import*

def menu():
    print("1.-Criar pessoa.\n")
    print("2.-Criar cachorro\n")
    print("3.-Ver lista pessoa\n")
    print("4.-ver lista cachorro\n")
    print("5.-Excluir pessoa")###
    print("6.-Excluir cachorro")###
    print("7.-Sair\n")


def listar_ps():
    num=1
    for pessoa in Humano.listaps:
        print(f"{num}.-{pessoa.nome}\n")
        num+1

def listar_c():
    num=1
    for cao in Cachorro.listach:
        print(f"{num}{cao.nome}\n")
        num+1

#def info_ps():
#    num=input("numero da pessoa:")
#    if num==            
#
#    for pessoa in Humano.listaps