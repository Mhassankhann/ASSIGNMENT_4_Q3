def main():
    curr_value = int(input("\nEnter a number: "))
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)

if __name__ == "__main__":
    main()