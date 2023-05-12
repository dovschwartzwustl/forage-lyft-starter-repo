from tires.tires import Tires

class Octoprime(Tires):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        result = 0
        for i in self.sensor_array:
            result += i
        
        if result >= 3:
            return True
        else:
            return False
