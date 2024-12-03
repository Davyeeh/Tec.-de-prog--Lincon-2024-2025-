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
        opcao = int(input('Digite: '))

        if opcao == 0:
            # Solicite o numero da conta a ser criada
            numero = input('Digite o número da conta: ')
            conta = Conta(numero)  # instacie uma conta com esse número
            sisbanco.cadastrar(conta)  # cadatre a conta no sisbanco

        elif opcao == 1:
            # Solicite o numero da conta alvo
            numero = input('Digite o número da conta: ')
            # solicte uma conta com esse numero
            valor = float(input('Digite o valor a ser creditado: '))
            sisbanco.creditar(numero, valor)  # cadastre a conta no sisbanco

        elif opcao == 2:
            # solicite o numero da conta alvo
            numero = input('Digite o número da conta: ')
            # solicite o valor a ser debitado
            valor = float(input('Digite o valor a ser debitado: '))
            # realize a opercao de debito no sisbanco
            sisbanco.debitar(numero, valor)

        elif opcao == 3:
            # solicite o numero da conta origem
            origem = input('Digite o número da conta de origem: ')
            # solicite o numero da conta destino
            destino = input('Digite o número da conta de destino: ')
            # solicite o valor a ser transferido
            valor = float(input('Digite o valor a ser transferido: '))
            # realize a operacao de transferencia no sisbanco
            sisbanco.transferir(origem, destino, valor)

        elif opcao == 4:
            # solicite o numero da conta alvo
            numero = input('Digite o número da conta: ')
            # realize a operacao de obtencao de saldo no sibanco
            saldo = sisbanco.saldo(numero)
            print(f'Saldo: {saldo}')  # exiba o saldo na tela

        elif opcao == 5:
            print('SisBanco::Bye!')
            return


if __name__ == "__main__":
    terminal()
