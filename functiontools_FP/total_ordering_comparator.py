# Given a class defining one or more rich comparison
# ordering methods, this class decorator supplies the rest

# The class should supply an __eq__() method
# The class must define one of __lt__(), __le__(), __gt__(), or __ge__()

from functools import total_ordering

@total_ordering
class Car:      # Comparator functions
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage
        print("=== If any function is not overrided, it will automatically be created ===")

    def __eq__(self, car2):
        return self.mileage == car2.mileage

    def __lt__(self, car2):
        return self.mileage < car2.mileage

 # Comparator
car1 = Car("Audi",10)
car2 = Car("Honda",20)

print('car1 ("Audi",10) == car2 ("Honda",20): ', car1==car2)
print('car1 ("Audi",10) != car2 ("Honda",20): ', car1!=car2)
print('car1 ("Audi",10) < car2 ("Honda",20): ', car1<car2)
print('car1 ("Audi",10) <= car2 ("Honda",20): ', car1<=car2)
print('car1 ("Audi",10) > car2 ("Honda",20): ', car1>car2)
print('car1 ("Audi",10) >= car2 ("Honda",20): ', car1>=car2)