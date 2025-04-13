import random

def main():

    num_count = 10
    num_min = 1
    num_max = 100

    for _ in range(num_count):
        result = random.randint(num_min, num_max)
        print(result, end=" ")
    print()

if __name__ == '__main__':
    main()