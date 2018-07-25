height = float(input("Your height in centimet?"))
weight = float(input("Your weight in kilogram?"))
heightm = height/100
bmi = weight/(heightm**2)
print("Your BMI is",bmi)
if bmi < 16:
    print("You are severely underweight.")
elif 16 < bmi < 18.5:
    print("You are underweight.")
elif 18.5 < bmi < 25:
    print("You are normal.")
elif 25 < bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")