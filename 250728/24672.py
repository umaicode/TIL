def correct_domain(str):
    if str.find("@"):
        print(str[str.find("@") + 1 : :])
    else:
        print("Invalid email")


str = input()
correct_domain(str)
