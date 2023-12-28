import random
import signs


def generate_password(random_signs_list, random_password):
    """Generates a random password"""
    for sign in random_signs_list:
        random_password += sign
    print(f"Your random password: {random_password}")


end_of_program = False
while not end_of_program:
    num_options = 0
    list_options = []
    random_signs = []
    password = ""

    try:
        signs_amount = int(input("How many signs do you want in your password?: "))
    except ValueError:
        print("Type a number!")
        continue

    while signs_amount <= 0:
        print("Your password needs at least one sign!")
        signs_amount = int(input("How many signs do you want in your password?: "))

    lowercase = input("Do you want lowercase letters in your password? "
                      "Type 'y' for Yes, or any other key for No: ").lower()

    uppercase = input("Do you want uppercase letters in your password? "
                      "Type 'y' for Yes, or any other key for No: ").lower()

    digits = input("Do you want digits in your password? Type 'y' for Yes, or any other key for No: ").lower()

    symbols = input("Do you want other symbols in your password? "
                    "Type 'y' for Yes, or any other key for No: ").lower()

    if lowercase == "y":
        num_options += 1
        list_options.append("lowercase")
    if uppercase == "y":
        num_options += 1
        list_options.append("uppercase")
    if digits == "y":
        num_options += 1
        list_options.append("digits")
    if symbols == "y":
        num_options += 1
        list_options.append("symbols")

    while num_options == 0:
        print("You have to choose at least one option!")
        lowercase = input("Do you want lowercase letters in your password? "
                          "Type 'y' for Yes, or any other key for No: ").lower()

        uppercase = input("Do you want uppercase letters in your password? "
                          "Type 'y' for Yes, or any other key for No: ").lower()

        digits = input("Do you want digits in your password? Type 'y' for Yes, or any other key for No: ").lower()

        symbols = input("Do you want other symbols in your password? "
                        "Type 'y' for Yes, or any other key for No: ").lower()

        if lowercase == "y":
            num_options += 1
            list_options.append("lowercase")
        if uppercase == "y":
            num_options += 1
            list_options.append("uppercase")
        if digits == "y":
            num_options += 1
            list_options.append("digits")
        if symbols == "y":
            num_options += 1
            list_options.append("symbols")

    while num_options > signs_amount:
        num_options = 0
        print(f"You can't choose more options than signs in your password!")

        lowercase = input("Do you want lowercase letters in your password? "
                          "Type 'y' for Yes, or any other key for No: ").lower()

        uppercase = input("Do you want uppercase letters in your password? "
                          "Type 'y' for Yes, or any other key for No: ").lower()

        digits = input("Do you want digits in your password? Type 'y' for Yes, or any other key for No: ").lower()

        symbols = input("Do you want other symbols in your password? "
                        "Type 'y' for Yes, or any other key for No: ").lower()

        if lowercase == "y":
            num_options += 1
            list_options.append("lowercase")
        if uppercase == "y":
            num_options += 1
            list_options.append("uppercase")
        if digits == "y":
            num_options += 1
            list_options.append("digits")
        if symbols == "y":
            num_options += 1
            list_options.append("symbols")

    num_values = signs_amount // num_options
    rest = signs_amount % num_options

    # It chooses a random option among choices selected by the user
    random_k = random.choice(list_options)

    if lowercase == "y" and random_k != "lowercase":
        lowercase_list = random.choices(signs.lowercase, k=num_values)
        random_signs.extend(lowercase_list)
    elif lowercase == "y" and random_k == "lowercase":
        lowercase_list = random.choices(signs.lowercase, k=num_values + rest)
        random_signs.extend(lowercase_list)

    if uppercase == "y" and random_k != "uppercase":
        uppercase_list = random.choices(signs.uppercase, k=num_values)
        random_signs.extend(uppercase_list)
    elif uppercase == "y" and random_k == "uppercase":
        uppercase_list = random.choices(signs.uppercase, k=num_values + rest)
        random_signs.extend(uppercase_list)

    if digits == "y" and random_k != "digits":
        digits_list = random.choices(signs.digits, k=num_values)
        random_signs.extend(digits_list)
    elif digits == "y" and random_k == "digits":
        digits_list = random.choices(signs.digits, k=num_values + rest)
        random_signs.extend(digits_list)

    if symbols == "y" and random_k != "symbols":
        symbols_list = random.choices(signs.symbols, k=num_values)
        random_signs.extend(symbols_list)
    elif symbols == "y" and random_k == "symbols":
        symbols_list = random.choices(signs.symbols, k=num_values + rest)
        random_signs.extend(symbols_list)

    random.shuffle(random_signs)

    generate_password(random_signs_list=random_signs, random_password=password)

    again = input("Do you want to generate a new random password? Type 'y' "
                  "or or any other word or sign to end the program: ").lower()

    if again != "y":
        end_of_program = True
