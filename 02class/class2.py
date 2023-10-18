#space with equal
name:str = "talha"
education: str = "Bscs"

# multiline strings with triple """
card : str = """ 
Card
Name :
Age :
"""

# F-string - directly convert to string-any expression can be inside {} - latest version
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


################# second index #### first
info1 : str = """a is {1} and b is {0}
""".format(2,3)  #### (first,second...)
print(info1)


info2 : str = """a is {} and b is {}
""".format(2,3)
print(info2)


###################

student_code : str = """ 
print("Hello")
print("Word")
"""

exec(student_code)
