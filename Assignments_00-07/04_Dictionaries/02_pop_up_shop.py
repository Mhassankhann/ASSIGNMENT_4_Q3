def main():

    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.0
    }

    total_cost = 0.0
    purchased_items = {}

    print("\n🍏🍍 Welcome to the **Tropical Fruit Pop-Up Shop!** 🍉🍌")
    print("\n🌟 **Available Fruits & Prices:**\n")

    for fruit, price in fruit_prices.items():
        print(f"➡️ {fruit.capitalize()} - ${price:.2f} each")

    print("\n🛒 **Start Shopping!** (Enter 0 to skip a fruit)\n")

    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(
                    input(f"How many {fruit}s would you like to buy? : "))
                if quantity < 0:
                    print("❌ Please enter a valid quantity!")
                else:
                    break
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

        if quantity > 0:
            purchased_items[fruit] = quantity
            total_cost += quantity * price
            print(f"Added {quantity} {fruit}(s) to your cart! 🛒\n")

    print("\n🧾 **Your Final Order Summary:**")
    for fruit, quantity in purchased_items.items():
        print(
            f"🍎 {fruit.capitalize()} x {quantity} = ${fruit_prices[fruit] * quantity:.2f}")

    print(f"\n\033[1m\033[3mTotal Amount Due: ${total_cost:.2f}\033[0m\n")
    print("🎉 Thank you for shopping.")


if __name__ == "__main__":
    main()
