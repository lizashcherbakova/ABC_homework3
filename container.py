from car import *
from bus import Bus
from truck import Truck

#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    #  Outputs items in the container to the given file.
    def print(self, ostream):
        ostream.write("Container contains " + len(self.store).__str__() + " transportaion:\n")
        for transportation in self.store:
            transportation.out(ostream)
            ostream.write("\n")

    #   Input all transportation from the file. If meets a mistake stops reading.
    def read(self, strArray):
        # Index for current
        i = 0
        while i < len(strArray):
            key = int(strArray[i])
            if key == 0:  # Key for the car.
                i += 1
                transportation = Car()
                i = transportation.in_data(strArray, i)
            elif key == 1:  # Key for the bus.
                i += 1
                transportation = Bus()
                i = transportation.in_data(strArray, i)
            elif key == 2:  # Key for the truck.
                i += 1
                transportation = Truck()
                i = transportation.in_data(strArray, i)
            # Adding input transportation.
            self.store.append(transportation)

    #  Creating random transportation with given size.
    def rnd(self, size):
        len = 0
        while len < size:
            number = random.randint(0, 2)
            if number == 0:
                transportation = Car()
            elif number == 1:
                transportation = Bus()
            else:
                transportation = Truck()
            transportation.rnd()
            self.store.append(transportation)
            len += 1
