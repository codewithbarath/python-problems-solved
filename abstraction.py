from abc import ABC,abstractmethod
class vehical(ABC):
    @abstractmethod
    def startengine(self):
        pass

class car(vehical):
    def startengine(self):
        print("engine started!")

my_car=car()
my_car.startengine()
