import math
for i in range(4):
    n = 0
    n = int(input("Введите число: "))
    if n<0:
        print("Error. Try again")
    else:
        n = math.sqrt(n)
        print(n)