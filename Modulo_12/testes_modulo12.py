import unittest


# 1. Código da Calculadora (com divisão por zero)
class Calculadora:

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError()
        return a / b


# 2. Testes Automatizados
class Testes(unittest.TestCase):

    def test_tudo(self):
        calc = Calculadora()

        # Atividade 1 e 2: Testa soma e divisão
        self.assertEqual(calc.somar(2, 3), 5)
        self.assertEqual(calc.dividir(10, 2), 5)

        # Atividade 3: Testa erro de divisão por zero
        with self.assertRaises(ValueError):
            calc.dividir(5, 0)


if __name__ == "__main__":
    unittest.main()
