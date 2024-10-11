import unittest
from src.criacao_classe import criar_classe

class TestCriacaoClasse(unittest.TestCase):
    def test_classe_criada(self):
        Pessoa = criar_classe('Pessoa', 'nome', 'João')
        pessoa = Pessoa()
        self.assertEqual(pessoa.nome, 'João')

if __name__ == '__main__':
    unittest.main()
