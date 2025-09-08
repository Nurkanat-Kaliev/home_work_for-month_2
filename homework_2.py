class Person:
    def __init__(self,name,birth_date,occupation,higher_edu):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_edu = higher_edu

    def introduce(self):
        print(f"Name: {self.name} \n"
              f"Occupation: {self.occupation} \n"
              f"Born in {self.birth_date} \n"
              f"Higher education: {self.higher_edu}")

class Classmate(Person):
    def __init__(self,name,birth_date,occupation,higher_edu,group_name):
        super().__init__(name,birth_date,occupation,higher_edu)
        self.group_name = group_name

    def introduce(self):
        print(f"Hello I'm {self.name} \n"
              f"Also Kanat's classmate we studied in {self.group_name}\n"
              f"I was born in {self.birth_date}\n"
              f"I work as a {self.occupation}\n"
              f"Higher education: {self.higher_edu}\n")

class Friend(Person):
    def __init__(self,name,birth_date,occupation,higher_edu,hobby):
        super().__init__(name,birth_date,occupation,higher_edu)
        self.hobby = hobby

    def introduce(self):
        print(f"Hello I'm {self.name} \n"
              f"Also Kanat's friend \n"
              f"I was born in {self.birth_date}\n"
              f"I work as a {self.occupation}\n"
              f"My hobby is {self.hobby}\n"
              f"Higher education: {self.higher_edu}\n")

classmate_1 = Classmate("Bektur", "5.12.2000", "Backend dev", True,"11-D")
classmate_2 = Classmate("Arstan", "9.11.2000", "Game dev", True,"11-D")
friend_1 = Friend("Turan", "27.11.2000", "Entrepreneur", False, "Wrestling")
friend_2 = Friend("Umut", "05.05.2000", "Data scientist", True, "football")

data = [classmate_1,classmate_2,friend_1,friend_2]

for char in data:
    char.introduce()





