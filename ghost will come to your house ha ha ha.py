class Car:
    car_type = "car"  # class variable, same for all instances

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects
ferrari = Car("ferrari", 86)
lamborghini = Car("lamborghini", 62)
tesla = Car("tesla", 21)

# Printing name and age
print(ferrari.name, ferrari.age)
print(lamborghini.name, lamborghini.age)
print(tesla.name, tesla.age)

# Printing name and car type
print("{} is a {} car".format(ferrari.name, ferrari.car_type))
print("{} is a {} car".format(lamborghini.name, lamborghini.car_type))
print("{} is a {} car".format(tesla.name, tesla.car_type))