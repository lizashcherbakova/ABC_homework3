import random
from transportation import *


#----------------------------------------------
class Truck(Transportation):
    def __init__(self):
        super(Truck, self).__init__()
        self.load_capacity = 0

    # Input truck parameters from the file.
    def in_data(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.load_capacity = int(strArray[i])
        self.fuel_tank_capacity = int(strArray[i + 1])
        self.lit_per_100_km = float(strArray[i + 2])
        return i + 3

    #  Creating random parameters for the truck.
    def rnd(self):
        self.load_capacity = random.randint(0, 28000)
        self.fuel_tank_capacity = random.randint(200, 1500)
        self.lit_per_100_km = round(random.uniform(10.0, 100.0), 1)

    #  Output track parameters.
    def out(self, ostream):
        ostream.write("This is a truck: load capacity = " + self.load_capacity.__str__())
        ostream.write(". Fuel tank capacity = " + self.fuel_tank_capacity.__str__())
        ostream.write("; Liters per 100 km needed " + self.lit_per_100_km.__str__())
        ostream.write(". Max distance can be covered = " + self.max_dist().__str__())

