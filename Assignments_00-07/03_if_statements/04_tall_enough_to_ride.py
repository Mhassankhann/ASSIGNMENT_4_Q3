MINIMUM_HEIGHT : int = 50

def main():
    height = float(input('How tall are you? '))

    if height >= MINIMUM_HEIGHT:
        print('You are tall enough to ride the roller coaster!')
    else:
        print('You are not tall enough to ride the roller coaster.')

if __name__ == '__main__':
    main()