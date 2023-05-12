from abc import ABC, abstractmethod

from car import Car

class Engine(Car):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def needs_service(self):
        pass
