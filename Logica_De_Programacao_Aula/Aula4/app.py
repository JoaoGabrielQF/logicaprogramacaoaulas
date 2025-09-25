while True:
    try:
        #entrada de dados
        etanol = float(input('digite o preço do etanol: ')).replace(',','.')
        gasolina = float(input('digite o preço da gasolina: ')).replace(',','.')
        calculo = (etanol/gasolina)*100
        resultado = 'gasolina' if calculo > 70 else etanol

        #resposta de calculo
        print(f'nesse momentoo ideal é abastecer com {resultado}')
        print(f'decisao com base no resultado : {calculo:.2f}%.')

        opcao = input('deseja repitir o calculo? (s/n)').lower().strip()
        match opcao:
            case 's':
                continue
            case 'n':
                break
            case _:
                print(f'opcao invalida')
    except Exception as e:
        print(f'nao foi possivel fazer a operacao')
        continue