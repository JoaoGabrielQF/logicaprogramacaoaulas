import os

while True:
    try:
        ntxt = input('digite o texto \n')
        narq = input ('digite o nome do arquivo (sem extensao): ').strip()

        with open(fr'C:\GIT\Logica_De_Programacao_Aula\Aula4/{narq}.txt','w',encoding='utf-8') as f:
            f.write(ntxt)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{narq}.txt, gravado com sucesso')

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