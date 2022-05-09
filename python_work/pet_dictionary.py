pet_dict = {
    "Name":"Ziggy",
    "Age":3,
    "Colour":"Black",
    "Breed":"Dorkie",
    "Fed and Watered":True,
    "Steps taken on walk":4677,
    "Mood":"Asleep",
}

print(pet_dict)
print(pet_dict["Name"])

pet_dict["Mood"] = "Barking at postie"
pet_dict["Fed and Watered"] = False
pet_dict["Steps taken on walk"] = 0
pet_dict["Mood"] = "Hungry"

print(pet_dict)

print(pet_dict.keys())