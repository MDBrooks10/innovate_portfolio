class Person():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def talk(self):
        print(f"Hello my name is {self.name}, I'm {self.height} tall and {self.age} years old.")

    def set_hair(self, hair):
        self.hair = hair

    def get_hair(self, hair):
        self.hair = hair

# will = Person("Will", "6ft", 31)
# mark = Person("Mark", "6ft", 37)


# user_name = input("Name...")
# user_height = input("Height...")
# user_age = input("Age...")

# Mark = Person(user_name, user_height, user_age)

# print(mark.name)
# print(mark.height)
# print(mark.age)
# mark.talk()

# print("Enter user name...")
# user_choice = input()

# if user_choice.lower == "will":
#     Will.talk()
# if user_choice.lower == "mark":
#     Mark.talk()
# else:
#     print("User not available")