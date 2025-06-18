class transport:
    def __init__(self, name, type,):
        self.name = name
        self.type = type
bus = transport("bus", "public")
car = transport("car", "private")
bike = transport("bike", "private")
print(bus.name, bus.type)
print(car.name, car.type)
print(bike.name, bike.type)
print("The {} is a {} transport.".format(bus.name, bus.type))
print("The {} is a {} transport.".format(car.name, car.type))
print("The {} is a {} transport.".format(bike.name, bike.type))

