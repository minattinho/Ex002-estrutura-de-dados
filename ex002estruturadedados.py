class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def exibirDetalhes(self):
        status = "disponível" if self.disponivel else "indisponível"
        print(f"título: {self.titulo}, autor: {self.autor}, status: {status}")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []

    def emprestarLivro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livrosEmprestados.append(livro)
            print(f"{self.nome} emprestou o livro '{livro.titulo}'.")
        else:
            print(f"o livro '{livro.titulo}' não está disponível.")

    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            livro.disponivel = True
            self.livrosEmprestados.remove(livro)
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
        else:
            print(f"{self.nome} não tem o livro '{livro.titulo}' emprestado.")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def exibirLivrosDisponiveis(self):
        print(f"Livros disponíveis na biblioteca {self.nome}:")
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        if disponiveis:
            for livro in disponiveis:
                livro.exibirDetalhes()
        else:
            print("Nenhum livro disponível no momento.")


livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")
usuario = Usuario("João")
biblioteca = Biblioteca("Biblioteca Central")

biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)