import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the length of the password: "))
        if password_length <= 0:
            print("Please enter a valid positive length.")
            return

        password = generate_password(password_length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
