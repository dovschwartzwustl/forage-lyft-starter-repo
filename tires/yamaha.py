from tires.tires import Tires

class Yamaha(Tires):
    def __init__(self, current_mileage):
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage > 2000