#!/usr/bin/envpython3
# Created By:Deepak
# Date: 10/27/2026
# This program tells you if your character is a upper or lower case and converts it

import constants

def main():

    user_letter = input("Enter a single letter: ")

    if len(user_letter) != 1:
        print("Please enter only one letter.")

    else:

        counter = 0
        found_letter = False

        while counter < 26:

            if user_letter == constants.UPPERCASE[counter]:
                print(f"{user_letter} is uppercase.")
                print(f"Converted to lowercase: {constants.LOWERCASE[counter]}")
                found_letter = True

            elif user_letter == constants.LOWERCASE[counter]:
                print(f"{user_letter} is lowercase.")
                print(f"Converted to uppercase: {constants.UPPERCASE[counter]}")
                found_letter = True

            counter += 1

        if found_letter == False:
            print("Invalid character.")

if __name__ == "__main__":
    main()