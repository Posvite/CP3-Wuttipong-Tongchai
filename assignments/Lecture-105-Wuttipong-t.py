class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass

car1 = Vehicle()
car1.turnOnAirConditioner()

pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()
