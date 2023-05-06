import secrets


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


def generate_password(tam, char_list):
    password = ""
    for i in range(tam):
        number_pass = generate_random_char(char_list)
        password += char_list[number_pass]
    return password
