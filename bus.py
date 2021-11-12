import random
from transportation import *


#----------------------------------------------
class Bus(Transportation):
    def __init__(self):
        super(Bus, self).__init__()
        self.passenger_capacity = 0

    # Input bus parameters from the file.
    def in_data(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.passenger_capacity = int(strArray[i])
        self.fuel_tank_capacity = int(strArray[i + 1])
        self.lit_per_100_km = float(strArray[i + 2])
        return i + 3

    # Creating random parameters for the bus.
    def rnd(self):
        self.fuel_tank_capacity = random.randint(0, 256)
        self.passenger_capacity = random.randint(0, 256)
        self.fuel_tank_capacity = random.randint(200, 300)
        self.lit_per_100_km = round(random.uniform(41.0, 100.0), 1)

    # Output bus parameters.
    def out(self, ostream):
        ostream.write("This is a bus: passenger capacity = " + self.passenger_capacity.__str__())
        ostream.write(". Fuel tank capacity = " + self.fuel_tank_capacity.__str__())
        ostream.write("; Liters per 100 km needed " + self.lit_per_100_km.__str__())
        ostream.write(". Max distance can be covered = " + self.max_dist().__str__())

