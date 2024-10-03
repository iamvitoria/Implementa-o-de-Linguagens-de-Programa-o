# Função para criar o método get_nome
def get_nome(self):
    return self.nome

# Função para criar o método set_nome
def set_nome(self, nome):
    self.nome = nome

# Criando a classe 'MinhaClasse' dinamicamente com o tipo `type`
MinhaClasse = type(
    'MinhaClasse',            # Nome da classe
    (object,),                # Classe base (herdando de 'object')
    {
        'get_nome': get_nome, # Adicionando o método 'get_nome'
        'set_nome': set_nome  # Adicionando o método 'set_nome'
    }
)

# Instanciando a classe dinamicamente criada
obj = MinhaClasse()

# Definindo o valor do atributo 'nome' usando o método set_nome
obj.set_nome("Vitória")

# Obtendo o valor do atributo 'nome' usando o método get_nome
print("Nome:", obj.get_nome())
