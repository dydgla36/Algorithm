x = int(input())
def factorial(y):
    if y == 1 or y == 0:
        return 1
    else:
        return (y * factorial(y-1))
print(factorial(x))