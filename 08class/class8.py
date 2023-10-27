from typing import Union
key = Union[str,int]
value = Union[str,int,set,list, dict, tuple]
data: dict[key,value] = {"name":"Talha"
                         , "fname":"sadiq",
                         "Hobby":{1:"cricket",2:"gardening"}
                         }

print(data["Hobby"][2])

numbers : list[int]= list(range(1,21))
print("List of even numbers")
for n in numbers:
    
    if n %2 ==0:
        print(n)
print("List of odd numbers")   
     
for n in numbers:    
    if n%2!=0:
        print(n)
for n in numbers:
    for m in range(1,11):
        print(f"{n} x {m} = {n*m}")