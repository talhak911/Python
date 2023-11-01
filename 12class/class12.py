studentsList:list[dict]=[]
class Student():
    def __init__(self,name:str,age:int) -> None:
        if age <18 or age >65:
            raise StudentAgeError("You are not eligible for this program")
        else:
            self.name=name
            self.age=age
            std:dict={"name":self.name,"Age":self.age}
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