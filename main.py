'''
class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:", end=" ")
            for passenger in self.passengers:
                print(passenger.name, end=" ")
            print("")
        else:
            print(f"There're not passengers.")

nick = Human("Nick")
kate = Human("Kate")

car = Auto("")
car.add_passengers(nick, kate)
car.print_passengers()

class C1:
    var = 20
    def __init__(self):
        var = 10
class C2(C1):
    def __init__(self):
        print("var=",self.var)
        super().__init__()
        print(self.var)
nick = C2()
print(nick.var)
'''
'''
class Audioplayer:
    def aplay(self):
        pass
class Videoplayer:
    def vplay(self):
        pass
class Multiplayer(Audioplayer, Videoplayer):
    def play(self):
        pass

multiplayer=Multiplayer()
multiplayer.play()
multiplayer.aplay()
multiplayer.vplay()

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

        self.memory = 128

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)
        print(self.model)

iphone = SmartPhone(model ="Last")
iphone.print_info()

'''

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname =firstname
        self.lastname = lastname
        self.age = age

    def get_Info(self):
        return (f"Person first name - {self.firstname}; "
                f"last name - {self.lastname}; "
                f"age - {self.age}; ")
    def getHi(self, msgText):
        return f"{msgText}! I am {self.firstname}."

class Employee(Person):
    def __init__(self, firstname, lastname, age, jobTitle, salary, seniority):
        super().__init__(firstname, lastname, age)
        self.jobTitle = jobTitle
        self.salary = salary
        self.seniority = seniority

    def get_Info(self):
        return super().get_Info()+(f"job title - {self.jobTitle}; salary - {self.salary}; seniority - {self.seniority}.")
    def getSickLeavePer(self):
        if self.seniority>5:
            return 1
        elif self.seniority>3:
            return 0.75
        else:
            return 0.5

employee1 = Employee("Kate", "Smith", 28, "Hr", 2800, 7)
print(employee1.getHi("Hie"))
print(employee1.get_Info())
print(f"If sick: {employee1.getSickLeavePer()*100}%")

#task 3
class Money:
    def __init__(self, money, penny):
        self.money = money
        self.penny = penny
        self.norm()
    def norm(self):
        self.money += self.penny // 100
        self.penny = self.penny % 100
    def set_money(self, money):
        self.money = money
    def set_penny(self, penny):
        self.penny = penny
        self.norm()
    def print_balance(self):
        return f"Your balance {self.money}.{self.penny if self.penny>10 else '0'+str(self.penny)}"

balance = Money(10, 854)
print(balance.print_balance())
balance.set_money(20)
print(balance.print_balance())
balance.set_penny(109)
print(balance.print_balance())

#task 1
class Device:
    def __init__(self, brand, typ, price, warranty, size, power):
        self.brand = brand
        self.price = price
        self.type = typ
        self.warranty = warranty
        self.size = size
        self.power = power

class CoffeeMachine(Device):
    def __init__(self, brand, typ, price, warranty, size, capacity, power):
        super().__init__(brand, typ, price, warranty, size, power)

        self.capacity = capacity

class Blender(Device):
    def __init__(self, brand, typ, price, warranty, size, power, capacityGlass):
        super().__init__(brand, typ, price, warranty, size, power)
        self.capacityGlass = capacityGlass

class MeatGrinder(Device):
    def __init__(self, brand, typ, price, warranty, size):
        super().__init__(brand, typ, price, warranty, size)
