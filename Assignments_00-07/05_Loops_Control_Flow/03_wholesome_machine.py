def main():
    affirmation = "I am capable of doing anything I put my mind to."
    print(f"\nType this: {affirmation}")

    while True:
        user_input = input("Type: \033[34m")
        print("\033[0m")

        if user_input == affirmation:
            print("\033[32mThat's right! :)\033[0m")
            break
        else:
            print("\033[31mTry again! Type exactly as shown.\033[0m")

if __name__ == '__main__':
    main()
