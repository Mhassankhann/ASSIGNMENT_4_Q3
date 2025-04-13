def main():
    lst = []

    while (val := input("\nEnter a value (or press Enter to stop): ")):
        lst.append(val)

    print("\nHere's the list:", lst)

if __name__ == '__main__':
    main()
