
age = input("Please enter your age: \n")
try:
    age = int(age)
except:
    age = input("Please enter a valid age: \n")
    age = int(age)


if age>10:
        lang = input("Do you speak english or spanish(Yes/No)")
        if lang == "Yes":
            print("You can create an account")
        elif lang =="No":
            print("You can create an account")

else:
    print("You can't create an account")


