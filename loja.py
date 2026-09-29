from typing import Self

from quadrinho import Quadrinho
import quadrinho
import sqlite3


class Loja:
    

    def __init__(self):
        self.caixa = 0.0
        self.conn = sqlite3.connect("loja.db")
        self.cursor = self.conn.cursor()
        self.historicos_venda = []
        self.cupons_gerados = 0

    def cadastrar_quadrinho(self):
        titulo = input("Digite o título do quadrinho: ")
        autor = input("Digite o autor do quadrinho: ")      
        editora = input("Digite a editora do quadrinho: ")
        ano = input("Digite o ano do quadrinho: ")
        preco = int(input("Digite o preço do quadrinho: "))

        self.cursor.execute("""
        INSERT INTO quadrinhos (titulo, autor, editora, ano, preco)
        VALUES (?,?,?,?,?)
 """, (titulo, autor, editora, ano, preco))

        self.conn.commit()

    def listar_quadrinhos(self):
        self.cursor.execute("SELECT * FROM quadrinhos")
        dados = self.cursor.fetchall()

        for q in dados:
            print(q)

    def buscar_quadrinho(self):
        nome_busca = input("Digite o título: ")

        self.cursor.execute(
            "SELECT * FROM quadrinho WHERE titulo LIKE ?",
            ('%' + nome_busca + '%',)
        )

        resultado = self.cursor.fetchall()

        if len(resultado) == 0:
            print("Não encontrado")
        else:
            for q in resultado:
                print(q)

    def contar_por_editora(self):
        nome_editora = input("Digite o nome da editora: ")

        self.cursor.execute(
            "SELECT COUNT(*) FROM quadrinhos WHERE editora = ?",
            (nome_editora,)
        )

        resultado = self.cursor. fetchone()

        quantidade = resultado[0]

        if quantidade > 0:
            print(f"Você possui {quantidade} quadrinho(s) da editora {nome_editora}.")
        else:
            print("Nenhum quadrinho dessa editora encontrado. ")

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
        id = int(input("ID do quadrinho: "))
        titulo_quadrinho = input("Digite o título do quadrinho: ")

        for quadrinho in self.conta:
            if titulo_quadrinho.lower() == quadrinho.titulo.lower():
                novo_preco = float(input("Digite um novo preço: "))
                self.cursor.execute("""
                UPDATE quadrinhos
                SET preco = ?
                WHERE id = ?
                """, (novo_preco, id))
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
        id = int(input("Digite o ID do quadrinho: "))

        self.cursor.execute("SELECT * FROM quadrinho WHERE ID = ?", (id,))
        resultado = self.cursor.fetchone()

        if resultado is None:
            print("Não existe!")
            return

        confirmar = input("Tem certeza que deseja apagar? (s/n): ")

        if confirmar.lower() == "s":
            self.cursor.execute("DELETE FROM quadrinho WHERE id = ?", (id,))
            self.conn.commit()
            print("Apagado com sucesso!")

