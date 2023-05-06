# I am using this incredible project for this purpose:
# https://github.com/0xZDH/passwd-strength
# With small modifications. Thank you, Mr. 0xZDH

# This is assuming 1277 MH/s (1.277.000.000.000 passwords/second) < Default - can be changed by user
# This baseline is based on the following cracking configuration:
#     10 x GeForce RTX 3090 GPUs
#     Hashtype: NTLMv2
# Test password: P4$sword

from __future__ import division

import re
import sys


def calc(password):
    print("\n"+'-'*25+"\n\n[Security]\n%s \n" % ("Checking password cracking time using brute force:"))
    entropy = 0
    crack_speed = 1277000000000  # Default

    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            crack_speed = int(sys.argv[1])

    policies = {'Uppercase characters': 0,
                'Lowercase characters': 0,
                'Special characters': 0,
                'Numbers': 0}

    entropies = {'Uppercase characters': 26,
                 'Lowercase characters': 26,
                 'Special characters': 33,
                 'Numbers': 10}

    pass_len = len(password)

    for char in password:

        if re.match("[0-9]", char):
            policies["Numbers"] += 1

        elif re.match("[a-z]", char):
            policies["Lowercase characters"] += 1

        elif re.match("[A-Z]", char):
            policies["Uppercase characters"] += 1

        else:
            policies["Special characters"] += 1

    del password

    print("\n[+] %-25s %d\n" % ("Password length:", pass_len))

    for policy in policies.keys():

        num = policies[policy] if policies[policy] > 0 else '-'
        print("[+] %-25s %s" % (policy + ":", str(num)))

        if policies[policy] > 0:
            entropy += entropies[policy]

    print("\n[+] %-25s %d" % ("Password entropy:", entropy))

    # Calculate the time to crack
    time_ = "hours"
    cracked = ((entropy ** pass_len) / crack_speed) / 3600

    if cracked > 24:
        cracked = cracked / 24
        time_ = "days"

    if cracked > 365:
        cracked = cracked / 365
        time_ = "years"

    if time_ == "years" and cracked > 100:
        cracked = cracked / 100
        time_ = "centuries"

    if time_ == "centuries" and cracked > 1000:
        cracked = cracked / 1000
        time_ = "millennia"

    return "\n[+] Time to crack password:   {:,.2f} {}".format(cracked, time_)
