def main():
    # gravity factors of different planets
    gravity = {
        "mercury": 0.38,
        "venus": 0.89,
        "mars": 0.38,
        "jupiter": 2.36,
        "saturn": 1.08,
        "uranus": 0.82,
        "neptune": 1.14
    }

    weight = float(input("🌍 Enter your weight on Earth: "))
    planet = input("🪐 Enter a planet name: ")

    if planet in gravity:
        new_weight = round(weight * gravity[planet], 2)
        print(f"✅ Your weight on {planet} is: {new_weight}")
    else:
        print("❌ That planet is not in our list. Try again!")


if __name__ == "__main__":
    main()
