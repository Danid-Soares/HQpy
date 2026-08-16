from loja import Loja

def main():

    loja = Loja()

    while True:

        print("1. Cadastrar quadrinho")
        print("2. Listar Quadrinhos")
        print("3. Apagar Quadrinho")
        print("4. Buscar Quadrinho")
        print("5. Contar por Editora")
        print("6. Vender Quadrinho")
        print("7. exibir Balanço")
        print("8. Aplicar desconto geral")
        print("9. Atualizar preço de quadrinho")
        print("10. Listagem de Raridades")
        print("11. Alerta de Estoque Crítico")
        print("12. Processar Eventos de Fidelidade")
        print("13. Exibir Histórico de Vendas")
        print("14. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            loja.cadastrar_quadrinho()
        elif opcao == "2":
            loja.listar_quadrinhos()
        elif opcao == "3":
            loja.apagar_quadrinho()
        elif opcao == "4":
            loja.buscar_quadrinho()
        elif opcao == "5":
            loja.contar_por_editora()
        elif opcao == "6":
            loja.vender_quadrinho()
        elif opcao == "7":
            loja.exibir_balanco()
        elif opcao == "8":
            loja.aplicar_desconto_geral()
        elif opcao == "9":
            loja.atualizar_preco_por_titulo()
        elif opcao == "10":
            loja.listar_raridades()
        elif opcao == "11":
            loja.alerta_estoque_critico()
        elif opcao == "12":
            loja.processar_eventos_fidelidade()
        elif opcao == "13":
            loja.exibir_historico_vendas()
        elif opcao == "14":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
menu = main()
