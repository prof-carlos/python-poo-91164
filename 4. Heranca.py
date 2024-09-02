from abc import ABC, abstractmethod
import os

os.system("cls || clear") # Limpa terminal.

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        # Acréscimo de 20%
        BONIFICACAO = 1.2 
        salario_final = self.salario * BONIFICACAO
        return salario_final


class Motoboy(Funcionario): 
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        # Acréscimo de 10%
        BONIFICACAO = 1.1 
        salario_final = self.salario * BONIFICACAO
        return salario_final


# Instanciar classes.

# funcionario1 = Funcionario("Jose", 33, 1000.0)
# print(f"Nome: {funcionario1.nome}")

gerente1 = Gerente("Marta", 22, 1000.0)
print(f"Nome: {gerente1.nome}")
print(f"Salário: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Jose", 33, 1000.0, "4654621")
print(f"Nome: {motoboy1.nome}")
print(f"Salário: {motoboy1.calcular_salario()}")

