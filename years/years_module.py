import datetime



def years(age):
    difference = 100 - int(age)
    this_year = datetime.date.today()
    years100 = int(this_year.year) + difference
  

    return years100


def main():
    
    name = input("What's your name?: ")
    age = input("How old are you?: ")
    
    years(age)

    print("Hello", name, "you will be 100 years old in the year: ", years(age))
        
    return


if __name__ == '__main__':
    main()
