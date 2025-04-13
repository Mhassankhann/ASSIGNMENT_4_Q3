def count_even():
    lst = []

    while True:
        user_input = input('Enter an integer or press Enter to stop: ')

        if not user_input:
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter an integer.")

    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f'Number of even numbers: {even_count}')

def main():
    count_even()

if __name__ == "__main__":
    main()