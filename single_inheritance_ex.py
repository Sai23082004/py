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

user_1_license=license('user','one',20,901764,101,2022)
user_2_license=license('user','two',21,902764,102,2021)

print(user_1_license.is_valid_license())
print(user_1_license.full_name())