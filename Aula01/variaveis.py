'''
Variáveis usadas para o programa.
Elas não precisam ser exatamanete denominadas no python.
O codigo vai indentificar as variaveis e escrever o texto
usando-as
'''
print(50*"-","dados",50*"-")
nome = "Silas"
idade = 87
altura = 1.63
dt = "10/02/1800"
ativo = True

'''
O código mostra os dados inseridos nas variáveis, escrevendo uma frase alterável
'''
print("olá! meu nome é",nome,", eu tenho",idade," anos e eu nasci no dia",dt,", foi um prazer te conhecer!")

'''
O código mostra o tipo das variáveis e os reais nomes delas
ao contrário do que foi ensinado no portugol, os nomes são esses
'''
print("o tipo da variável nome é:",type(nome))
print("o tipo da variável idade é",type(idade))
print("o tipo da variável altura é",type(altura))
print("o tipo da variável data de nascimento é",type(dt))
print("o tipo da variável ativo é",type(ativo))

'''Operadores para cálculos no programa
num1 e num2 são variáveis para os números
divi_inteira é a divisão inteira dos números, isso é,
sem virgula, apenas o número inteiro'''

print()
print(50*"-","operadores",50*"-")
num1 = 25
num2 = 20

soma = num1 + num2
divi = num1 / num2
divi_inteira = num1 // num2
mult = num1 * num2
expo = num1 ** num2
sub = num1 - num2

print("a soma de",num1,"e",num2,"é:",soma)
print("a divisao de",num1,"por",num2,"é:",divi)
print("a divisao inteira de",num1,"por",num2,"é",divi_inteira)
print("a multiplicacao de",num1,"por",num2,"é",mult)
print("a exponenciacao de",num1,"elevado a",num2,"é",expo)
print("a subtracao de",num1,"por",num2,"é",sub)

'''Operadores de comparação para verificar se os números são iguais ou diferentes
a diferença entre = e == é que = atribui valores a variável, logo se fosse apenas num = num 2, num1 estaria tendo o valor de num2
== verifica se os valores são iguais
!= verifica se os valores são diferentes
usadas as mesmas variáveis do códiog anterior
'''
print()
print(50*"-","comparação",50*"-")

num1 > num2
num1 < num2
num1 == num2
num1 != num2
num1 >= num2
num1 <= num2

ano = 2025
print("o ano atual é",ano)
ano += 1 #aumenta o ano em 1
print("o ano seguinte é",ano)
ano -= 1 #diminui o ano em 1
print("o ano seguinte menos 1 é",ano)

'''OBS: Operadores logicos:
    AND, OR, NOT
'''

'''Entrada de dados
a entrada de dados é feita pela função input
é como o leia do portugol, mas melhor, o sistema não vai continuar até que o usuário digite algo no input
'''
print ()
print(50*"-","entrada de dados",50*"-")

nome_usuario = input("digite seu nome:")
print("seja bem vindo",nome_usuario,"ao python!")

'''Calculadora simples, ela funciona como os numeros anteriores mas agora com o input de numeros
int obriga a variavel a ser um numero inteiro
alem do int, tem o float, que sao os numeros reais, com virgula
no python não usamos virgula, e sim ponto
'''

print()
print(50*"-","calculadora",50*"-")

numero1 = int(input("digite o primeiro numero:"))
numero2 = int(input("digite o segundo numero:"))

soma = numero1 + numero2
divi = numero1 / numero2
divi_inteira = numero1 // numero2
mult = numero1 * numero2
expo = numero1 ** numero2
sub = numero1 - numero2

print("a soma de",numero1,"e",numero2,"é:",soma)
print("a divisao de",numero1,"por",numero2,"é:",divi)
print("a divisao inteira de",numero1,"por",numero2,"é",divi_inteira)
print("a multiplicacao de",numero1,"por",numero2,"é",mult)
print("a exponenciacao de",numero1,"elevado a",numero2,"é",expo)
print("a subtracao de",numero1,"por",numero2,"é",sub)

'''TIPOS DE DADOS
int: numeros inteiros
float: numeros reais
str: texto ou conjunto de caracteres
bool: valores de True e False
'''

print()
print(50*"-","Convertendo tipos de dados",50*"-")

ano_nascimento = input("digite o ano do seu nascimento:")
print("antes de converter:",type(ano_nascimento))
ano_nascimento = int(ano_nascimento) #aqui o ano_nascimento é convertido de str para int
print("depois de converter:",type(ano_nascimento))

'''OBS quando uma variavel nao precisa de um input especifico, principalmente em calculos,
não é necessario fazer o calculo para depois usar o print com o resultado, é possivel usar o proprio print
como o calculo para mostrar o resultado, economizando linhas de código
'''
n1 = 10
n2 = 20

print("a soma de",n1,"e,",n2,"é:",n1+n2,"e n1 é",type(n1),"e n2 é",type(n2),"e n2 acaba de ser convertido para float",float(n2),"olhe",type(float(n2)))

saudacao = input("digite seu nome:")
cpf = input("digite seu cpf:")
telefone = input("digite seu telefone:")

print(50*'-','dados pessoais',50*'-')
print('nome:',saudacao)
print('cpf:',cpf)
print('telefone:',telefone)
print(50*'-','fim do programa',50*'-')