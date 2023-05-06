import secrets
import string

def generate_ascii_list(x, y):
    ascii_list = []
    for i in range(x, y):
        if i == 96:  # Remove "`", invalid ascii character in passwords
            continue
        ascii_list += chr(i)
    return ascii_list


def generate_random_char(char_list):
    random_char = secrets.randbits(128) % len(char_list)
    return random_char


def generate_password(tam, char_list, parameters):
    parameter = False
    while (parameter != True):
        decimal_type = upper_type = lower_type = special_type = 0
        password = ""
        for i in range(tam):
            number_pass = generate_random_char(char_list)
            chargen_password = str(char_list[number_pass])
            password += chargen_password
            if chargen_password.isdecimal():
                decimal_type += 1
            elif chargen_password.isupper():
                upper_type += 1

            elif chargen_password.islower():
                lower_type += 1

            elif chargen_password in string.punctuation:
                special_type += 1

        if sum([special_type>0, lower_type>0, upper_type>0, decimal_type>0]) == 4:
            parameter = True
        else:
            parameter = False
    return password
