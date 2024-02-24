# Punto 1
age = 18

# Punto 2
hight = 1.62

# Punto 3
compejo = 1j

# Punto 4
base = int(input("Enter base: "))
alt = int(input("Enter hight: "))
at = int(0.5 * base * alt)
print("The area of the triangle is : ", at)

# Punto 5
lade_a = int(input("Enter side a: "))
lade_b = int(input("Enter side b: "))
lade_c = int(input("Enter side c: "))
perimeter = lade_a + lade_b + lade_c
print("The perimeter of the triangle is: ", perimeter)

# Punto 6
leng = int(input("Enter lenght: "))
wid = int(input("Enter width: "))
area = leng * wid
peri = 2 * ( leng * wid )
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", peri)

# Punto 7
r = int(input("Enter r value: "))
area = 3.14 * r * r
circun = 2 * 3.13 * r
print("The area of the circle is: ", area)
print("The circunference of the circle is: ", circun)

# Punto 8
x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
intercep = (2 * x) - 2
print("X:", intercep)
intercep = (2 * y) - 2
print("Y:", intercep)

# Punto 9
x1 = int(input("Enter X1 value: "))
x2 = int(input("Enter X2 value: "))
y1 = int(input("Enter Y1 value: "))
y2 = int(input("Enter Y2 value: "))
m = x1 - x2 
print("X:", m)
print( intercep == m )
m = y1 - y2 
print("Y:", m)
print( intercep == m )

# Punto 10
x = int(input("Enter X value: "))
x1 = int(input("Enter X1 value: "))
x2 = int(input("Enter X2 value: "))
intercep = (2 * x) - 2
print("X:", intercep)
m = x1 - x2 
print("X:", m)
print( intercep == m )

y = int(input("Enter Y value: "))
y1 = int(input("Enter Y1 value: "))
y2 = int(input("Enter Y2 value: "))
intercep = (2 * y) - 2
print("Y:", intercep)
m = y1 - y2 
print("Y:", m)
print( intercep == m )

# Punto 11
x = int(input("Enter X value: "))
slope = ((x ** 2) + (6 * x) + 9)
print("Slope value:", slope)

# Punto 12
a = "python"
b = "dragon"
print(len(a) != len(b))

# Punto 13
print("on is in python and dragon:", "on" in "python" and "on" in "dragon")

# Punto 14
print("I hope this course is not full of jargon:", "on" not in "I hope this course is not full of jargon")

# Punto 15
print("on is in python and dragon:", "on" not in "python" and "on" not in "dragon")

# Punto 16
long = len("Python")
long_float = float(long)
long_str = str(long_float)
print(type(long))
print(type(long_float))
print(type(long_str))

# Punto 17
num = int(input("Enter a number: "))
num = num % 2
print("El numero es par:", num == 0)

# Punto 18
enterger = int(2.7)
div = 7 / 3
print("The afirmartion is:", div == enterger)

# Punto 19
print("type of '10' is equal to type of 10:", type('10') == type(10))

# Punto 20
print("int('9.8') is equal to 10:", int(9.8) == 10)

# Punto 21
hours = int(input("Enter the hours: "))
per_hour = int(input("enter rate per hour: "))
pay = (hours * per_hour) * 5
print("Your weekly earning is:", pay)

# Punto 22
years = int(input("Enter number of years you have lived: "))
seconds = years * 31449600
print("You have lived for (",seconds,") seconds.")

# Punto 23
print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")
