# This is a sample password generator in Python

import sys

import passwd_create
import passwd_strength

while True:
    try:
        if len(sys.argv) > 1 and sys.argv[1].isdecimal():
            tam = int(sys.argv[1])
        else:
            tam = int(input("Enter size of password: "))
            if tam < 4:
                print("Smallest number of accepted digits is 4")
                continue
            else:
                break
        break

    except ValueError:
        print("That is not a valid integer number")

list_all_char = passwd_create.generate_ascii_list(33, 127)  # define ascii size

# parameters
uppercase = True  # set as required uppercase
lowercase = True  # set as required lowercase
special = True  # set as required special char
number = True  # set as required number
parameters = [uppercase, lowercase, number, special]

new_password = passwd_create.generate_password(tam, list_all_char, parameters)  # define size of passwd and valid chars

print("\n[Password]\n[*] %-25s %s\n" % ("Generated password:", new_password))

print(passwd_strength.calc(new_password))

del new_password  # clear new_password
