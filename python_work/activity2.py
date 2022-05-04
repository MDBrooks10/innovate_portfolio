alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# print(alphabet)

# print(alphabet[3])

for x in alphabet:
    print(x)



def letter_number():
    user_input = int(input("Pick a number between 1 and 26..."))
    index_prop = user_input -1

    if user_input >= 1 and user_input <= 26:
        print (alphabet[index_prop])
    else:
        print ("Error...")
        letter_number()

letter_number()