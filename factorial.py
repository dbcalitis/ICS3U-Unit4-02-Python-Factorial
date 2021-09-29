#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program is a the factorial program


def main():
    # This function multiplies all numbers 1 to the given number (factorial)
    """the list of factorial products starts
    with 1 because 0! = 1"""
    # If these variables down below are 0, the product will always be 0.
    loop_counter = 1
    product = 1

    # input
    user_input = input("Enter a positive number: ")

    # process & output
    try:
        user_input = int(user_input)

        if user_input < 0:
            print("You did not enter a positive number.")
        else:
            while loop_counter <= user_input:
                product *= loop_counter
                loop_counter += 1
            print("{0}! = {1}".format(user_input, product))
    except (Exception):
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
