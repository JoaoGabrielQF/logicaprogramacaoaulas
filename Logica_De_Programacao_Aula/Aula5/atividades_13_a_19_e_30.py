import os
print('\n OLA USUARIO')
input('aperte ENTER para avançar')
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
limpar()

# questao 13: Solicite a altura e a largura de um retângulo e exiba o perímetro
print(f'{'-'*50} 13 {50*'-'}')
alt = int(input('insira a altura do seu retângulo: ').replace(',','.'))
lar = int(input('insira a largura do seu retângulo: ').replace(',','.'))
per = (alt * 2) + (2 * lar)
print(f'o perímetro do seu retângulo é {per}')
input('\nAperte ENTER para avançar')
limpar()

# questao 14: Peça um número e exiba o quadrado dele
print(f'{50*'-'} 14 {50*'-'}')
n = int(input('diga seu número: '))
print(f'o quadrado do seu número é {n**2}')
input('\nAperte ENTER para avançar')
limpar()

# questao 15: Peça três números e exiba o produto deles
print(f'{50*'-'} 15 {50*'-'}')
n1 = int(input('insira seu primeiro número: '))
n2 = int(input('insira seu segundo número: '))
n3 = int(input('insira seu terceiro número: '))
print(f'o produto de {n1}, {n2}, {n3} é {n1*n2*n3}')
input('\nAperte ENTER para avançar')
limpar()

# questao 16: Peça o valor de um produto e exiba o valor após aplicar um desconto de 10%
print(f'{50*'-'} 16 {50*'-'}')
n = float(input('insira o valor: '))
dscnt = (10/100) * n
print(f'com o desconto, seu valor fica {n - dscnt}')
input('\nAperte ENTER para avançar')
limpar()

# questao 17: Solicite um valor principal, a taxa de juros e o tempo, e exiba o valor dos juros simples
print(f'{50*'-'} 17 {50*'-'}')
n = float(input('insira o valor: '))
tx = int(input('insira a taxa de juros: '))
ju = (tx/100)
tp = (int(input('insira o tempo do juros (meses): ')))
print(f'o valor do juros é {n * ju * tp}, no total o resultado é {(n * ju * tp) + n}')
input('\nAperte ENTER para avançar')
limpar()

# questao 18: Peça dois números e verifique se são diferentes
print(f'{50*'-'} 18 {50*'-'}')
n = input('insira o primeiro número: ')
n1 = input('insira o segundo número: ')
if n == n1:
    print(f'{n} e {n1} são números iguais!')
else:
    print(f'os números {n} e {n1} são diferentes.')
input('\nAperte ENTER para avançar')
limpar()

# questao 19: Peça três números e verifique
# se o primeiro é maior que o segundo e menor que o terceiro.
print(f'{50*'-'} 19 {50*'-'}')
n = int(input('insira o primeiro número: '))
n1 = int(input('insira o segundo número: '))
n2 = int(input('insira o terceiro número: '))
if n > n1 and n < n2:
    print(f'{n} é maior que {n1} e menor que {n2}.')
elif n > n1 and n > n2:
    print(f'{n} é maior que {n1} e {n2}.')
elif n < n1 and n > n2:
    print(f'{n} é menor que {n1} e maior que {n2}.')
else:
    print(f'{n} é menor que {n1} e {n2}.')
input('\nAperte ENTER para avançar')
limpar()

#questao 30: corrigir o codigo dado
print(f'{50*'-'} 30 {50*'-'}')

x = int(input("Digite o numero da tabuda: "))
for num in range(1, 11):
    print(f"{x} x {num} = {int(x) * num}")

print('codigo corrigido :')
print('x = int(input("Digite o numero da tabuda: "))')
print('for num in range(1, 11):')
print('    print(f"{x} x {num} = {int(x) * num}")')

print('Obrigado por testar o codigo ;)')
input('Aperte enter para fechar o codigo')
limpar()
SystemExit()