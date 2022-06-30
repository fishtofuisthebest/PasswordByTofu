minLength = 6
maxLength = 12
passWord = input("please enter a new password: ")

passWordLength = len(passWord)

if passWordLength < minLength:
    print("your password is " + str(passWordLength) + " characters long")
    print("your password is too short")
    print("your password has to be greater than or equal to 6 characters")

if passWordLength > maxLength:
    print("your password is " + str(passWordLength) + "characters long")
    print("your password is too long")
    print("your password has to be less than or equal to 12 characters")

if (passWordLength >= minLength) and (passWordLength <= maxLength):
    print("thank you for making a strong password")

