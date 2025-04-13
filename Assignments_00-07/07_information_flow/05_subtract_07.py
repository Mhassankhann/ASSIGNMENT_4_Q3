def subtract_seven(num):
    return num - 7

def main():
    user_input = int(input('\nEnter a number: '))
    output = subtract_seven(user_input)
    print(f'After subtracting 7: {output}')

if __name__ == '__main__':
    main()