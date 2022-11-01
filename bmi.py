def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight / (height * height)
    print("BMI = " + str(BMI))

    if BMI < 18.5:
        print("User is underweight")
        return -1
    elif 18.5 <= BMI <= 25.0:
        print("User has normal weight")
        return 0
    else:
        print("User is overweight")
        return 1


value = calculate_bmi(weight=57, height=1.73)
print(value)