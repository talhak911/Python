from mypackage.talha import ExecutionTimer
@ExecutionTimer
def square(numbers:list[int]):
    return [i**2 for i in numbers]
square(list(range(10)))
