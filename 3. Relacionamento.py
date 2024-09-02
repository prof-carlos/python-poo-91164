import os

os.system("cls || clear") # Limpar o terminal.

class Endereco: 
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    # def exibir_endereco(self) -> str:
        # return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
    
    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
    

class Aluno:
    # Construtor.
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        # Atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"

# Instanciar classe.
aluno1 = Aluno("Marta", 22, Endereco("Rua A", 22))

print(aluno1)
