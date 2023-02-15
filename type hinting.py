import random

def descrizione(nome:str,eta:int) -> str:
    return f"{nome} ha {eta} anni"
descrizione("Pippo",23)

def numero_casuale() -> int:
    return random.randint(0,99)
numero_casuale()

def descrizione_eta_casuale(nome:str) -> str:
    eta=numero_casuale()
    return descrizione(nome,eta)
print(descrizione_eta_casuale("Pippo"))

def descrizione_casuale() -> str:
    nomi=["Mattia","Anna","Francesco"]
    nome=random.choice(nomi)
    eta=numero_casuale()
    return descrizione(nome,eta)
print(descrizione_casuale())

