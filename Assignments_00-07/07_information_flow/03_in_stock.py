def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "orange": 250,
        "mango": 700
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("\n\033[34mEnter a fruit: \033[0m").strip()  
    stock = num_in_stock(fruit)

    print(f"\033[32mIn stock: {stock}\033[0m" if stock else "\033[31mNot in stock!\033[0m")

if __name__ == '__main__':
    main()
