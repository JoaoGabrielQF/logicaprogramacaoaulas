# importacao
import json
try:
    arq = input('digite o nome do arquivo: ').strip().lower()
    with open (f'{arq}.json','r', encoding='utf-8') as f:
        dados = json.load(f)
    
    print(f'{'-'*50} dados {50*'-'}')
    for dado in dados:
        for chave in dado:
            print(f'{chave.capitalize} : {dado.get(chave)}')
        print(100*'-')
except Exception as e:
    print(f'nao foi possivel ler o arquivo {e}')