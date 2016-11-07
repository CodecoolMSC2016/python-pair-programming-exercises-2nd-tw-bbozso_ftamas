import string
import random

def passwordgen():
    lowercaselist = list(string.ascii_lowercase)
    uppercaselist = list(string.ascii_uppercase)
    digitlist = list(string.digits)
    symbolslist = list(str("!@#$%^&*()?"))
    passwordlist = lowercaselist + uppercaselist + digitlist + symbolslist
    lenght = random.randint(8, 16)


    password = random.sample(passwordlist, lenght)
    
    print("Your password is: ")
    print("".join(password))
    password = str(password)
    
    return password

def main():
    passwordgen()
    while True:
        again = input("Do you want a new password?(y,n): ")
        if again == "y":
            passwordgen()
        
        else:
            return


if __name__ == '__main__':
    main()
