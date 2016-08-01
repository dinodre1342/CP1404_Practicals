#Function

#Built in Function
print("abc")
x = int ("67")
print (x)

def get_user_input(message):


def check_calorie(num_of_fries, num_of_cookies):
    calories_fries = 100
    calories_cookies = 70

    total_calories = num_of_fries *calories_fries + num_of_cookies * calories_cookies
    print ("The total calories are: {:}".format(total_calories))

    if total_calories > 500:
        return "Watch your diet!!!"
    elif total_calories > 300:
        return "You are at brderline."
    else:
        return "You are pretty safe!"

fries = get_user_input("Enter num of fries:")
cookies = get_user_input("Enter num of cookies:")
#first way of handling the return, use it directly
print(check_calorie(fries, cookies))

check_calorie(2, 3)
check_calorie(10, 5)