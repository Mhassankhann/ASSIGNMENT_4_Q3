def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    message = input("\033[34mPlease type a message: \033[0m")
    repeats = int(input("\033[34mEnter a number of times to repeat your message: \033[0m"))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()