class Person:
    def __init__(self,name,birth_date,occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"My name is {self.name},I was born in {self.birth_date} i work as a {self.occupation}")

class Classmate(Person):
    def __init__(self,name,birth_date,occupation):
        super().__init__(self,name,birth_date,occupation)

    def introduce(self):
        print(f"Hello! I'm {self.name}'s {self.name}")

class Friend(Person):
    def __init__(self, name, birth_date, occupation):
        super().__init__(self, name, birth_date, occupation)

    def introduce(self):
        print(f"I'm {self.name}'s friend my name is {self.name}")


