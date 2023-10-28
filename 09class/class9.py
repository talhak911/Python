import sys

print("Start")

print(type(sys.argv)) 

if sys.argv[1] == '-g':
    print("Installing package globally")

print(sys.argv) # iterative data type list[str] 0=filename **value user define