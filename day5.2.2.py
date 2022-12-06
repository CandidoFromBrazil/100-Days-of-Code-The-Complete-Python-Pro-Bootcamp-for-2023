#BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_cast = float(height)
weight_cast = int(weight)

BMI = weight_cast / (height_cast**2)
BMI_cast = int(BMI)
print(BMI_cast)
