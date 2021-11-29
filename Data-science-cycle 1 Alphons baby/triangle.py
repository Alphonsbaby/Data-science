def checkTriangle(x, y, z):

    if x == y == z:
        print("Equilateral Triangle")


    elif x == y or y == z or z == x:
        print("Isosceles Triangle")


    else:
        print("Scalene Triangle")

x = input("enter the first side")
y = input("enter the second variable")
z = input("enter the third variable")

checkTriangle(x, y, z)