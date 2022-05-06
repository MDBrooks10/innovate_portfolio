# print("This is my file")

#----------------------------------
#Casting
#-------

# print (int(5.3))
# print (int("54"))

# print (float(54))

# print (type(str(54)))
# print (type(str(5.4)))

#-----------------------------------


#-----------------------------------
#Truthy and Falsey
#-----------------

# print ("What is your name?")
# name = input()

# if name:
#     print(f"Hello {name}")
# else:
#     print("You did not provide a name")


# print (not True)
# print (not False)

# bool = False
# if bool != True:
#     print(False)
# else:
#     print(True)

#-----------------------------------


#-----------------------------------
#Try/Except
#----------

# def add_up():
#     num1 = input("Number 1 \n")               #   This will add the two strings
#     num2 = input("Number 2 \n")               #       and not add the numbers
#     print (num1 + num2)

# add_up()


# def add_up():
#     num1 = input("Number 1 \n")                 #   Now we've used casting to let 
#     num2 = input("Number 2 \n")                 #       python know to treat these as intergers
#     print (int(num1) + int(num2))

# add_up()


# def add_up():
#     num1 = input("Number 1 \n")
#     num2 = input("Number 2 \n")

#     try:
#         print(f"{num1} + {num2} is {int(num1) + int(num2)}")        #   Incase user inputs characters and
#                                                                     #       not numbers. try and except will
#     except:                                                         #           let us catch errors
#         print("Error!")
#         print("**************")
#         add_up()

# add_up()

#-----------------------------


#-----------------------------
#Scope
#-----

# light = False

# def light_switch():
#     if light:
#         print("Whoah it's bright")        #   the variable 'light' is outside
#         light = False                     #       the scope of the function
#     else:
#         print("Whoah it's dark")
#         light = True

# light_switch()
# light_switch()

# light = False

# def light_switch():
#     global light
#     if light:
#         print("Whoah it's bright")          #   Now we tell the function to use
#         light = False                       #       the variable light in the global
#     else:                                   #           scope
#         print("Whoah it's dark")
#         light = True

# light_switch()
# light_switch()


# balance = 100

# def cash_withdraw(amount):
#     global balance
#     print(f"Your balance is {balance}")
#     print(f"You are withdrawing {amount}")
#     balance -= amount
#     print(f"Your new balance is {balance}")

# cash_withdraw(50)

#------------------------------


#------------------------------
#Lists and Tuples
#----------------

# list1= [
#     "Entry1",
#     "Entry2",                           #   Lists can be changed or mutated
#     "Entry3"
# ]

# tuple1= (
#     "Entry1",
#     "Entry2",                           #   Tuples are concrete and can't be mutated
#     "Entry3"
# )


# even_nums = [2, 4, 6, 8, 10]                #   List
# odd_nums = (1, 3, 5, 7, 9)                  #   Tuple

# even_nums.append(12)                        #   Making changes to the list
# even_nums.insert(0, 0)                      #       no problem

# # for i in even_nums:
# #     print (i)

# # odd_nums.remove(1)                        #   Making changes to
# # odd_nums.pop(1)                           #       tuples no way hose

# #-----------------------


# #-----------------------
# #Slicing Lists
# #-------------

# list_of_fruits = [
#     "apples",
#     "bananas",
#     "oranges",
#     "cherry",
#     "mango",
#     "grapes",
#     "pineapple",
#     "tomato",
# ]

# print(list_of_fruits[1:7])                  #   This will print the list items only between index position 1 and 7

# print(list_of_fruits[0:8:2])                #   This will print the list between 0 and 8 but only every second item

#-------------------------------


#-------------------------------
#While True
#----------

num = 0

while num < 10:
    print(num)
    num += 1


