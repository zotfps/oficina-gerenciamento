from modelos.dados import dados_veiculos

def adicionar_carro():
    try:
        Nome_Dono = input('Digite o nome do proprietario: ').upper()
        Veiculo = input('Digite o veiculo: ')
        Marca = input('Digite a Marca: ')
        Ano = input('Digite o ano do veiculo: ')

        carro ={
            "Proprietario": Nome_Dono,
            "Veiculo": Veiculo,
            "Marca": Marca,
            "Ano": Ano
        }

        dados_veiculos.append(carro)
        print("Carro cadastrado com sucesso!")
    except:
        print("Ocorreu um erro!")

def remover_carro():
    nome = input("Digite o nome do proprietario para remover: ").upper()
    encontrados = [c for c in dados_veiculos if c["Proprietario"] == nome]

    if not encontrados:
        print("❌ Nenhum cliente encontrado com esse nome.")
    

    print("\nClientes encontrados:")
    for i, c in enumerate(encontrados, start=1):
        print(f"{i} - Nome: {c['Proprietario']} | Veiculo: {c['Veiculo']} | Marca: {c['Marca']} | Marca: {c['Ano']}")

    try:
        escolha = int(input("\nDigite o número do cliente que deseja remover: "))
        if 1 <= escolha <= len(encontrados):
            veiculo_removido = encontrados[escolha - 1]
            dados_veiculos.remove(veiculo_removido)
            print(f"✅ Veiculo '{veiculo_removido['Veiculo']}' removido com sucesso!")
    except ValueError:
        print("⚠️ Digite um número válido.")