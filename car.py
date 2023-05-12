from abc import ABC, abstractmethod

from servicable import Serviceable

class Car(Serviceable, ABC):
    def __init__(self, Engine, Battery):
        self.Battery = Battery
        self.Engine = Engine

    @abstractmethod
    def needs_service(self):
        pass
