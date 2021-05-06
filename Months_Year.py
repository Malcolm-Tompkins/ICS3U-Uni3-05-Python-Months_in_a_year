#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 5, 2021
# Program checks which month the user's number corresponds with


def main():
    # Function that checks the month

    # User input
    print("Input a number 1-12 to correspond to a month of the year")
    user_number = int(input("Input your number from 1-12: "))
    # Process
    if user_number == 1:
        print("January")
    elif user_number == 2:
        print("Febuary")
    elif user_number == 3:
        print("March")
    elif user_number == 4:
        print("April")
    elif user_number == 5:
        print("May, my birthday month!")
    elif user_number == 6:
        print("June")
    elif user_number == 7:
        print("July")
    elif user_number == 8:
        print("August")
    elif user_number == 9:
        print("September")
    elif user_number == 10:
        print("October")
    elif user_number == 11:
        print("November")
    elif user_number == 12:
        print("December")
    else:
        print("An error has occured")
        print("Make sure what you entered is a number between 1 and 12")


if __name__ == "__main__":
    main()
