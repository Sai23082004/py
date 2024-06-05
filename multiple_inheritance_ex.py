class driver:
    def __init__(self,f_name,l_name,age,mob_no):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
        self.mob_no=mob_no
    def full_name(self):
        return f'{self.f_name} {self.l_name}'
    
class license(driver):
    def __init__(self, f_name, l_name, age,mob_no,license_id,validity_year):
        driver.__init__(self,f_name, l_name, age,mob_no)
        self.license_id=license_id
        self.validity_year=validity_year

    def is_valid_license(self):
        if self.validity_year>=2021:
            return True
        else:
            False

class vehicle(license):
    def __init__(self, f_name, l_name, age, mob_no, license_id, validity_year,vehicle_no,vehicle_age):
        license.__init__(self,f_name, l_name, age, mob_no, license_id, validity_year)
        self.vehicle_no=vehicle_no
        self.veicle_age=vehicle_age

    def is_valid_driver(self):
        if self.age>=18:
            return True
        else:
            False

class disel:
    def __init__(self,price):
        self.price=price
    def print__price(self):
        print(self.price)


class petrol:
    def __init__(self,price):
        self.price=price
    def print_petrol_price(self):
        print(self.price)


class bus(vehicle,disel):
    def __init__(self, f_name, l_name, age, mob_no, license_id, validity_year, vehicle_no, vehicle_age,price,wheel):
        vehicle.__init__(self,f_name, l_name, age, mob_no, license_id, validity_year, vehicle_no, vehicle_age)
        disel.__init__(self,price)
        self.wheel=wheel 


bus= bus('user','one',22,901480,101,2022,23,2,100,6)
print('full name =',bus.full_name())
print('licence valid = ',bus.is_valid_license())
print('driver elgible =',bus.is_valid_driver())
bus.print__price()