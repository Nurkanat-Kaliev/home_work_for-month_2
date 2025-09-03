class Person:
    def __init__(self,name,birth_date,occupation,higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Identity:\n "
              f"name: {self.name}\n"
              f"birth date: {self.birth_date}\n"
              f"occupation: {self.occupation}\n"
              f"higher education: {self.higher_education}\n")

identity = Person("Soup","08.09.1986","SAS soldier",False)
identity_2 = Person("Price","06.11.1977","SAS soldier",False)
identity_3 = Person("Trump","14.07.1946","US presidnet",True)
identity.introduce()
identity_2.introduce()
identity_3.introduce()