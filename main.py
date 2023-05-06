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
        break
    except ValueError:
        print("That is not a valid integer number")

list_all_char = passwd_create.generate_ascii_list(33, 127)  # define ascii size

# parameters
uppercase = True
lowercase = True
special = True
number = True

new_password = passwd_create.generate_password(tam, list_all_char)  # define size of passwd and valid chars

print("\n[Password]\n[*] %-25s %s\n" % ("Generated password:", new_password))

print(passwd_strength.calc(new_password))

del new_password  # clear new_password
