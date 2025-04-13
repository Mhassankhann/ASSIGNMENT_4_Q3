import random

def main():
    secret_number = random.randint(1, 99)
    print("\nI'm thinking of a number between 1 and 99...")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congrats! The number was {secret_number}.")
            break

if __name__ == '__main__':
    main()
