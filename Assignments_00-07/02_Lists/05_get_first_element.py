def get_first_element(lst):
    print("\nFirst element:", lst[0])

def main():

    lst = [input(f"Enter element {i+1}: ") for i in range(int(input("\nEnter number of elements: ")))]

    print("\nList:", lst)
    get_first_element(lst)

if __name__ == '__main__':
    main()