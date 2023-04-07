"""
создайте класс `Plane`, наследник `Vehicle`
"""
class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = max_cargo
    super().__init__(max_cargo)

    def load_cargo(self, cargo_add):
        if self.cargo + cargo_add <= max_cargo:
            self.cargo += cargo_add
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        self.cargo = 0
        self.cargo = self.load_cargo

