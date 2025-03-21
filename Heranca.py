# Exercício: Sistema de Funcionários
# Objetivo:
# Criar um sistema com classes base e herança para gerenciar diferentes tipos de funcionários.

# Classes:
# Classe Funcionario (classe base):
# Atributos: nome, salario
# Métodos:
# exibir_dados(): Mostra o nome e o salário do funcionário.
# aumentar_salario(valor): Aumenta o salário de acordo com o valor passado como parâmetro.

# Classe Gerente (classe filha):
# Atributos adicionais: departamento
# Método:
# exibir_dados(): Exibe o nome, salário e o departamento (sobrescreve o método da classe Funcionario).

# Classe Vendedor (classe filha):
# Atributos adicionais: total_vendas
# Método:
# exibir_dados(): Exibe o nome, salário e o total de vendas (sobrescreve o método da classe Funcionario).

# Regras:
# Use herança para a criação das classes Gerente e Vendedor.
# Sobrescreva o método exibir_dados() nas classes filhas.
# Use o método aumentar_salario da classe Funcionario para aumentar o salário de todos os funcionários.

# Adicione um atributo comissao na classe Vendedor para calcular a comissão de 5% sobre o valor total de vendas.
# Utilize o super() na classe Vendedor para chamar o método __init__ da classe Funcionario e garantir que o salário base do vendedor 
# seja corretamente inicializado.
# Crie um método calcular_comissao() na classe Vendedor para calcular e adicionar a comissão ao salário do vendedor.
# Sobrescreva o método exibir_dados() na classe Vendedor para incluir a comissão no salário.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def exibir_dados(self):
        return f"Nome {self.nome}, salario = {self.salario}"
    
    def aumentar_salario(self, valor):
        self.salario += valor
        return f"Seu salario aumentou e foi para {self.salario}"
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario, total_vendas):
        super().__init__(nome, salario)
        self.total_vendas = total_vendas
        self.comissao = 0
    
    def calcular_comissao(self):
        self.comissao = self.total_vendas * 0.05
        self.salario += self.comissao

    def exibir_dados(self):
        return f"Nome: {self.nome}, Salário base: {self.salario - self.comissao}, Total de vendas: {self.total_vendas}, Comissão: {self.comissao}, Salário total: {self.salario}" #Sobrescrevemos a classe
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
        
    def exibir_dados(self):
        return f"Nome {self.nome}, salario = {self.salario}, departamento = {self.departamento}"   #Sobrescrevemos a classe

f1 = Funcionario("Carlos", 3000)
print(f1.exibir_dados())
f1.aumentar_salario(500)
print(f1.exibir_dados())

v1 = Vendedor("Ana", 2500, 50000) 
print(v1.exibir_dados())  
v1.calcular_comissao()
print(v1.exibir_dados())  