def main():
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]

    while True:
        print("\n📋 Choose an option:")
        print("1️⃣  View item")
        print("2️⃣  Change item")
        print("3️⃣  Get part of the list")
        print("4️⃣  Exit")

        choice = input("\n👉 Enter your choice: ")

        if choice == "1":
            index = int(input("🔍 Enter index: "))
            if 0 <= index < len(fruits):
                print(f"✅ Item at index {index}: {fruits[index]}")
            else:
                print("❌ Index out of range!")

        elif choice == "2":
            index = int(input("✏️ Enter index to change: "))
            if 0 <= index < len(fruits):
                new_value = input("🔄 Enter new value: ")
                fruits[index] = new_value
                print(f"✅ Updated list: {fruits}")
            else:
                print("❌ Index out of range!")

        elif choice == "3":
            start = int(input("📍 Start index: "))
            end = int(input("📍 End index: "))
            if 0 <= start < len(fruits) and 0 <= end <= len(fruits):
                print(f"✅ Sliced list: {fruits[start:end]}")
            else:
                print("❌ Invalid indices!")

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    main()
