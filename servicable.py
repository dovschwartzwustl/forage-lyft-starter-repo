from abc import ABC, abstractmethod

#the highest level abstract class

#used by car but can also be used by other forms of transportation


class Serviceable(ABC):
    
    @abstractmethod
    def needs_service(self):
        pass

