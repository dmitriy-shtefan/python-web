class Animal:
    def __init__(self, name):
        self._name = name
        
    def describe(self):
        return f"Animal: {self._name}"

    def __str__(self):
        return f"Animal: {self._name}"

    # def __repr__(self):
    #    return f"__repr__ Animal: {self._name}"


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        
    def describe(self):
        return f"Dog: {self._name}"

    def __str__(self):
        return f"Dog: {self._name}"

    def __repr__(self):
        return f"__repr__ Dog: {self._name}"
    
    
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    
    def describe(self):
        return f"Cat: {self._name}"

    def __str__(self):
        return f"Cat: {self._name}"

    def __repr__(self):
        return f"__repr__ Cat: {self._name}"
    
class Bird(Animal):
    def __init__(self, name, age):
        self.age = age
        Animal.__init__(self, name)
    
    def describe(self):
        return f"Bird: {self._name}"

    def __str__(self):
        return f"Bird: {self._name}, age: {self.age}"

    # def __repr__(self):
    #    return f"__repr__ Bird: {self._name}"

    # less than
    def __lt__(self, other):
        return self.age < other.age

    # greater than
    def __gt__(self, other):
        return self.age > other.age

    # equal
    def __eq__(self, other):
        return self.age == other.age

    # для функції len
    def __len__(self):
        return len(self._name)

    # для використання обʼєкту по типу функції
    def __call__(self):
        print(self)
    
    
animals_list = [
    Animal('Bob'),
    Dog('Martha'),
    Cat('Meow'),
    Bird('Jack', 1)
]



# for animal in animals_list:
    # print(animal.describe())


for animal in animals_list:
    print(animal)

print(animals_list)

print(Animal('Ionia'))

bird1 = Bird('Jack', 1)
bird2 = Bird('Ionia', 2)

print(bird1 > bird2)


print(len(bird1))
print(len(bird2))


bird1()