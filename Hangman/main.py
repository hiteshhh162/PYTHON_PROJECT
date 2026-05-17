import random

fruits = [
    "apple",
    "mango",
    "banana",
    "orange",
    "grapes"
]

guess_word = random.choice(fruits)

print("=" * 50)
print("Guess Fruit Name")
print("=" * 50)

count = 8

# display list
word = ["_"] * len(guess_word)

while True:

    # WIN CONDITION
    if "".join(word) == guess_word:

        print("\n🎉 You Won")
        break

    # LOSE CONDITION
    if count == 0:

        print("\n💀 You Lost")
        print("Correct Word :", guess_word)
        break
    print("\nWord :", " ".join(word))

    user_letter = input(
        "Enter one letter : "
    ).lower()


    # ONLY ONE LETTER
    if len(user_letter) > 1:

        print("Enter Only One Letter")
        continue

    # CORRECT LETTER
    if user_letter in guess_word:

        for i in range(len(guess_word)):

            if guess_word[i] == user_letter:

                word[i] = user_letter

        print("✅ Correct Guess")

    else:

        count -= 1

        print("❌ Wrong Guess")

    print("Chances Left :", count)