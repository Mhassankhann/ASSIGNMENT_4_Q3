def main():
    num_counts = {}

    while (user_input := input("\033[94mEnter a number (or press Enter to finish): \033[0m")):

        number = int(user_input)

        num_counts[number] = num_counts.get(number, 0) + 1

    print("\nNumber occurrences:")
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

if __name__ == '__main__':
    main()
