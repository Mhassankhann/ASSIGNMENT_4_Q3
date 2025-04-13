import random

NUM_ROUNDS = 5

def main():
    print("\n🎲 Welcome to the High-Low Game! 🎯")
    print("-----------------------------------\n")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"🔢 Round {round_num}")

        user_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)

        print(f"✨ Your number is: {user_num}")

        while True:
            guess = input(
                "👉 Is your number 'higher' or 'lower' than the computer's? ").strip().lower()
            if guess in ["higher", "lower"]:
                break
            print("⚠️ Please type 'higher' or 'lower'.")

        if (guess == "higher" and user_num > comp_num) or (guess == "lower" and user_num < comp_num):
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong guess.")

        print(f"💻 Computer's number was: {comp_num}")
        print(f"🏆 Current score: {score}\n")

    print("🎮 Game Over!")
    print(f"🔚 Final Score: {score}/{NUM_ROUNDS}")

    if score == NUM_ROUNDS:
        print("🌟 Amazing! You guessed all correctly!")
    elif score >= NUM_ROUNDS // 2:
        print("👍 Nice! You did well!")
    else:
        print("🙃 Better luck next time!")


if __name__ == '__main__':
    main()
