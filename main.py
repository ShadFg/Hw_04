class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"{self.name} {self.age} years")

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Crockodile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Kenguru(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

tiger = Tiger("tiger", 7)
tiger.showInfo()

crockodile = Crockodile("crockodile", 1)
crockodile.showInfo()

kenguru = Kenguru("kenguru", 3)
kenguru.showInfo()