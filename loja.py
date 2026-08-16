from typing import Self

from quadrinho import Quadrinho
import quadrinho

class Loja:
    

    def __init__(self):
        self.caixa = 0.0
        self.conta = [
            Quadrinho("Batman: O Cavaleiro das Trevas", "Frank Miller", "Panini", "1986", 25),
            Quadrinho("Watchmen", "Alan Moore", "DC Comics", "1986", 30),
            Quadrinho("Spider-Man: Blue", "Jeph Loeb", "Marvel", "2002", 80),
            Quadrinho("Mulher Maravilha: Sangue", "Brian Azzarello", "Panini", "2012", 40)
        ]
        self.conta.append(Quadrinho("Watchmen - Edição Definitiva", "Alan Moore", "1986", 190.00))
        self.conta.append(Quadrinho("Sandman: Edição Absoluta Vol. 1", "Neil Gaiman", "1989", 350.00))
        self.conta.append(Quadrinho("Saga - Capa Dura Vol. 1", "Brian K. Vaughan", "2012", 140.00))
        self.conta.append(Quadrinho("Akira - Coleção Completa Box", "Katsuhiro Otomo", "1982", 480.00))

        # Quadrinhos acima de R$ 1.000 (Raridades)
        self.conta.append(Quadrinho("Action Comics #1", "Jerry Siegel", "1938", 1250.00))
        self.conta.append(Quadrinho("Marvel Comics #1", "Stan Lee", "1939", 1100.00))
        self.conta.append(Quadrinho("Batman #1 - Edição Autografada", "Bob Kane", "1940", 2500.00))
        self.historicos_venda = []
        self.cupons_gerados = 0

    def cadastrar_quadrinho(self):
        titulo = input("Digite o título do quadrinho: ")
        autor = input("Digite o autor do quadrinho: ")      
        editora = input("Digite a editora do quadrinho: ")
        ano = input("Digite o ano do quadrinho: ")
        preco = int(input("Digite o preço do quadrinho: "))
        quadrinho = Quadrinho(titulo, autor, editora, ano, preco)
        self.conta.append(quadrinho)

    def listar_quadrinhos(self):
        if len(self.conta) == 0:
            print("Nenhum quadrinho cadastrado")
        else:
            print("--------Quadrinhos cadastrados:--------")
            for quadrinho in self.conta:
                quadrinho.exibir_dados()
            print("--------------------------------------")

    def buscar_quadrinho(self):
        print("\n-------- Buscar Quadrinho --------")
        nome_busca = input("Digite o título do quadrinho a ser buscado: ")
        encontrou = False
       
        for quadrinho in self.conta:
            if nome_busca.lower() in quadrinho.titulo.lower():
                print("\n🔍 Quadrinho Encontrado:")
                quadrinho.exibir_dados()
                encontrou = True

        if not encontrou:
            print("\n❌ Quadrinho não encontrado.")

    def contar_por_editora(self):
        nome_editora = input("Digite o nome da editora: ")
        contador = 0

        for quadrinho in self.conta:
            if nome_editora.lower() == quadrinho.editora.lower():
                print("Nome da editora encontrada")
                contador += 1
                quadrinho.exibir_dados()
                print("-" * 20)

        if contador > 0:
            print(f"Você possui {contador} quadrinho(s) da editora {nome_editora}.")
        else:
            print("Nenhum quadrinho dessa editora encontrado.")

    def vender_quadrinho(self):
        print("\n-------- Venda de Quadrinho --------")
        if len(self.conta) == 0:
            print("Nenhum quadrinho no estoque para vender.")
            return

        nome_quadrinho = input("Digite o título exato do quadrinho a ser vendido: ")
        
        for quadrinho in self.conta:
            # Usamos == para garantir que estamos vendendo o gibi certo!
            if nome_quadrinho.lower() == quadrinho.titulo.lower():
                # 1. Soma o preço do quadrinho ao caixa global da loja
                self.caixa += quadrinho.preco 
                
                # 2. Remove o quadrinho do estoque (lista)
                self.conta.remove(quadrinho) 
                
                print(f"\n💰 Venda realizada! R$ {quadrinho.preco:.2f} adicionados ao caixa.")
                print(f"💵 Saldo atual do caixa da loja: R$ {self.caixa:.2f}")
                return # Encerra o método porque o produto já foi vendido e removido
                
        print("❌ Esse quadrinho não foi encontrado no estoque.")

    def exibir_balanco(self):
        estoque = 0

        if len(self.conta) == 0:
            print("Nenhum quadrinho no estoque ainda")
        else:
            print("------- Balanço da Loja -------")
            print(f"Saldo total em Caixa: {self.caixa}")

        for quadrinho in self.conta:
            estoque += 1

        print("--------------------------------------------")

        if estoque > 0:
            print(f"Total de quadrinhos em Estoque: {estoque}")
        else:
            print("Não tem quadrinhos no estoque")

    def aplicar_desconto_geral(self):
        for quadrinho in self.conta:
            quadrinho.preco = quadrinho.preco * 0.90
        print("Preços atualizados com sucesso")

    def atualizar_preco_por_titulo(self):
        titulo_quadrinho = input("Digite o título do quadrinho: ")

        for quadrinho in self.conta:
            if titulo_quadrinho.lower() == quadrinho.titulo.lower():
                novo_preco = float(input("Digite um novo preço: "))
                quadrinho.preco = novo_preco
                print("Preço alterado com sucesso!")
                return  # sai da função quando encontra

        # esse print fica FORA do for
        print("Quadrinho não encontrado")

    def listar_raridades(self):
        print("-------- Listagem de Raridade —-----")
        for quadrinho in self.conta:
            if int(quadrinho.ano) < 2000:
                quadrinho.exibir_dados()

    def alerta_estoque_critico(self):
        print("------- Alerta de estoque -------")
        nome_autor = input("Digite o nome de um autor: ")
        estoque = 0

        for quadrinho in self.conta:
            if nome_autor.lower() == quadrinho.autor.lower():
                estoque += 1

        if estoque == 0:
            print(f"Nenhum quadrinho encontrado para o autor {nome_autor}.")
        elif estoque <= 1:
            print(f"Alerta: Estoque crítico para o autor {nome_autor}! Resta apenas {estoque} unidade(s).")
        else:
            print(f"Estoque seguro para o autor {nome_autor} ({estoque} unidades)")

    def exibir_historico(self):
        print("-------- Historico de Vendas -------")
        if len(self.historicos_venda) == 0:
            print("Nenhum quadrinho no historico de vendas")
        else:
            for quadrinho in self.historicos_venda:
                print(quadrinho)
        print("---------------------------------------------")

    def processar_eventos_fidelidade(self):
        print("------- Evento de Fidelidade -------") 
        nome_clientes = input("Digite o nome do cliente: ")
        compras_clientes = 0

        for quadrinhos in self.historicos_venda:   
            if nome_clientes.lower() in quadrinhos.lower():
                compras_clientes += 1

        if len(self.historicos_venda) == 0:
            print(f"Bem-vindo à loja, {nome_clientes}! Como esta é sua primeira interação, você ganhou um Quadrinho de Brinde do evento!")
        elif compras_clientes >= 1 and compras_clientes <= 3:
            print(f"Parabéns {nome_clientes}, você ganhou um cupom de 15%!")
            self.cupons_gerados += 1
        else:
            print(f"Parabéns {nome_clientes}, você é um Cliente VIP! Receba um cupom de 30%!")
            self.cupons_gerados += 1

        print("------ Relatorio de final de evento ------")
        print(f"Total de cupons emitidos pela loja hoje: {self.cupons_gerados}") 
        print("--------------------------------------------------")


    def apagar_quadrinho(self):
        if len(self.conta) == 0:
            print("Nenhum quadrinho cadastrado")
        else:
            titulo = input("Digite o título do quadrinho a ser apagado: ")
            for quadrinho in self.conta:
                if quadrinho.titulo.lower() == titulo.lower():
                    self.conta.remove(quadrinho)
                    print("Quadrinho apagado com sucesso!")
                    return
            print("Quadrinho não encontrado.")

