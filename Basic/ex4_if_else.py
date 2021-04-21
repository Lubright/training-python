height = float(input("請輸入球員的身高(cm): "))
weight = float(input("請輸入球員的體重(kg): "))
bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi > 30:
    print("Obese")
elif (bmi >= 18.5) and (bmi < 25):
    print("Normal weight")
else:
    print("Overweight")
