def main():
    C = 299792458
    mass = float(input("Enter mass in kg: "))

    print("\ne = m * C²...")
    print(f"m = {mass} kg\nC = {C} m/s")
    print(f"{mass * C**2} joules of energy!")


if __name__ == '__main__':
    main()
