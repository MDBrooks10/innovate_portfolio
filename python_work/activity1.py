greeting = "Welcome to Code Nation"
greetlen = len(greeting)

print(greeting)
print(len(greeting))

def check():
    if greetlen%2==0:
        print(f"{greeting} is {greetlen} index places long. This is even.")
    else:
        print(f"{greeting} is {greetlen} index places long. This is odd.")

check()

greeting = greeting.replace("l", "")
greetlen = len(greeting)

check()