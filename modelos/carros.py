from modelos.dados import dados_veiculos

def adicionar_carro():
    try:
        Veiculo = input('Digite o veiculo: ')
        Marca = input('Digite o veiculo: ')
        Ano = input('Digite o ano do veiculo: ')

        carro ={
            "nome": Veiculo,
            "cpf": Marca,
            "ano": Ano
        }

        dados_veiculos.append(carro)
        print("Carro cadastrado com sucesso!")
    except:
        print("Ocorreu um erro!")