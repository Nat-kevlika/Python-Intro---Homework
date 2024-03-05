import math

#the sides of the triangle: a, b, c; 
#perimeter : p = a + b + c;
#area of the triangle: A = sqrt(s*(s - a)*(s - b)*(s - c)), where s = (a+b+c)/2

a = float(input("The length of side a : "))
b = float(input("The length of side b : "))
c = float(input("The length of side c : "))

p = a + b + c
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("perimeter of the triagle is: ", p)
print("area of the triangle is: ", area)

