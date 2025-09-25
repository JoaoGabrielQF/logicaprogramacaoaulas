import os

while True:
    try:
        ntxt = input('digite o texto \n')
        narq = input ('digite o nome do arquivo (sem extensao): ').strip()

        with open(fr'C:\GIT\Logica_De_Programacao_Aula\Aula4/{narq}.txt','w',encoding='utf-8') as f:
            f.write(ntxt)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{narq}.txt, gravado com sucesso')

        texto2 = input('digite um novo texto: \n')
        with open(fr'C:\GIT\Logica_De_Programacao_Aula\Aula4/{narq}.txt','a',encoding='utf-8') as f:
            f.write(texto2)
            print('gravado com sucesso')

            # ler os arquivos atualizados

            with open(fr'C:\GIT\Logica_De_Programacao_Aula\Aula4/{narq}.txt','r',encoding='utf-8') as f:
                arqaberto = f.read()
                print(arqaberto, '\n esse é o conteudo contido no arquivo alterado')
        break


        while True:
            prosseguir = input('Deseja abrir outro arquivo? (s/n) \n').lower().strip()
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('Opção Inválida')
                continue
                
        match prosseguir:
            case 's':
                continue
            case 'n':
                break

    except Exception as e:
        print(f'Não foi possível abrir o arquivo {e}')

SystemExit