def print_divisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')
    print()

def main():
    num = int(input("\n\033[34mEnter a number: \033[0m"))
    print(f"Here are the divisors of {num}:")
    print_divisors(num)

if __name__ == '__main__':
    main()
