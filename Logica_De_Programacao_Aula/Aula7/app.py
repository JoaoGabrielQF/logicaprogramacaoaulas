import random
import string

def gerar(comprimento=12, incluir_maiusculo=True, incluir_minusculo=True, incluir_numeros=True, incluir_caracter=True):

    caracteres= ''
    if incluir_minusculo:
        caracteres += string.ascii_lowercase
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracter:
        caracteres += string.punctuation
    if not caracteres:
        return ValueError('Deve ter pelo menos um tipo de cada caractere.')
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'senha: {senha}')
    return senha

def main():
    print('Gerador de Senhas fortes')
    comprimento = int(input('Digite o comprimento da senha (padrão é 12): ') or 12)
    incluir_maiuscula = input('Incluir maiuscula (s/n padrão sim)').lower() != 'n'
    incluir_minuscula = input('Incluir minuscula (s/n padrao sim)').lower() != 'n'
    incluir_numeros = input('Incluir numeros (s/n padrão sim)').lower() != 'n'
    incluir_caracteresp = input('Incluir caracteres especiais (s/n padrão sim)').lower() != 'n'

    senha = gerar(comprimento, incluir_minuscula, incluir_maiuscula, incluir_numeros, incluir_caracteresp)

    print(f'A senha gerada foi: {senha}')

    with open('senhas.txt', 'a') as s:
        s.write(f'\n{senha}')
