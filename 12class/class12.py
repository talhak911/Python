studentsList:list[dict]=[]
class Student():
    def __init__(this,name:str,age:int) -> None:
        this.newvariable = 12
        if age <18 or age >65:
            raise StudentAgeError("You are not eligible for this program")
        else:
            this.name=name
            this.age=age
            std:dict={"name":this.name,"Age":this.age}
            studentsList.append(std)

 
class StudentAgeError(Exception):
    pass

try:
    def addStudent()->None:
        name:str =input("Enter your name ")
        age:int =int(input("Enter your age "))
        newEntry = Student(name,age)
    print("Welcome to University !")
    flag =True
    while flag:
        addOrNot=input("Want to add student? (y/n) ")
        if addOrNot.lower() == "y":
            addStudent()   
        else:
            flag = False
        

except Exception as E:
    print("Error : ",E)
print(f"List of all eligible students",studentsList)