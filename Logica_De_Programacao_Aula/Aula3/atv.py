#comeco do codigo, opcoes do menu
print(50*'-','lista',50*'-')
print('1 - adicionar nome')
print('2 - remover nome')
print('3 - pesquisar nome')
print('4 - alterar nome')
print('5 - mostrar nomes')
print('6 - sair')

#lista de nomes
nomes = []
#loop de opcoes
while True:
    opc = int(input('digite a opcao desejada: '))

    if opc == 1:
        nomeins = input('digite o nome a ser inserido: ')
        nomes.append(nomeins)
        print(f'nome {nomeins} adicionado com sucesso!')
    if opc == 2:
        nomerem = input ('digite o nome a ser removido: ')
        if nomerem in nomes:
            try:
                nomes.remove(nomerem)
                print(f'nome {nomerem} removido com sucesso!')
            except:
                 print(f'nome {nomerem} nao encontrado na lista!')
    if opc == 3:
        nomepes = input('digite o nome a ser pesquisado: ')
        if nomepes in nomes:
         print(f'nome {nomepes} encontrado na lista!')
        else:
         print(f'nome {nomepes} nao encontrado na lista!')
    if opc == 4:
        nomealt = input('digite o nome que deseja alterar: ')
        nomes[nomes.index(nomealt)] = input(' digite o novo nome: ')
    if opc == 5:
        for nome in nomes: 
            print(nome)
    if opc == 6:
        break