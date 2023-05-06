import string

from passlen import len_iters_random
import random as rn


def password_gen():
    size_alloc = input("enter 'm' for manual and 'a' for auto:")

    if size_alloc == 'm':
        size_num = int(input("Enter the number of numerics in the password:"))
        size_lower = int(input("Enter the number of lowercase alphabets in the password:"))
        size_upper = int(input("Enter the number of uppercase aplhabets in the password:"))
        size_special = int(input("Enter the number of special characters in the password:"))
    elif size_alloc == 'a':
        size_password = int(input("Enter password length:"))
        size_num, size_lower, size_upper, size_special = len_iters_random(size_password)
    else:
        print("Invalid")

    password_list = []

    numbers = list(string.digits)
    lower_alphabets = list(string.ascii_lowercase)
    upper_alphabets = list(string.ascii_uppercase)
    special_characters = list(string.punctuation)

    # for a in (lower_alphabets, upper_alphabets, special_characters):
    #     for b in (size_lower, size_upper, size_special):
    #         for c in range(1, (b + 1)):
    #             password_list.append(rn.choice(a))
    #         break
    #
    # for i in range(1, (size_num + 1)):
    #     password_list.append(str(rn.choice(numbers)))
    # rn.shuffle(password_list)
    # # global password
    password = ''.join(password_list)

    print(password)


password_gen()
