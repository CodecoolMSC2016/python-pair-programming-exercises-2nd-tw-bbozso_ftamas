def palindrome(str):
    str = str.lower()
    str = "".join(str.split())
    
    forward_list = []
    backward_list = []
    
    
    forward_list = list(str)
    backward_list = list(reversed(forward_list))
    
    if forward_list == backward_list:
        return True
    else:
        return False 


def main():
    
    str = input("What's your string?: ")
    if palindrome(str):
        print("This is a palindrome")
    else:
        print("No palindrome")


if __name__ == '__main__':
    main()

