import os
os.system("cls || clear")

class Livro: 
    def __init__(self, titulo: str, autor: str, numero_paginas: int, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"\nNome: {self.titulo} \nAutor: {self.autor} \nNúmero de páginas: {self.numero_paginas} \nPreço: {self.preco}"
    

# Instanciando classe.
primeiro_livro = Livro("Pai rico, pai pobre", "Robert Kiosaki", 376, 45)
segundo_livro = Livro("O poder do hábito", "Charles Duhigg", 516, 29.90)

print(primeiro_livro.exibir_dados())
print(segundo_livro.exibir_dados())