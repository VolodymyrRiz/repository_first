import math
try:
    a1 = int(input("Enter coefficient a: "))
    a1 = bool(a1)
   
except ValueError:
    print("Введіть число")
try:
    b1 = input("Enter coefficient b: ")
    b1 = bool(b1)
except ValueError:
    print("Введіть число")
try:
    c1 = input("Enter coefficient c: ")
    c1 = bool(c1)
except ValueError:
    print("Введіть число")
while not a1 or not b1 or not c1:
    if not a1:
        print("Введіть число ")
        a1 = input("Number ")
        if not b1:
            print("Введіть число ")
            b1 = input("Number ")
            if not c1:
                print("Введіть число ")
                c1 = input("Number ")
           
a = int(a1)
b = int(b1)
c = int(c1)
D = b ** 2 - 4 * a * c

if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    print(x1)
else:
    D = D * -1
    v = math.sqrt(D)
    x2 = (-b - v) / (2 * a)
    print(x2)