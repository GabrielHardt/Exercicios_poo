#encapsulamento, polimorfismo e interfaces e classes abstratas

# Exercício: Sistema de Pagamento
# Você foi contratado para desenvolver um sistema de pagamento de uma loja. Esse sistema deve ser capaz de lidar com diferentes formas de pagamento (cartão de crédito, boleto e pix).

# Implemente uma estrutura de classes que siga os conceitos abaixo:

# 📌 Regras:
# Interface (Classe Abstrata):

# Crie uma classe abstrata Pagamento com o método abstrato pagar(self, valor).

# Encapsulamento:

# Cada classe de pagamento (CartaoCredito, Boleto, Pix) deve ter um atributo privado chamado saldo.

# Crie um método get_saldo() para acessar o saldo.

# Polimorfismo:

# Cada classe concreta (CartaoCredito, Boleto, Pix) deve implementar o método pagar, de forma diferente.

# Faça um pequeno menu de simulação onde o usuário escolha a forma de pagamento e o valor da compra.

# Pontos trabalhados:
# ✅ Encapsulamento: saldo privado (__saldo)
# ✅ Polimorfismo: método pagar() é implementado de forma diferente nas 3 classes
# ✅ Classe Abstrata / Interface: Pagamento define o método abstrato pagar()


from abc import ABC, abstractmethod

class Pagamento(ABC): #Impedir a criação de objetos da classe abstrata: Ninguém pode fazer pagamento = Pagamento(). Ela é só um molde.
    @abstractmethod # Ele serve para marcar um método que todas as classes filhas são obrigadas a implementar. Neste caso, pagar
    def pagar(self, valor):    # quando se colocar o @abstractMethod , basicamente se esta falando "Toda classe que herdar de Pagamento vai ser obrigada a criar o método pagar() do jeito dela."
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor, saldo):
        super().__init__(valor)
        self.__saldo = saldo           #saldo esta encapsulado
    
    def get_saldo(self):
        return f"Seu saldo Atual e de: {self.__saldo}"    # para saber quanto de saldo possuimos, teremos que chamar este metodo
    
# Se um dado é privado da classe filha, ele deve ser acessado só pelos métodos da filha.

    def pagar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return f"Compra aprovada aprovada no valor de R${valor}"
        else:
            return f"Saldo insuficiente para compra"

class Boleto(Pagamento):
    def __init__(self, valor, saldo):
        super().__init__(valor)
        self.__saldo = saldo           
    
    def get_saldo(self):
        return f"Seu saldo Atual e de: {self.__saldo}"    
    
    def pagar(self, valor):
        return f"Boleto gerado no valor de R${valor}"
    
class Pix(Pagamento):
    def __init__(self, valor, saldo):
        super().__init__(valor)
        self.__saldo = saldo          
    
    def get_saldo(self):
        return f"Seu saldo Atual e de: {self.__saldo}"    
    
    def pagar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor  # Aqui desconta o saldo
            return f"Pix realizado no valor de R${valor}"
        else:
            return f"Saldo insuficiente para Pix"
        

# 📌 Confirmação ponto a ponto:
# ✅ Encapsulamento → Está presente no __saldo

# O __saldo é privado

# Só pode ser acessado/modificado pelos métodos da própria classe (get_saldo(), pagar())

# Protege o dado de alterações externas e acidentais

# ✅ Interface → Representada pela classe abstrata Pagamento

# Ela obriga qualquer classe filha a implementar o método pagar()

# É o famoso "contrato": "se você é um Pagamento, você precisa saber pagar"

# ✅ Polimorfismo → Acontece quando você tem várias classes diferentes (CartaoCredito, Pix, Boleto)

# Todas possuem o método pagar()

# Mas cada uma faz do seu jeito

# Quando você chama pagar() em uma lista de objetos Pagamento, o Python executa o método correto dependendo da classe real daquele objeto

