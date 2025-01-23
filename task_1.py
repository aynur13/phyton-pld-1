import math

def is_valid_triangle(a, b, c):
  
    return (a + b > c) and (a + c > b) and (b + c > a)

def calculate_area(a, b, c):
  
    s = (a + b + c) / 2
  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input(" 1 "))
b = float(input(" 2 "))
c = float(input(" 3 "))


if is_valid_triangle(a, b, c):
    
    area = calculate_area(a, b, c)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The given sides do not form a valid triangle.")
