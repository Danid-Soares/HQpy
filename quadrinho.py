class Quadrinho:
    def __init__(self, titulo, autor, editora, ano, preco):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.preco = preco

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")
        print(f"Ano: {self.ano}")
        print(f"Preço: {self.preco}")