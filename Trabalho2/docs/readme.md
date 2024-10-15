# Projeto de Metaprogramação: Reflexão e Meta-Objetos em Python

## Descrição

Este projeto tem como objetivo demonstrar a utilização de **reflexão** e **meta-objetos** em Python por meio da criação programática de classes, atributos e métodos. A metaprogramação é uma técnica poderosa que permite que o código manipule outros códigos, modificando ou criando componentes de maneira dinâmica durante a execução do programa. Em Python, a metaprogramação é amplamente facilitada por recursos como reflexão, decoradores, metaclasses e funções de manipulação de classes e objetos.

## Relação com Reflexão e Meta-Objetos

### O que é Reflexão?

**Reflexão** é a capacidade de um programa de inspecionar e modificar sua própria estrutura e comportamento em tempo de execução. Em Python, a reflexão permite, por exemplo:

- **Inspecionar tipos**: Verificar dinamicamente os tipos de objetos, classes e métodos.
- **Manipular atributos e métodos**: Adicionar, remover ou modificar atributos e métodos de objetos e classes em tempo de execução.
- **Criar instâncias dinamicamente**: Criar classes ou instâncias com base em informações que só estão disponíveis durante a execução do programa.

Neste projeto, a reflexão é utilizada para:

- Criar novas classes dinamicamente a partir de parâmetros fornecidos pelo usuário.
- Adicionar ou remover atributos e métodos de instâncias e classes em tempo de execução.

### O que são Meta-Objetos?

**Meta-objetos** referem-se aos objetos que descrevem ou modificam a estrutura de outros objetos, como classes ou instâncias. Em Python, as metaclasses desempenham um papel importante na manipulação de meta-objetos, pois controlam a criação e o comportamento das classes.

Neste projeto, a ideia de meta-objetos está presente na capacidade de criar e modificar classes e métodos programaticamente, explorando como os objetos (incluindo classes, que também são objetos em Python) podem ser manipulados de maneira dinâmica.

## Funcionalidades do Projeto

O projeto demonstra as seguintes funcionalidades de metaprogramação:

1. **Criação Programática de Classes:**
   - Uma nova classe é criada dinamicamente com base nos parâmetros fornecidos.
   - A classe pode receber atributos iniciais, como `nome` e `idade`.

2. **Adição Dinâmica de Atributos:**
   - Atributos podem ser adicionados a instâncias de classes criadas dinamicamente.
   - Atributos como `idade`, `cidade`, etc., são adicionados à instância da classe.

3. **Adição Dinâmica de Métodos:**
   - Métodos podem ser criados e adicionados dinamicamente a classes e instâncias.
   - Métodos como `dizer_idade` e `dizer_cidade` são criados e podem ser chamados para exibir os atributos.

4. **Uso de Decoradores e Funções:**
   - Decoradores são utilizados para modificar classes, adicionando novos métodos ou atributos de forma declarativa.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

```
Trabalho2/
├── src/
│   ├── __init__.py
│   ├── main.py               # Arquivo principal que executa o código
│   ├── criacao_classe.py      # Contém a função para criação dinâmica de classes
│   ├── metodos_atributos.py   # Contém as funções para manipulação de métodos e atributos
└── tests/
    └── test_metaprogramacao.py  # Testes unitários para validar as funcionalidades do projeto
```

## Como Executar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Navegue até a pasta do projeto:

   ```bash
   cd Trabalho2
   ```

3. Execute o arquivo `main.py` para ver a criação dinâmica de uma classe, bem como a adição de atributos e métodos:

   ```bash
   python src/main.py
   ```

   O resultado será algo como:

   ```
   Idade: 30
   Cidade: São Paulo
   ```

## Exemplo de Uso

Aqui está um exemplo de como o projeto pode ser utilizado para criar uma classe `Pessoa` dinamicamente, adicionar atributos como `nome` e `idade`, e métodos como `dizer_nome` e `dizer_idade`:

```python
from criacao_classe import criar_classe
from metodos_atributos import adicionar_metodo, adicionar_atributo

# Criar classe dinamicamente
Pessoa = criar_classe('Pessoa', 'nome', 'João')

# Criar instância
pessoa = Pessoa()

# Adicionar atributos
adicionar_atributo(pessoa, 'idade', 30)

# Adicionar métodos
adicionar_metodo(Pessoa, 'dizer_idade', lambda self: print(f"Idade: {self.idade}"))

# Usar os métodos
pessoa.dizer_idade()  # Saída: Idade: 30
```

## Tecnologias Utilizadas

- **Python 3.x**
- **Metaprogramação (Reflexão e Meta-Objetos)**
- **Decoradores**
- **Funções Dinâmicas**
