# --------------------------------------abstract class and abstract method---------------------------------------


from abc import ABC, abstractmethod

class computer(ABC):

    @abstractmethod
    def process(self):
        pass
class Laptop(computer):
    def process(self):
        print("its working")

class programmer:

    def work(self, com):
        print("solving bugs")
        com.process()


# com = computer()
com1 = Laptop()
# com1.process()

prog1 = programmer()
prog1.work(com1)

