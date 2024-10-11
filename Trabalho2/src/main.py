from criacao_classe import criar_classe
from metodos_atributos import adicionar_metodo, adicionar_atributo

def main():
    # Criação da classe dinamicamente
    Pessoa = criar_classe('Pessoa', 'nome', 'João')

    # Instância de Pessoa
    pessoa = Pessoa()

    # Adicionar atributos dinamicamente
    adicionar_atributo(pessoa, 'idade', 30)
    adicionar_atributo(pessoa, 'cidade', 'São Paulo')

    # Adicionar métodos dinamicamente
    adicionar_metodo(Pessoa, 'dizer_idade', lambda self: print(f"Idade: {self.idade}"))
    adicionar_metodo(Pessoa, 'dizer_cidade', lambda self: print(f"Cidade: {self.cidade}"))

    # Usando os novos métodos
    pessoa.dizer_idade()
    pessoa.dizer_cidade()

if __name__ == "__main__":
        main()
