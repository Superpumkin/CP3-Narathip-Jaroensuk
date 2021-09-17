class Vehicle :
    license_Code = ''
    serial_Code = ''
    
    def turnOnAirConditioner(self) :
        print(f'{self.license_Code} => Turn On : Air')

class Car(Vehicle) :
    pass

class Pickup(Vehicle) :
    pass

class Van(Vehicle) :
    pass

class EstateCar(Vehicle) :
    pass

# CAR
car_1 = Car()
car_1.license_Code = 'CAR'
car_1.turnOnAirConditioner()

# PICKUP
car_2 = Car()
car_2.license_Code = 'PICKUP'
car_2.turnOnAirConditioner()

# VAN
car_3 = Car()
car_3.license_Code = 'VAN'
car_3.turnOnAirConditioner()

# ESTATECAR
car_4 = Car()
car_4.license_Code = 'ESTATECAR'
car_4.turnOnAirConditioner()