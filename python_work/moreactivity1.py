def num_in():
    print("Enter a number...")
    num = input("")
    try:
        print(f"You have chosen the number {num}.")
        print(type(int(num)))

    except:
        print("Error!")
        print(f"{num} is not a number")
        num_in()

num_in()