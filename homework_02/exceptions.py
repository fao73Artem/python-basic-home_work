"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self):
        super().__init__(self)


class NotEnoughFuel(Exception):
    def __init__(self):
        super().__init__(self)



class CargoOverload(Exception):
    def __init__(self):
        super().__init__(self)




# try:
#     pass
# except LowFuelError
# except NotEnoughFuel
# except CargoOverload