import os

while True:
    try:
        # usuario informa o nome do arquivo 
        arquivo = input('digite o nome do arquivo (sem extensao): ').strip().lower()

        # abre o arquivo
        with open(f'{arquivo}.txt', 'r', encoding='utf-8') as f:
            arquivoaberto = f.read()
        os.system('cls' if os.name == 'nt' else 'clear')

        # mostrar os dados do arquivo
        print(arquivoaberto)

        while True:
            prosseguir = input('Deseja abrir outro arquivo? (s/n)').lower().strip()
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