#name_age()
name = input("Enter your name:")
age = input("Enter your age:")
print(f"Hello {name}. Your age is: {age}.")

#swap_integers(num1, num2)
x = input ("Enter value of x:")
y = input ("Enter value of y:")

temp = x
x = y
y = temp

print("Let's turn that around!")

print("x = {}".format(x))
print("y = {}".format(y))


#check_numbers(num1, num2)

def check_numbers(num1, num2):
    if num1 % 6 == 0 or num2 % 6 == 0:
        print("At least one number is divisible by 6.")
    elif num1 % 10 == 0 and num2 % 10 == 0:
        print("Both numbers are divisible by 10.")
    else:
        return False

#sum_up(num1,num2)

def sum_up(num1,num2):
    if num1 > num2:
        return False
        print("zero")
    if num1 < 0:
        return False
        print("zero")
    if num2 < 0:
        return False
        print("zero")
    else:
        sum(range(num1,num2))


#check_string(text)
text = input("Type in a word:")

def check_string(text):
    if str.startswith("a"):
        return True
    elif str.endswith("a"):
        return True
    else:
        return False

check_string(text)


#triangle(rows)

rows = int(input("How many rows should your triangle have?"))

def triangle(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("* ", end="")
        print("\n")