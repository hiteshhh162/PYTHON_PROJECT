import random
import time

# =============================
# Stone Paper Scissor Game
# =============================

print("\n" + "=" * 50)
print("🎮   WELCOME TO STONE PAPER SCISSOR   🎮")
print("=" * 50)
print("First to score 5 points wins the game!")
print()

u_score = 0
c_score = 0

choices = {
    1: "🪨 Stone",
    2: "📄 Paper",
    3: "✂️ Scissor"
}

while True:

    print("\n" + "-" * 50)
    print(f"🏆 Your Score : {u_score}   |   🤖 Computer Score : {c_score}")
    print("-" * 50)

    print("\nChoose your move:")
    print("1 ➜ 🪨 Stone")
    print("2 ➜ 📄 Paper")
    print("3 ➜ ✂️ Scissor")
    print("0 ➜ ❌ Exit Game")

    try:
        user = int(input("\n👉 Enter your choice: "))

        if user == 0:
            print("\n👋 Thanks for playing!")
            break

        if user not in [1, 2, 3]:
            print("\n⚠️ Invalid choice! Please choose between 1 to 3.")
            continue

        com = random.randint(1, 3)

        print("\n🎲 Computer is choosing...")
        time.sleep(1)

        print(f"\n🧑 You chose      : {choices[user]}")
        print(f"🤖 Computer chose : {choices[com]}")

        # Winning conditions
        if (
            (user == 1 and com == 3) or
            (user == 2 and com == 1) or
            (user == 3 and com == 2)
        ):
            print("\n✅ You WON this round! 🎉")
            u_score += 1

        elif user == com:
            print("\n🤝 This round is DRAW!")

        else:
            print("\n❌ Computer WON this round!")
            c_score += 1

        # Final Result
        if c_score == 5:
            print("\n" + "=" * 50)
            print("😥 Oops! You LOST the game.")
            print("🏁 Better luck next time!")
            print("=" * 50)
            break

        elif u_score == 5:
            print("\n" + "=" * 50)
            print("🥳 CONGRATULATIONS! YOU WON THE GAME! 🤩")
            print("🏆 You are the champion!")
            print("=" * 50)
            break

    except ValueError:
        print("\n⚠️ Please enter only numbers!")