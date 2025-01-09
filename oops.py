

class Vehicle:
    my_val = "simple_vehicle"

    def __init__(self):
        self.fuel = 0

    def add_fuel(self, fuel):
        self.fuel += fuel


if __name__ == '__main__':
    v = Vehicle()
    v.add_fuel(100)
    print(v.__dict__)
    print(v.__class__)
    # print(Vehicle.__dict__)
    for itm in Vehicle.__dict__:
        print(itm, ":", Vehicle.__dict__[itm])
    print(Vehicle.__class__)
    print(Vehicle.__name__)

    print(Vehicle)

