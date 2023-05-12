from tires.tires import Tires

class Carrigan(Tires):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array
    
    def needs_service(self):
        for i in self.sensor_array:
            if i >= 0.9:
                return True
        
        return False

        