from abc import ABC, abstractmethod
import os

os.system("cls || clear") # Limpa o terminal.

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNumero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
                )


class Funcionario(ABC): 
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"\nSalário: {self.salario_final()}" 
                f"\nEndereço: {self.endereco}"
                )


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return 2000.0

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
            )


class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return 5000.0

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}"
            )

# Instanciando classes.
print("\n=== Dados do engenheiro ===")
engenheiro_1 = Engenheiro("Jose", "46546", "jose@gmail.com", "4632", 
                          Endereco("Rua A", "33", "Bloco A", "406546", "Salvador"))
print(engenheiro_1)

print("\n=== Dados do médico === ")
medico_1 = Engenheiro("Marta", "46546", "marta@gmail.com", "4632", 
                          Endereco("Rua B", "22", "Bloco B", "406546", "Salvador"))
print(medico_1)