# Using Magic functions for comparison
# __eq__, __lt__, __gt__, __le__, __le__

class Car:      # Comparator functions
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage
        print("=== If any function is not overrided, it will throw error ===")

    def __lt__(self, car2):
        return self.mileage < car2.mileage

    def __gt__(self, car2):
        return self.mileage > car2.mileage
        
    def __le__(self, car2):
        return self.mileage <= car2.mileage

    def __ge__(self, car2):
        return self.mileage >= car2.mileage
    
    def __eq__(self, car2):
        return self.mileage == car2.mileage

    def __ne__(self, car2):
        return self.mileage != car2.mileage

 # Comparator
car1 = Car("Audi",10)
car2 = Car("Honda",20)

print('car1 ("Audi",10) == car2 ("Honda",20): ', car1==car2)
print('car1 ("Audi",10) != car2 ("Honda",20): ', car1!=car2)
print('car1 ("Audi",10) < car2 ("Honda",20): ', car1<car2)
print('car1 ("Audi",10) <= car2 ("Honda",20): ', car1<=car2)
print('car1 ("Audi",10) > car2 ("Honda",20): ', car1>car2)
print('car1 ("Audi",10) >= car2 ("Honda",20): ', car1>=car2)