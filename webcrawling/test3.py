class Dog:
    # class attribute, class variables
    species = 'Dog'

    # intitialize; instance
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Class information
print(Dog)
print(Dog.species)

# create instances
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("kind", 4)

# compare
print(a == b, b == c, id(a), id(b), id(c))

# name space
print('Dog a', a.__dict__)
print('Dog b', b.__dict__)
print('Dog c', c.__dict__)

print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))
print('{} is {}'.format(c.name, c.age))