import math
print("input the lenghts of the sides of the triangle")
a=float(input("side A "))
b=float(input("side B "))
c=float(input("side C "))
p=a+b+c
print("The perimeter is", p)
if a**2+b**2==c**2:
    area1=a*b/2
    print("This is a right triangle with an area of", area1)
elif a**2==b**2+c**2:
    area2=b*c/2
    print("This is a right triangle with an area of", area2)
elif a**2+c**2==b**2:
    area3=a*c/2
    print("This is a right triangle with an area of", area3)
elif a==b==c:
    h1=math.sqrt(a**2-(a/2)**2)
    area4=a*h1/2
    print("This is a equilateral triangle with an area of", area4)
elif a==b!=c:
    h2=math.sqrt(a**2-(c/2)**2)
    area5= c*h2/2
    print("This is a isosceles triangle with an area of", area5)
elif a!=b==c:
    h3 = math.sqrt(b ** 2 - (a / 2) ** 2)
    area6 = a * h3 / 2
    print("This is a isosceles triangle with an area of", area6)
elif a==c!=b:
    h4 = math.sqrt(a ** 2 - (b / 2) ** 2)
    area7 = b * h4 / 2
    print("This is a isosceles triangle with an area of", area7)
else:
    t=p/2
    area8=math.sqrt(t*(t-a)*(t-b)*(t-c))
    print("This is a scalene triangle with an area of", area8)
