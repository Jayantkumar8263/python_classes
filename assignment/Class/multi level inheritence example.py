#Suppose you are tasked with modeling a hierarchy of vehicles. There are three main categories: Vehicle, Car, and ElectricCar. Each category has specific attributes and behaviors. Implement these classes using multi-level inheritance and provide a method to display the details of each vehicle.

class vehicle:
    def _init_(self,make, model, year):
        self.make = make
        self.model = model
        self.year= year
        
    def display_details(self):
        print(f'Make : {self.make}, Modle: {self.model}, Year: {self.year}')
        
class car(vehicle):
    def _init_(self, make, model,year, fuel_type):
        super()._init_(make, model,year)
        self.fuel_type=fuel_type
        
    def display_details(self):
        super().display_details()
        print(f'Fuel Type: {self.fuel_type}')
        
class electric_car(car):
    def _init_(self, make, model, year, battery):
        super()._init_(make, model, year, fuel_type= 'EV')
        self.battery = battery
    
    def display_details(self):
        super().display_details()
        print(f'Battery : {self.battery}')
        
        
# making the object 
my_car_obj = electric_car('tata','nexon', '2023', battery=100)

my_car_obj.display_details()