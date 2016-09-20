import random
class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class UnreliableCar(Car):
    """ represent a car object """

    def __init__(self, fuel, reliability):
        self.fuel = fuel
        self.reliability = reliability

    def __str__(self):
        return "{}, fuel={}, odo={}".format( self.fuel, self.odometer)

    def drive(self, distance):
        if self.reliability > random.randint(0,100):
            super().drive(distance)


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel, price_per_km):
        """ initialise a Taxi instance, based on parent class Car """
        super().init_(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, ${:.2f}/km, {}km on current fare".format(super().str_(), self.price_per_km,
                                                             self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def get_current_fair_distance(self):
        return self.current_fare_distance

    def get_fuel(self):
        return self.fuel

    def set_current_fair_distance(self, distance):
        self.current_fare_distance = distance

    def set_price_per_km(self, scale):
        self.price_per_km *= scale

if __name__ == "main":
    Prius1 = Taxi("Prius 1", 100)
    Prius1.drive(40)
    print("Fare: ${}\n".format(Prius1.get_fare()))

    Prius1.set_current_fair_distance(0)
    Prius1.drive(100)
    print(Prius1)
    print("Fare: ${}\n".format(Prius1.get_fare()))

class SilverServiceTaxi(Car):
    def __init__(self, name="", fuel=0, fanciness=50):
        super().__init__(name, fuel)
        super().set_price_per_km(fanciness)

        self.new_fare = 0
        self.flagfall = 4.5

    def get_fare(self):
        """Get the price of the taxi trip"""
        if not self.new_fare:
            return "{:.{prec}f}".format((self.price_per_km * self.current_fare_distance) + 4.5, prec=2)
        else:
            return "{:.{prec}f}".format(self.price_per_km * self.current_fare_distance, prec=2)

newTaxi = SilverServiceTaxi("Silver Service", 100, 2)
print(newTaxi)
newTaxi.driver(10)
print ("Fare: ${}".format(newTaxi.get_fare()))





