def read_phonebook():
    phonebook = {}

    while (name := input("Name (press Enter to stop): ")):
        phonebook[name] = input("Number: ")
    return phonebook

def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_number(phonebook):
    while (name := input("Enter name to lookup (press Enter to stop): ")):  
        print(phonebook.get(name, f"{name} is not in the phonebook"))

def main():
    phonebook = read_phonebook()
    print_phonebook(phonebook)
    lookup_number(phonebook)

if __name__ == '__main__':
    main()
