# src/metodos_atributos.py

def adicionar_metodo(classe, nome_metodo, funcao):
    setattr(classe, nome_metodo, funcao)

def adicionar_atributo(instancia, nome_atributo, valor):
    setattr(instancia, nome_atributo, valor)
