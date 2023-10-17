#space with equal
name:str = "talha"
education: str = "Bscs"

# multiline strings with triple """
card : str = """ 
Card
Name :
Age :
"""

# F-string - directly convert to string-any expression inside {} - latest version
new_card : str = f""" 
Card
Name : {name}
Education : {education}
"""

# .format()

first =2
second = 1
print(" a is {} and b is {}".format(first,second))

info : str = """a is {b} and b is {a}
""".format(a=first,b=second)
print(info)

###################

student_code : str = """ 
print("Hello")
print("Word")
"""

exec(student_code)
