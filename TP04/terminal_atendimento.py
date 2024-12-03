from sisbanco import Conta, Banco, ContaPopanca, ContaEpecial


def terminal():
    sisbanco = Banco()

    while (True):
        print('SisBanco::Bem-vindo!')
        print('.::Opções::.')
        print('[0]-Criar uma conta')
        print('[1]-Creditar')
        print('[2]-Debitar')
        print('[3]-Trasnferir')
        print('[4]-Consultar saldo')
        print('[5]-Render juros')
        print('[6]-Render bônus')
        print('[7]-Alterar taxa de juros')
        print('[8]-Alterar taxa de imposto')
        print('[9]-Sair')
        opcao = int(input('Digite: '))

        if opcao == 0:
            # qual tipo de conta deve ser criada: S - simples | P - Poupanca | E - Especial
            tipo = str(
                input('Digite o tipo de conta: (S - Simples | P - Poupança | E - Especial)'))
            if tipo == 'S':
                # solicite o numero da conta a ser criada
                numero = int(input('Digite o número da conta: '))
                # instacie uma conta do tipo selecionado com esse numero
                conta = Conta(numero)
                # cadastre a conta no sisbanco
                sisbanco.cadastrar(conta)
            elif tipo == 'P':
                # solicite o numero da conta a ser criada
                numero = int(input('Digite o número da conta: '))
                # instacie uma conta do tipo selecionado com esse numero
                conta = ContaPopanca(numero)
                # cadastre a conta no sisbanco
                sisbanco.cadastrar(conta)
            elif tipo == 'E':
                # solicite o numero da conta a ser criada
                numero = int(input('Digite o número da conta: '))
                # instacie uma conta do tipo selecionado com esse numero
                conta = ContaEpecial(numero)
                # cadastre a conta no sisbanco
                sisbanco.cadastrar(conta)

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
            # solicite o numero da conta alvo
            numero = input('Digite o número da conta: ')
            # realize a operacao de correcao da poupanca no sisbanco
            sisbanco.render_juros(numero)

        elif opcao == 6:
            # solicite o numero da conta alvo
            numero = input('Digite o número da conta: ')
            # realize a operacao conversao/rendimento de bonus no sisbanco
            conta = sisbanco.procurar(numero)
            if isinstance(conta, ContaEpecial):
                conta.render_bonus()

        elif opcao == 7:
            # solicite a nova taxa de correcao da poupanca
            taxa = float(input('Digite a nova taxa de juros: '))
            # realize a operacao de alteracao da taxa no sisbancos
            sisbanco.set_taxa(taxa)

        elif opcao == 8:
            # solicite nova taxta dde imposto
            taxa = float(input('Digite a nova taxa de imposto: '))
            # realize a operacao de alteracao de taxa de imposto
            sisbanco.set_taxa(taxa)

        elif opcao == 9:
            print('SisBanco::Bye!')
            break


if __name__ == "__main__":
    terminal()
