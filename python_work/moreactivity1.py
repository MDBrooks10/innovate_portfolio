print("Enter a number...")

num = input("")

def num_in():
    try:
        print(f"You have chosen the number {num}.")

    except:
        print("Error!")
        print("Unknown input")
        num_in()

num_in()

print(type(int(num)))