from modelos.dados import dados_clientes

def salvar_clientes():
    try:
        nome_cliente = input("Digite o nome do cliente: ")
        cpf_cliente = input("Digite o CPF do cliente: ")
        if nome_cliente == "" or cpf_cliente == "":
            print("Algum espaço ficou vazio!")
            return
        else:
            cliente = {
            "nome": nome_cliente.upper(),
            "cpf": cpf_cliente
        }
        dados_clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
    except:
        print("Ocorreu um erro!")

def remover_cliente():
    nome = input("Digite o nome do cliente para remover: ").upper()
    if nome == "":
        print("Invalido")
        return
    encontrados = [c for c in dados_clientes if c["nome"] == nome]

    if not encontrados:
        print("❌ Nenhum cliente encontrado com esse nome.")
    

    print("\nClientes encontrados:")
    for i, c in enumerate(encontrados, start=1):
        print(f"{i} - Nome: {c['nome']} | CPF: {c['cpf']}")

    try:
        escolha = int(input("\nDigite o número do cliente que deseja remover: "))
        if 1 <= escolha <= len(encontrados):
            cliente_removido = encontrados[escolha - 1]
            dados_clientes.remove(cliente_removido)
            print(f"✅ Cliente '{cliente_removido['nome']}' removido com sucesso!")
        else:
            print("⚠️ Opção inválida.")
    except ValueError:
        print("⚠️ Digite um número válido.")


