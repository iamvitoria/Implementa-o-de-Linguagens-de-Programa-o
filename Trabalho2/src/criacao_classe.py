# src/criacao_classe.py

def criar_classe(nome_classe, nome_atributo, valor_atributo):
    atributos = {
        nome_atributo: valor_atributo
    }
    NovaClasse = type(nome_classe, (object,), atributos)
    return NovaClasse
