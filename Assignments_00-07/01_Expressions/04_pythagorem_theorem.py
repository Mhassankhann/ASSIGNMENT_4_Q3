import math

def main():
    
    ab = float(input("\033[1m\033[3mEnter the length of side AB:\033[0m "))
    ac = float(input("\033[1m\033[3mEnter the length of side AC:\033[0m "))

    bc = math.sqrt(ab**2 + ac**2)

    print(f"\nThe length of BC (the hypotenuse) is: {bc}")


if __name__ == "__main__":
    main()