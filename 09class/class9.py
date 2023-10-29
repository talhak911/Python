
import sys
a : int = 1
print("First assignment address of int variable a ",id(a))
b=a
print(f"b=a ,  value {b} address of b ",id(b))
b=10
print("b=10 ,  address of b",id(b))
print(f"value {a} ,  address of a ",id(a))
print("Start")

print(type(sys.argv)) 

if sys.argv[1] == '-g':
    print("Installing package globally")

print(sys.argv) # iterative data type list[str] 0=filename **value user define