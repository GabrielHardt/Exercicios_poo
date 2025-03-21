class ContaBancaria:
    def __init__(self, titular, saldo,):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return f"Voce depositou {valor}, Saldo atual = {self._saldo}"
        else:
            return "Seu valor precisar ser maior que zero"
    
    def sacar(self, valor): 
        if valor < self._saldo :
            return f"Voce sacou {valor}, Saldo atual = {self._saldo - valor}"
        else:
            return f"Saldo insuficiente para este saque, seu saldo eh {self._saldo}"
        
    def consultar_saldo(self):
        return f"Seu saldo atual e de: {self._saldo}"


    
A = ContaBancaria("Maria", 2000)
print(A.sacar(300))
print(A.depositar(200))
print(A.consultar_saldo())