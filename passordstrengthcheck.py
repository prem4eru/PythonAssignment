#Create a Python script to check the password strength ,  Python function called check_password_strength that takes a password string as input
# Definining the check_password_strength fun
def check_password_strenght(password):
    upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
    length = len(password)
#Checking the condition password should be 8 characters long
    if (length < 8):
        print("Password must be at least 8 characters long!\n")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].islower()):
                lowerChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1
#We are checking condition whether all type of chars are given or not
    if(upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 10):
            print("The strength of password is strong.\n")
            return True
        else:
            print("The strength of password is medium.\n")
            return True
    else:
        if (upperChars == 0):
            print("Password must contain at least one uppercase character!\n")
        if (lowerChars == 0):
            print("Password must contain at least one lowercase character!\n")
        if (specialChars == 0):
            print("Password must contain at least one special character!\n")
        if (digits == 0):
            print("Password must contain at least one digit!\n")


password = input("Please enter password: ")
#calling the check_password_strength fun
print(bool(check_password_strenght(password)))