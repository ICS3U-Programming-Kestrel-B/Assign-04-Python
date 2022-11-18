#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 11, 2022
# This program prints the 0X9
# multiplication tables using
# a while loop and if statements


def main():
    # introductory paragraph
    print("This program prints the 0X9")
    print("multiplication tables using")
    print("a while loop and if statements")
    print("")

    # initializing num1
    num1 = 0

    # initializing num2
    num2 = 0

    start = input("Enter Y to start program: ")

    # starting do while loop
    while start == "Y":
        # calculating product
        product = num1 * num2

        # displaying to user
        print(("{} X {} = {}").format(num1, num2, product))

        # updating counters
        if num2 < 9:
            num2 = num2 + 1
        else:
            num2 = 0
            num1 = num1 + 1

        # checking if program should end
        if num1 > 9:
            break


if __name__ == "__main__":
    main()
