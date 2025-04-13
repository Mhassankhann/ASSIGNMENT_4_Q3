MAX_LENGTH = 3  

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        print("Removed:", lst.pop())  # remove and print last item

def main():
    lst = [input(f"Enter value {i+1}: ") for i in range(int(input("\nEnter number of elements: ")))]
    
    print(f"\nOriginal list: {lst}")
    shorten(lst)
    print(f"Shortened list: {lst}")

if __name__ == '__main__':
    main()
