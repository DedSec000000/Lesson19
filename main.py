
for x in range(10):  # starts at 0 and finishes at 9.
    print(x)  # this line is repeated starting at 0 and finishing at 9

for x in range(5):  # it prints hello five times.
    print("Hello")

for x in range(1,11):  # it prints the square numbers, starting at 1 and ending at 100.
    print(x,"squared is", x**2)

for x in range(1,51):  # it prints the even numbers starting at 1 and ending on 100.
    print(2*x)

total = 0
for x in range(1,101):  # it prints the program to calculates 1+2+3..........+99+100
    total += x
print(total)

p = 1
for x in range(1,6):  # it prints the program to calculates 1*2*3*4*5
    p *= x
print(p)

def factorial(x):
    p = 1
    for x in range(1,x+1):
        p *= x
    return(p)

for x in "stephen":
    print(x)

name = ""
sign = -1
for x in "stephen":
    sign *= -1
    if sign == 1:
        name += x.upper()
    else:
        name += x.lower()
print(name)



