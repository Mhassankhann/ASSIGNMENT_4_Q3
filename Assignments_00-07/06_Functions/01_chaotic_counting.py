import random

def done():
    return random.random() < 0.2

def chaotic_counting():
    for i in range(1, 11):
        if done():
            break
        print(i, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

if __name__ == '__main__':
    main()