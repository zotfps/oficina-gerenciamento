from modelos.clientes import salvar_clientes, remover_cliente
from modelos.carros import adicionar_carro, remover_carro

def menu():
 print("""
1 - Adicionar carro
2 - Listar carros
3 - Buscar carro
4 - Remover carro
      
5 - Adicionar Cliente
6 - Remover Cliente

9 - Sair""")

while True:
    menu()
    opcao_selecionada = input("Digite a opção: ")

    if opcao_selecionada == '1':
        adicionar_carro()
        input("\nPressione ENTER para voltar ao menu...")
    if opcao_selecionada == '2':
        pass
    if opcao_selecionada == '3':
        pass
    if opcao_selecionada == '4':
        remover_carro()
        input("\nPressione ENTER para voltar ao menu...")
    if opcao_selecionada == '5':
        salvar_clientes()
        input("\nPressione ENTER para voltar ao menu...")
    if opcao_selecionada == '6':
        remover_cliente()
        input("\nPressione ENTER para voltar ao menu...")
    if opcao_selecionada == '7':
        pass
    if opcao_selecionada == '8':
        pass
    if opcao_selecionada == '9':
        print("Saindo...")
        break