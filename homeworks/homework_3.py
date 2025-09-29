import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_edu):
        self.name = name
        self.__birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y").date()
        self.__occupation = occupation
        self.__higher_edu = higher_edu

    @property
    def get_occupation(self):
        return self.__occupation

    @property
    def age(self):
        today = datetime.date.today()
        years = today.year - self.__birth_date.year
        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
            years -= 1
        return years

    @property
    def get_edu(self):
        return self.__higher_edu

    def introduce(self):
        education = "есть высшее образование" if self.__higher_edu else "нет высшего образования"
        print(f"Hello I'm {self.name} \n"
              f"My age is {self.age}\n"
              f"I work as a {self.get_occupation}\n"
              f"Higher education: {education}\n")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_edu, group_name):
        super().__init__(name, birth_date, occupation, higher_edu)
        self.group_name = group_name

    def introduce(self):
        education = "есть высшее образование" if self.get_edu else "нет высшего образования"
        print(f"Hello I'm {self.name} \n"
              f"Also Kanat's classmate, we studied in {self.group_name}\n"
              f"My age is {self.age}\n"
              f"I work as a {self.get_occupation}\n"
              f"Higher education: {education}\n")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_edu, hobby):
        super().__init__(name, birth_date, occupation, higher_edu)
        self.hobby = hobby

    def introduce(self):
        education = "есть высшее образование" if self.get_edu else "нет высшего образования"
        print(f"Hello I'm {self.name} \n"
              f"Also Kanat's friend \n"
              f"My age is {self.age}\n"
              f"I work as a {self.get_occupation}\n"
              f"My hobby is {self.hobby}\n"
              f"Higher education: {education}\n")


# создаём объекты
person = Person("Kanat", "03.08.2000", "Data scientist", True)
classmate_1 = Classmate("Bektur", "05.12.2000", "Backend dev", True, "11-D")
classmate_2 = Classmate("Arstan", "09.11.2000", "Game dev", True, "11-D")
friend_1 = Friend("Turan", "27.11.2000", "Entrepreneur", False, "Wrestling")
friend_2 = Friend("Umut", "05.05.2000", "Data scientist", True, "Football")

data = [person, classmate_1, classmate_2, friend_1, friend_2]

for char in data:
    char.introduce()
