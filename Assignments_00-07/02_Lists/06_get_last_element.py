def get_last_element(last):
    print("\nLast element:", last[-1])

def main():

    last = [input(f"Enter element {i+1}: ") for i in range(int(input("\nEnter number of elements: ")))]

    print("\nList:", last)
    get_last_element(last)

if __name__ == '__main__':
    main()