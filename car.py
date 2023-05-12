from servicable import Serviceable

#inherits from the serviceable class

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.battery = battery
        self.engine = engine
        self.tires = tires

   #must implement a needs_service method from Serviceable

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tires.needs_service()
