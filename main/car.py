class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("this car is driving now")
        
    def stop(self):
        print("this car is stopped")
       
    def pres(self):
        print("this "+self.make+" "+self.model+" is super nice!")