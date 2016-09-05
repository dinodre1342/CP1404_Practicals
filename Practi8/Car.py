 import random
 class Car:
    """ represent a car object """

    def _init_(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def _str_(self):
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

     def _init_(self, fuel, reliability):
         """ initialise a Car instance """
         self.fuel = fuel
         self.reliability = reliability

     def _str_(self):
         return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

     def drive(self, distance):
         """ drive the car a given distance if it has enough fuel or drive until fuel runs out
         return the distance actually driven """
         print(self.reliability.random)

         if distance > self.fuel:
             distance_driven = self.fuel
             self.fuel = 0
         else:
             self.fuel -= distance
             distance_driven = distance
         self.odometer += distance_driven
         return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    def _init_(self, name, fuel, price_per_km):
        """ initialise a Taxi instance, based on parent class Car """
        super().init_(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def _str_(self):
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



