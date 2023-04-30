





def display_main_menu():
    print("Key in numbers separated by commas = ")
    x = get_user_input()
    calc_average(x)
    find_min_max(x)
    calc_median_temperature(x)

def get_user_input():
    temp = input()
    values = temp.split(",")
    x = []
    for y in values:
        x.append(float(y))
    print (x)
    return (x)


def calc_average(x):
    Average = sum(x)/len(x)
    Average = round(Average)
    print("\nYour average is = ", Average)

def find_min_max(x):
    x.sort()
    print("\nMinimum value is", x[0])
    print("Maximum value is", x[-1])


def calc_median_temperature(x):
    x.sort()
    odd_even = (len(x) % 2)
    if odd_even == 1: #check if it's an lord number
        y = ((len(x)+1)/2)
        y = int(-y)
        print (x[y])

    elif odd_even == 0: #check if it's an even number
        y = (len(x)/2)
        y = int(-y)
        print((x[(y)]+x[(y-1)])/2)

display_main_menu()

