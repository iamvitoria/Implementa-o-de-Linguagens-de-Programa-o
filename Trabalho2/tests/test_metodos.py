import unittest
from src.metodos_atributos import adicionar_metodo, adicionar_atributo

class TestMetodosAtributos(unittest.TestCase):
    def test_adicionar_atributo(self):
        class Pessoa:
            pass

        pessoa = Pessoa()
        adicionar_atributo(pessoa, 'idade', 30)
        self.assertEqual(pessoa.idade, 30)

if __name__ == '__main__':
    unittest.main()
