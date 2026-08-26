def validate_text(text, special_text=False):
    clean_text = text.strip()
    if not special_text:
        if clean_text.isalpha() and len(clean_text) >= 2:
            return True
        else:
            print("Input must consist of at least 2 letters")
            return False
    else:
        if 500 >= len(clean_text) >= 6:
            return True
        else:
            print("Input must consist of at least 6 and a maximum of 500 characters")
            return False


def validate_number(number):
    if number.isdigit() and len(number) == 4:
        return True
    else:
        print("Input must consist of exactly 4 numbers")
        return False


def validate_status(status):
    if status == "yes":
        return True
    elif status == "no":
        return False
    else:
        print("You must chose between yes/no")


def validate_choice(choice, allowed_choice):
    if choice in allowed_choice:
        return True
    else:
        print(
            f"Choice is not available, pick one of available options: {allowed_choice}"
        )
        return False
