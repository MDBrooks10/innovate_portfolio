print("Enter a number...")

def num_in():
    num = input("")
    try:
        print(f"You have chosen the number {num}.")
        print(type(int(num)))

    except:
        print("Error!")
        print("Unknown input")
        num_in()

num_in()