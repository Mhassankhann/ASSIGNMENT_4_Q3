def main():

    animal = input("What's your favorite animal? ")

    formatted_animal = f"\033[1;3m{animal}\033[0m"

    print(f'My favorite animal is also {formatted_animal}.')

if __name__ == "__main__":
    main()
