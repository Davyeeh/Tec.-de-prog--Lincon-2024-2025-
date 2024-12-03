from sisbanco import Conta, Banco

def terminal():
    sisbanco = Banco()

    while (True):
        print('SisBanco::Bem-vindo!')
        print('.::Opções::.')
        print('[0]-CriarConta')
        print('[1]-Creditar')
        print('[2]-Debitar')
        print('[3]-Trasnferir')
        print('[4]-Saldo')
        print('[5]-Sair')
        opcao = input('Digite: ')

        if opcao == 0:
            numero = input('Digite o número da conta: ') # Solicite o numero da conta a ser criada
            conta = Conta(numero) # instacie uma conta com esse número
            sisbanco.cadastrar(conta) # cadatre a conta no sisbanco

        elif opcao == 1:
            numero = input('Digite o número da conta: ') # Solicite o numero da conta alvo
            valor = float(input('Digite o valor a ser creditado: ')) #solicte uma conta com esse numero
            sisbanco.creditar(numero, valor) #cadastre a conta no sisbanco

        elif opcao == 2:
            numero = input('Digite o número da conta: ') #solicite o numero da conta alvo
            valor = float(input('Digite o valor a ser debitado: ')) # solicite o valor a ser debitado
            sisbanco.debitar(numero, valor) #realize a opercao de debito no sisbanco

        elif opcao == 3:
            origem = input('Digite o número da conta de origem: ') #solicite o numero da conta origem
            destino = input('Digite o número da conta de destino: ')  #solicite o numero da conta destino
            valor = float(input('Digite o valor a ser transferido: ')) #solicite o valor a ser transferido
            sisbanco.transferir(origem, destino, valor) #realize a operacao de transferencia no sisbanco

        elif opcao == 4:
            numero = input('Digite o número da conta: ') #solicite o numero da conta alvo
            saldo = sisbanco.saldo(numero) #realize a operacao de obtencao de saldo no sibanco
            print(f'Saldo: {saldo}')  # exiba o saldo na tela

        elif opcao == 5:
            print('SisBanco::Bye!')
            return

if __name__ == "__main__":
    terminal()
