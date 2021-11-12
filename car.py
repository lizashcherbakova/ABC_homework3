import random
from transportation import *


#----------------------------------------------
class Car(Transportation):
    def __init__(self):
        super(Car, self).__init__()
        self.max_speed = 0

    # Input car parameters from the file.
    def in_data(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.max_speed = int(strArray[i])
        self.fuel_tank_capacity = int(strArray[i + 1])
        self.lit_per_100_km = float(strArray[i + 2])
        # print("Rectangle: x = ", self.x, " y = ", self.y)
        return i + 3

    # Creating random parameters for the car.
    def rnd(self):
        self.max_speed = random.randint(0, 256)
        self.fuel_tank_capacity = random.randint(45, 100)
        self.lit_per_100_km = round(random.uniform(5.0, 15.0), 1)

    #  Output car parameters.
    def out(self, ostream):
        ostream.write("This is a car: maximum speed = " + self.max_speed.__str__())
        ostream.write(". Fuel tank capacity = " + self.fuel_tank_capacity.__str__())
        ostream.write( "; Liters per 100 km needed " +  self.lit_per_100_km.__str__())
        ostream.write(". Max distance can be covered = " + self.max_dist().__str__())

