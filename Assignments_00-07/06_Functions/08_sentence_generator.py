def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid choice! Please enter 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    word = input("\n\033[34mPlease type a noun, verb, or adjective: \033[0m")
    part_of_speech = int(input("\033[34mIs this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: \033[0m"))
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()
