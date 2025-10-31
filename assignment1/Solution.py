

def generate_password(lenght = 8):
    import random
    import string

    if lenght < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    # Restrict string.punctuation to the required subset so the password includes at least one of them
    special_char = "!@#$%^&*()-_=+`"
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_char)
    ]
    # Ensure the first character is not a digit or special character
    
    # Fill the rest of the password length with a mix of all character sets
    all_characters = lowercase + uppercase + digits + special_char 
    password += random.choices(all_characters, k=lenght - 5)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)
    first_char = random.choice(lowercase + uppercase)
    password.insert(0, first_char)

    return ''.join(password)

def main():
    while True:

        try:
            length = int(input("Enter desired password length (8-16): "))
            if 8 <= length <= 16:
                break
            else:
                print("Length must be between 8 and 16 characters.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()  
