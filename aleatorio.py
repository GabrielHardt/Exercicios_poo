#Escreva um programa Python para criar uma classe Vehicle com atributos max_speedde mileageinstância.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

carro = Vehicle(100, 18)
print(carro.max_speed, carro.mileage)

# Exercício 3 de POO: Crie uma classe filha Bus que herdará todas as variáveis ​​e métodos da classe Vehicle

class Bus(Vehicle):
    pass

onibus = Bus(200,8)
print(f"Velocidade maxima do onibus {onibus.max_speed}, mileage = {onibus.mileage} ")

# Crie uma classe Bus que herde da classe Vehicle . Dê ao argumento capacity Bus.seating_capacity()um valor padrão de 50.

# Use o código a seguir para sua classe pai Vehicle.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (f"The seating capacity of a {self.name} is {capacity}")

class Bus(Vehicle):
    pass

    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity= 50)

onibus = Bus("onibus", 18, 180)
print(onibus.seating_capacity())

# Exercício 5 de POO: Defina uma propriedade que deve ter o mesmo valor para cada instância de classe (objeto)
# Defina um atributo de classe “ color ” com um valor padrão white . Ou seja, todo veículo deve ser branco.

# Use o código a seguir para este exercício.

class Vehicle:
    color = "branco"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

onibus = Bus("escolar", 180, 18)
print(onibus.color, onibus.name, onibus.max_speed)

# Crie uma classe filha Bus que herda da classe Vehicle. A tarifa padrão de qualquer veículo é capacidade de assentos * 100. 
# Se Vehicle for uma instância Bus , precisamos adicionar 10% extras na tarifa cheia como uma taxa de manutenção. Então a tarifa
#  total para a instância bus se tornará o valor final = tarifa total + 10% da tarifa total.

# Observação: a capacidade do ônibus é de 50 assentos , então o valor final da tarifa deve ser 5.500. 
# Você precisa substituir o fare()método de uma classe de veículo na classe de ônibus.

# Use o seguinte código para sua classe pai Vehicle. Precisamos acessar a classe pai de dentro de um método de uma classe filha.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass

    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())