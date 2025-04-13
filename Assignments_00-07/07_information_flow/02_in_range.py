def in_range(n, low, high):
    return low <= n <= high  # Check if n is within the range

def main():
    n = int(input("\n\033[34mEnter a number: \033[0m"))  
    low = int(input("\033[34mEnter the lower limit: \033[0m"))  
    high = int(input("\033[34mEnter the upper limit: \033[0m"))  

    output = in_range(n, low, high)
    print(output)

if __name__ == '__main__':
    main()
