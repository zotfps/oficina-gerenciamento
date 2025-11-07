from modelos.dados import dados_veiculos

def adicionar_carro():
    try:
        Nome_Dono = input('Digite o nome do proprietario: ').upper()
        Veiculo = input('Digite o veiculo: ')
        Marca = input('Digite a Marca: ')
        Ano = input('Digite o ano do veiculo: ')
        Descricao = input('Oque foi feito?: ')

        carro ={
            "Proprietario": Nome_Dono,
            "Veiculo": Veiculo,
            "Marca": Marca,
            "Ano": Ano,
            "Serviço": Descricao
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
        print(f"{i} - Nome: {c['Proprietario']} | Veiculo: {c['Veiculo']} | Marca: {c['Marca']} | Ano: {c['Ano']}")

    try:
        escolha = int(input("\nDigite o número do cliente que deseja remover: "))
        if 1 <= escolha <= len(encontrados):
            veiculo_removido = encontrados[escolha - 1]
            dados_veiculos.remove(veiculo_removido)
            print(f"✅ Veiculo '{veiculo_removido['Veiculo']}' removido com sucesso!")
    except ValueError:
        print("⚠️ Digite um número válido.")

def listar_carros():
    veiculo = input("Digite o nome do veículo ou proprietário que deseja listar: ").upper()

    carros_encontrados = [
        carro for carro in dados_veiculos
        if veiculo in carro["Veiculo"].upper() or veiculo in carro["Proprietario"].upper()
    ]

    if not carros_encontrados:
        print("❌ Nenhum veículo encontrado com esse nome ou proprietário.")
        return

    print("\n🚗 Veículos encontrados:")
    for i, c in enumerate(carros_encontrados, start=1):
        print(f"{i} - Proprietário: {c['Proprietario']} | Veículo: {c['Veiculo']} | Marca: {c['Marca']} | Ano: {c['Ano']} | Descrição: {c['Serviço']}")
