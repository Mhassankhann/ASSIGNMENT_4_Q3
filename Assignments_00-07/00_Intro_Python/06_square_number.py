def main():

    number = int(input("Enter a number to be squared: "))
    square = number ** 2 

    formatted_number = f"\033[1;32m{number}\033[0m"
    formatted_square = f"\033[1;32m{square}\033[0m"

    print(f"\nThe square of {formatted_number} is {formatted_square}.")

if __name__ == '__main__':
    main()
