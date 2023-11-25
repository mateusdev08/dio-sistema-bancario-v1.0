"""
Regras:

1- Criar um menu de opções para o usuário com as opções abaixo:
Deposito
Saque
Extrato
Sair

2- Depósito: Criar uma variável para armazenar os valores de cada depósito, e exibir cada um no extrato.

3- Saque: O usuário só poderá sacar 3 valores por dia e terá um limite de R$ 500,00 por dia. Se o cliente não possuir saldo exibir uma mensagem relatando o motivo da falha do saque. Os saques serão armazenados em uma variável e exibidos um a um no extrato.

4- Extrato: Exibir todos os saques e depositos e no final, mostrar o saldo atual. Os valores devem ser exibidos com R$
"""
import os

menu = """
====================================================
        SEJA BEM VINDO AO BANCO INOVATION
====================================================
[ 1 ] Deposito
[ 2 ] Saque
[ 3 ] Extrato
[ 0 ] Sair
====================================================
"""

deposito = []
saque = []
extrato_list = []
extrato_dict = {}
saldo = 0.00
limite_saque = 500.00
numero_saques = 3

while True:
    print(menu, end='')
    print(f'Seu saldo atual é de R${saldo:.2f}')
    print('====================================================')

    while True:
        opcao_menu = str(input('Informe o número da opção acima: ')).strip()
        if opcao_menu > '3' or not opcao_menu.isnumeric() or opcao_menu == '':
            print('Digite uma opção válida.')

        else:
            break

###### Bloco para sair do sistema
    if opcao_menu == '0':
        os.system('cls')
        mensagem_despedida = 'O BANCO INOVATION AGRADECE A SUA PREFERÊNCIA. VOTLE SEMPRE!!!'
        print('=' * len(mensagem_despedida))
        print(mensagem_despedida)
        print('=' * len(mensagem_despedida))
        break

###### Bloco responsável pelo processo de depósito
    elif opcao_menu == '1':
        os.system('cls')
        while True:
            depositar = float(input('Informe o valor a ser depositado R$ '))
            deposito.append(depositar)
            extrato_dict.clear()
            extrato_dict['Depósito'] = depositar
            extrato_list.append(extrato_dict.copy())
            saldo += depositar

            continuar = str(input('Deseja realizar outro depósito [S/N]? ')).strip().upper()[0]
            if continuar == 'N':
                os.system('cls')
                break
            os.system('cls')
    
###### Bloco responsável pelo processo de saque
    elif opcao_menu == '2':
        os.system('cls')
        while True:
            if saldo == 0:
                print('Você não possui saldo para saque, faça um depósito e tente novamente.')
                break

            if limite_saque == 0 or numero_saques == 0:
                os.system('cls')
                print('Limite atingido. Tente novamente amanhã.')
                break

            resumo_limite = f'''=== Limites Diários ===
Quantidade de saques: {numero_saques}
Limite diário restante: R${limite_saque:.2f}
Saldo atual: R${saldo:.2f}'''
            
            print(resumo_limite)
            print('-' * 50)

            sacar = float(input('Informe o valor do saque R$ '))

            if saldo >= sacar and sacar + sum(saque) <= 500:
                saque.append(sacar)
                extrato_dict.clear()
                extrato_dict['Saque'] = sacar * -1
                extrato_list.append(extrato_dict.copy())
                numero_saques -= 1
                limite_saque -= sacar
                saldo -= sacar

            else:
                print(f'O valor solicitado ultrapassa o seu limmite de valor diário. Você possui {numero_saques} saques e R${limite_saque:.2f} de limite para sacar.')

            # if limite_saque == 0 or numero_saques == 0:
            #     os.system('cls')
            #     print('Limite atingido. Tente novamente amanhã.')
            #     break

            continuar = str(input('Deseja realizar outro saque [S/N]? ')).strip().upper()[0]
            if continuar == 'N':
                os.system('cls')
                break
            os.system('cls')

###### Bloco responsável pelo extrato
    elif opcao_menu == '3':
        os.system('cls')
        extrato_saldo = 0
        while True:
            print(f"{'Operação'}\t\t{'Valor'}")
            print('-' * 35)
            for item in extrato_list:
                for operacao, valor in item.items():
                    if operacao == 'Depósito':
                        print(f"{operacao}\t\tR${valor:.2f}")
                    
                    else:
                        print(f"{operacao}\t\t\tR${valor:.2f}")

                for operacao, valor in item.items():
                    extrato_saldo += valor
            print(f"{'Saldo'}\t\t\tR${extrato_saldo:.2f}")

            print('-' * 35)
            continuar = str(input('Digite qualquer coisa para sair: ')).strip()
            if continuar:
                os.system('cls')
                break
