names : list [str] = []
names.append("Talha")
print(names)
loop:bool= True
print("Welcome to Calculator")
while loop == True:
    a = input("Enter first number ")
    o = input("Select operation + - * /  ")
    b = input("Enter second number ")
    if o == "+":
        print(f"{a} {o} {b} = {int(a)+int(b)} ")
    elif o == "-":
        print(f"{a} {o} {b} = {int(a)-int(b)} ")
    elif o == "*":
        print(f"{a} {o} {b} = {int(a)*int(b)} ")
    elif o == "/":
        if b =="0":
            print("can't divide by zero")
        else:
            print(f"{a} {o} {b} = {int(a)/int(b)} ")
    res = input("Want to perform another operation type (y/n)")
    if res.lower() !="y":
        loop = False