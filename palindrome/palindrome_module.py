def palindrome(str):
    forward_list = []
    backward_list = []
    
    
    forward_list = list(str)
    backward_list = list(reversed(forward_list))
    if forward_list == backward_list:
        print(True)
    else:
        print(False)
    
   
    return


def main():
    string = input("Write me a string!: ").lower()
    string = "".join(string.split())
    palindrome(string)
    return


if __name__ == '__main__':
    main()

