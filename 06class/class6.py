from typing import Union, Optional
# optional have by default None or it  can have str
# percentage:int | float= int(input("Enter your percentage "))
name : Optional[str]=None
percentage: Union[int,float] = int(input("Enter your percentage "))
grade : Union[None, str]=None
if percentage >=80:
    grade = "A+"
elif percentage >=70:
    grade = "A"
elif percentage >=60:
    grade = "B"
elif percentage >=50:
    grade = "C"
elif percentage >=40:
    grade = "D"
elif percentage >=33:
    grade = "E"
else:
    grade = "F"
print(f"Dear student your grade is {grade}")
