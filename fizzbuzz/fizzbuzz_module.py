def fizzbuzz(number):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        else:
            i = i
        print(i)
    return


def main():
    for i in range(1,101):
        fizzbuzz(number)
        break

number = range(1, 101)

if __name__ == '__main__':
    main()
   