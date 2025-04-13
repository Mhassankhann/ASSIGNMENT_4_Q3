def double(num: int):
    return num * 2

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    
    print(f"\033[1m\033[3mUser input: {num}\033[0m")
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
