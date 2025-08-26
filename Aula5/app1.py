#dicionario

usuario = {
    'nome':'gomes',
    'idade':'25'
}

print(type(usuario))
print(usuario)

#imprimir apenas o nome
print(f'nome: {usuario["nome"]}')
print(f'idade: {usuario["idade"]}')

usuarioss = ['gomes','nunes','maicol','jackson']
print(usuarioss)
print(f'nome: {usuarioss[-1]}')