import json
import os

usuarios = []
novoarq = ''

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
    usuario = {}
    print('1 - Cadastrar novo usuario')
    print('2 - Salvar arquivo JSON')
    print('3 - Fazer leitura do JSON')
    print('4 - Sair do sistema')

    opcao = input('Informe a opção desejada: ')
    limpar ()

    match opcao:
        case '1':
            usuario['nome'] = input('informe o nome: ').strip().title()
            usuario['idade'] = input('informe a idade: ')
            usuario['email'] = input('informe o email: ').strip().lower()

            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso')
            continue
        case '2':
            narq = input('Informe o nome do arquivo: ').strip().lower()
            with open(fr'C:\GIT\Logica_De_Programacao_Aula\Aula5\{narq}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios,f,ensure_ascii=False,indent=4)
            limpar()
            print('Arquivo salvo com sucesso')
            continue
        case '3':
            if not narq:
                narq = input('Digite o nome do arquivo').strip().lower()
            with open(fr'C:\GIT\Logica_De_Programacao_Aula\Aula5\{narq}.json','r',encoding='utf-8') as f:
                dados = json.load(f)
            print(f'{'-'*50}USUARIOS{'-'*50}')
            for usuario in dados:
                for chave in usuario:
                    print(fr'{chave.capitalize()}: {usuario.get(chave)}')
                print('-'*100)
            continue
        case '4':
            print('Saindo do sistema...')
            break