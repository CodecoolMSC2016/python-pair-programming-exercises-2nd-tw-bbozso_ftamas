import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def listoverlap(list1, list2):
    c = []
    for i in a and b:  
        if i in a and i in b:
            c.append(i)
    print(c)
    return


def main():
    listoverlap(a, b)
    return


if __name__ == '__main__':
    main()
