from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime


#must import these classes to use their functionalities

#each method takes in the necessary variables and..
#passes them into either the Engine or the Battery fields...
#to make the necessary batteries or engines...
#the car is then composed of those batteries/engines and returned

#this factory method makes it easy to add new cars to the fleet
#would also not be that hard to add different components such as tires


class carFactory:
    @staticmethod
    def create_Calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Carrigan(sensor_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Octoprime(sensor_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, sensor_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Carrigan(sensor_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = Carrigan(sensor_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = Octoprime(sensor_array)
        car = Car(engine, battery, tires)
        return car