
WeightClass = ["Under weight", "Normal weight", "Over weight"]

def calculate_bmi(height, weight):
    print("Height = " + str(height) + "m")
    print("Weight = " + str(weight) + "kg")
    print("Your weight is %skg and you are %scm tall" % (weight, height))
    print("Your accurate weight is %.2fkg" % (weight))



    print(f"Your weight is {weight}kg.")
    BMI = weight / (height * height)
    print(str(BMI))

    if BMI < 18.5:
        print("wow bamboo, ure " + WeightClass[0])

    elif BMI < 18.5 and BMI > 25.0:
        print("boring, you're " + WeightClass[1])

    elif BMI > 25:
        print("OMEGA CHUNGGUS LOL U ARE " + WeightClass[2])


calculate_bmi(weight = 70, height = 1.8)



Money = {"$2": 5, "$1": 23,}

print(f"{Money['$2']} $2 notes and {Money['$1']} $1 coins.")