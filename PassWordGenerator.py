import random
import string

def generate_password(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(len))
    return password

def main():
    while(True):
        print("Generator")

        len = int(input("Enter length of password: "))

        password = generate_password(len)

        print("Generated Password: ", password)

if __name__ == "__main__":
    main()