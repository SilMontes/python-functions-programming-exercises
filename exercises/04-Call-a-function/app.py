import math
def calculate_area(length,edge):
	return length * edge

# Your code Below this line:
square_area1=calculate_area(4,4)
square_area2=calculate_area(2,2)
square_area3=calculate_area(5,5)

def volum_Sphere(radio):
   return int((4.0/3.0)*math.pi*radio**3) #el .0 no es necesario ni los parentesis

volum_Sphere_Total=volum_Sphere(2)
print(volum_Sphere_Total)

def triangle_area(base, heigth):
    a=(base*heigth)/2
    return a
triangle_area_result=triangle_area(2,4)
print(int(triangle_area_result))

#functions with keyword arguments. An important remider is that the required or not given (without initial value) or non_defautl arguments shoud go after the default argumets, also known as keywords arguments. And if you want to modified the value of the default argument you have to specified its name when the function is been call
def centimeters(feet=0, inches=0):
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54 
    return inches_to_cm+feet_to_cm
print("Results")
print(centimeters(feet=5)) #convertion from feets to centimeters
print(centimeters(inches=70)) #convertion from inches to centimeters
print(centimeters(feet=5, inches=8)) #convertion from inches and feets to centimeters

