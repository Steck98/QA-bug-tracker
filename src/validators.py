test_choice = []


def validate_text(text):
    clean_text = text.strip()
    if clean_text.isalpha() and len(clean_text) >= 2:
        return True
    else:
        print("Input must consist of only letters and can't be empty")
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
