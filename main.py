#Name: Nwobi Golibe
#This is a program that calculates the area and perimeter of a triangle
#Firstly, we need to import the math module
import math

# Then we print the name and purpose of the program
print("Name: Nwobi Golibe")
print("Purpose of the Program: Calculate the perimeter and area of a triangle")

# Now we will take the inputs for the three sides of the triangle
length1 = float(input("Enter the length of side 1: "))
length2 = float(input("Enter the length of side 2: "))
length3 = float(input("Enter the length of side 3: "))

# Now we calculate the perimeter
perimeter_of_the_triangle = length1 + length2 + length3

# Since the triangle is not said to be a right-angled triangle, we can't use (base * height)/2
# Instead we will use a formula that can always calculate the area of a triangle, Heron's Formula
# Now we calculate the semi-perimeter
semi_perimemter_of_triangle = perimeter_of_the_triangle / 2

# Now we use Heron's formula to actually calculate the area of the triangle
area_of_the_triangle = math.sqrt(semi_perimeter_of_triangle * (semi_perimemter_of_triangle - length1) * (semi_perimemter_of_triangle - length2) * (semi_perimemter_of_triangle - length3))

# These are the results of the calculations
print(f"The perimeter of the triangle is= {perimeter:.2f}")
print(f"The area of the triangle is= {area:.2f}")
