from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel
class Vehicle(ABC):
    def __init__(self, weight = 1000, started = 5, fuel = 30, fuel_consumption = 10):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if self.started =


    def move(self):
        pass

