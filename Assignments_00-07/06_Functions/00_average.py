def find_average(num_1, num_2):
    return (num_1 + num_2) / 2

def main():
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    average = find_average(num1, num2)

    print(f"The average of {num1} and {num2} is {average}")

if __name__ == "__main__":
    main()