'''problema: crie um sistema que calcule o indice de massa corporal (IMC) do usuário, mostre o valor
do IMC na tela, retorne se o usuário estiver no peso ideal ou precisa emagrecer ou engordar.
Utilize a tabela do IMC para definir os valores
imc = peso / (altura²)
18,5 ou menos: muito abaixo do peso
de 18,5 a 24,9: peso normal
de 25 a 29,9: sobrepeso
de 30 a 34,9: obesidade grau 1
de 35 a 39,9: obesidade grau 2
de 40 ou mais: obesidade grau 3
'''

print(50*'-','calcculadora IMC',50*'-')
altura = float(input('digite a sua altura: ').replace(',','.'))
peso = float(input('digite seu peso: ').replace(',','.'))

imc = peso / (altura ** 2)
print()
print(f'seu IMC é: {imc:.2f}')

if imc <= 18.5:
    print('você está muito abaixo do peso')
elif 18.5 < imc <= 24.9:
    print('você está no peso ideal')
elif 25 <= imc <= 29.9:
    print('você está com sobrepeso')
elif 30 <= imc <= 34.9:
    print('você está com obesidade grau 1')
elif 35 <= imc <= 39.9:
    print('você está com obesidade grau 2')
else:
    print('você está com obesidade grau 3')

'''
problema 2: Um elevador de carga possui capacidade para 200kg. Crie um programa que receba
 do usuário seu peso e o peso de carga e verifica se aa carga está autorizada a usar 
o elevador de carga ou não.
'''

print(50*'-','elevador de carga',50*'-')
peso_user = float(input('digite seu peso: '))
carga = float(input('digite o peso da carga: '))
restante = 200 - (carga + peso_user)
if restante >= 0:
    print('carga autorizada a usar o elevador, restam',restante,'kg de capacidade')
else:
    print('carga não autorizada, peso maximo atingido')

'''
LAÇOS
laços são estruturas de repetição, ou seja, executam um bloco de código várias vezes
existem 3 tipos de laços: while, continue'''
num = 10
while num >= 0:
    print(num)
    num -= 1 

while True:
    #menu principal
    print(50*'-','sistema console 2º ds',50*'-')
    print('1 - calculadora IMC')
    print('2 - maioridade')
    print('3 - calculadora simples')
    print('4 - dados pessoais')
    print('5 - arvore de natal')
    print('0 - sair')
    opcao = input('digite a opcao desejada: ')
    if opcao == '1':
        altura = float(input('digite a sua altura: ').replace(',','.'))
        peso = float(input('digite seu peso: ').replace(',','.'))

        imc = peso / (altura ** 2)
        print()
        print(f'seu IMC é: {imc:.2f}')

        if imc <= 18.5:
            print('você está muito abaixo do peso')
        elif 18.5 < imc <= 24.9:
             print('você está no peso ideal')
        elif 25 <= imc <= 29.9:
            print('você está com sobrepeso')
        elif 30 <= imc <= 34.9:
            print('você está com obesidade grau 1')
        elif 35 <= imc <= 39.9:
            print('você está com obesidade grau 2')
        else:
            print('você está com obesidade grau 3')
    if opcao == '2':
        ano = 2025
        nasc = input('digite seu ano de nascimento:')
        idade = ano - nasc
        if idade >= 18:
            print('voce é maior de idade')
        else:
            print('voce é menor de idsade')
    if opcao == '3':
        while True:
            print(50*'-','calculadora simples',50*'-')
            print('1 - soma')
            print('2 - subtração')
            print('3 - multiplicação')
            print('4 - divisão')
            op_calc = input('digite a operacao desejada: ')
            n1 = float(input('digite o primeiro numero: ').replace(',', '.'))
            n2 = float(input('digite o segundo numero: ').replace(',', '.'))
            if op_calc == '1':
                print(f'a soma de {n1} e {n2} é: {n1 + n2}')
            elif op_calc == '2':
                print(f'a subtração de {n1} e {n2} é: {n1 - n2}')
            elif op_calc == '3':
                print(f'a multiplicação de {n1} e {n2} é: {n1 * n2}')
            elif op_calc == '4':
                print(f'a divisão de {n1} e {n2} é: {n1 / n2}')
            print('deseja calcular novamente?')
            continuar = input('(s/n)').lower()
            if continuar != 's':
                print('saindo da calculadora simples...')
                break
            elif continuar != 'n':
                continue
    if opcao == '4':
        nome = input("digite seu nome: ")
        cpf = input("digite seu cpf: ")
        telefone = input("digite seu telefone: ")
        dt = input("digite sua data de nascimento :")
        print(100*'-')
        print(f'nome: {nome}')
        print(f'cpf: {cpf}')
        print(f'telefone: {telefone}')
        print(f'data de nascimento: {dt}')
    if opcao == '5':
        ...
    if opcao == '0':
        print('saindo do sistema...')
        break

