import arithmetic as ar
import geometry as geo

print("Hello Everone!!")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

ar.sum(a, b)
ar.subtract(a, b)

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
geo.calc_rect_area(length, breadth)
geo.calc_rect_perimeter(length, breadth)