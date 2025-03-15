''''''
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class dog(animal):
    def make_sound(self):
        print("dog says:woof woof!")


class cat(animal):
    def make_sound(self):
        print("cat says:meow meow")

d=dog()
d.make_sound()

c=cat()


c.make_sound()

#new example of thr abstract class 
from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def move_forward(self):
        pass
    def move_backward(self):
        pass
    def fm(self):
        pass


class innova(car):
    def move_forward(self):
        print("move forward!")

    #def move_backward(self):
        #print("move backward")

    def fm(self):
        print("music playing")

c1=innova()
c1.move_backward()
c1.move_forward()
c1.fm()        




