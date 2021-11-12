#----------------------------------------------
class Transportation:
    def __init__(self):
        self.fuel_tank_capacity = 0
        self.lit_per_100_km = 0.0

    def in_data(self, strArray, i):
        pass

    def rnd(self):
        pass

    def out(self, ostream):
        pass

    def max_dist(self):
        return self.lit_per_100_km * 100.0 * self.fuel_tank_capacity
