import random
import tkinter as tk
from tkinter import messagebox

# Random number generate
num = random.randint(1, 100)
tries = 0

# Function

def check_guess():
    global tries, num

    try:
        guessed = int(entry.get())
        tries += 1

        if guessed == num:
            result_label.config(
                text=f"🎉 Congratulations! You found the number in {tries} tries",
                fg="green"
            )
            messagebox.showinfo("Winner", "You guessed the correct number 🥳")

        elif guessed > num:
            result_label.config(
                text="📉 Too High! Try a lower number",
                fg="red"
            )

        else:
            result_label.config(
                text="📈 Too Low! Try a higher number",
                fg="orange"
            )

        entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")


# Reset Game

def reset_game():
    global num, tries

    num = random.randint(1, 100)
    tries = 0

    result_label.config(text="Game Reset! Start Again 😄", fg="blue")
    entry.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x350")
root.config(bg="#1e1e1e")

# Heading
heading = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)
heading.pack(pady=20)

# Instruction
instruction = tk.Label(
    root,
    text="Guess a number between 1 to 100",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)
instruction.pack()

# Entry Box
entry = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center",
    width=10
)
entry.pack(pady=20)

# Guess Button
guess_btn = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 14, "bold"),
    bg="cyan",
    fg="black",
    padx=10,
    pady=5,
    command=check_guess
)
guess_btn.pack(pady=10)

# Reset Button
reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="black",
    padx=10,
    pady=5,
    command=reset_game
)
reset_btn.pack(pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e"
)
result_label.pack(pady=20)

# Run Window
root.mainloop()
