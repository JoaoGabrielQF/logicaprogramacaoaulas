#atividade de python, criar programa bancário com funçoes
import os
import json

limpar = lambda:os.system('cls' if os.name == 'nt' else 'clear')

def criar():
    limpar()
    global senha 
    global saldo
    print('Insira seu: ')
    print('Nome Completo \nCPF \nData de Nascimento \nRenda Anual')
    nm_cmp = input('Insira seu Nome completo: ')
    cad_pf = int(input('Insira seu CPF: '))
    dt_nasc = input('Insira sua Data de Nascimento da seguinte maneira(DD/MM/AAAA): ')
    ren_ano = float(input('Insira sua Renda Anual: '))
    senha = input('Defina uma Senha: ')
    global saldo
    saldo = 0    
    print('Conta criada com sucesso')

def menu():
    global opcao
    print(f'{50*'-'}Menu Principal{50*'-'}')
    print('1 - Criar Conta')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Exibir Dados da Conta')
    print('5 - Encerrar conta')
    print('0 - Sair do programa')
    opcao = input('Digite a opcao desejada: ')
# Variáveis globais para senha e saldo
senha = None
saldo = 0

#looping do menu
while True:
    #menu
    match menu():
        case 1:
           criar(senha)
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case 0:
            ...
        case _:
            ...