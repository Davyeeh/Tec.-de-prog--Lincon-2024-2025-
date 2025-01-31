import unittest
from sisbanco_bugs import Conta, ContaPoupanca, ContaEspecial, ContaImposto, Banco


class TesteConta(unittest.TestCase): # Teste da classe conta

    def teste_debitar(self): # Teste de debitar
        conta = Conta("123-X")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5.0) # OK
        conta.creditar(10)
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), 0.0) # OK

class TesteContaPupanca(unittest.TestCase): # teste de conta pupança

    def teste_render_juros(self): # teste de render juros
        conta = ContaPoupanca("132-X")
        conta.creditar(10) 
        conta.render_juros(5)
        self.assertEqual(conta.get_saldo(), 60)

class TesteContaEspecial(unittest.TestCase):

    def teste_creditar(self):
        conta = ContaEspecial("132-X")
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10)


    def teste_render_bonus(self):
        conta = ContaEspecial("321-X")
        conta.creditar(10)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 10.1)

class TesteContaImposto(unittest.TestCase):
    
    def teste_debitar(self):
        conta = ContaImposto("312-X")
        conta.creditar(20)
        conta.debitar(10)
        self.assertEqual(conta.get_saldo(), 9.99)

    def teste_get_taxa(self):
        conta = ContaImposto("213-X")
        conta.get_taxa()
        self.assertEqual(conta.get_taxa(), 0.001)

    def teste_set_taxa(self):
        conta = ContaImposto("231-X")
        conta.set_taxa(0.002)
        self.assertEqual(conta.get_taxa(), 0.002)

class TesteBanco(unittest.TestCase):
    def set(self):
        self.banco = Banco()
        self.banco.cadastrar(self.conta1)
        self.banco.cadastrar(self.conta2)
        self.banco.cadastrar(self.conta3)

    def teste_procurar(self):
        self.banco = Banco()
        self.conta1 = Conta("789-X")
        self.banco.cadastrar(self.conta1)

        conta = self.banco.procurar("789-X")
        self.assertEqual(conta.get_numero(), "789-X")

        conta_inexistente = self.banco.procurar("999-X")
        self.assertIsNone(conta_inexistente, "Erro! Conta inxistente")

    def teste_creditar_banco(self):
        self.banco = Banco()
        self.conta1 = Conta("456-X")
        self.banco.cadastrar(self.conta1)

        self.banco.creditar("456-X",10)
        self.assertEqual(self.conta1.get_saldo(), 10)

    def teste_debitar_banco(self):
        self.banco = Banco()
        self.conta1 = Conta("465-X")
        self.banco.cadastrar(self.conta1)
        
        self.banco.creditar("465-X", 10)
        self.banco.debitar("465-X", 5)
        self.assertEqual(self.conta1.get_saldo(), 5)

    def teste_transferir(self):
        self.banco = Banco()
        self.conta1 = Conta("546-X")
        self.banco.cadastrar(self.conta1)
        self.conta2 = ContaPoupanca("564-X")
        self.banco.cadastrar(self.conta2)

        self.banco.creditar("546-X", 10)
        self.banco.creditar("564-X", 5)
        self.banco.transferir("546-X", "564-X", 5)
        self.assertEqual(self.conta1.get_saldo(), 5)
        self.assertEqual(self.conta2.get_saldo(), 10)

    def teste_render_juros_banco(self):
        self.banco = Banco()
        self.conta2 = ContaPoupanca("645-X")
        self.banco.cadastrar(self.conta2)

        self.banco.creditar("645-X", 10)
        self.banco.render_juros("645-X")
        self.assertEqual(self.conta2.get_saldo(), 10.01)

    def teste_render_bonus_banco(self):
        self.banco = Banco()
        self.conta3 = ContaEspecial("654-X")
        self.banco.cadastrar(self.conta3)

        self.banco.creditar("654-X", 10)
        self.banco.render_bonus("654-X")
        self.assertEqual(self.conta3.get_saldo(), 10.1)



if __name__ == '__main__':
    unittest.main()
