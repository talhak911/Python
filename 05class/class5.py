names : list[str] = ["Sir Zia","Muhammad qasim", "Dr noman"]
for name in names:
    print(f"Welcome Dear Teacher {name.title()}")
print("Team PIAIC")

print("new program")
numbers = list([i for i in range(1,11)])
squareEven: list[int]=[]
for number in numbers:
     print(f"square of {number} is {number**2}")
    
for number in numbers[1::2]:
    print(f"square of even number {number} is {number**2}")
    squareEven.append(number**2)
print("List of even numbers",squareEven)

