import tkinter as tk
from tkinter import messagebox
import random

# This function checks who won
def check_winner(user_choice):
    global user_score, computer_score

    # Options the computer can pick from
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)  # Randomly pick one

    # Figure out if it's a tie, or if someone won
    if user_choice == computer_choice:
        result = "It's a tie!"  # Same choice
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"  # User wins
        user_score += 1
    else:
        result = "You lose!"  # Computer wins
        computer_score += 1

    # Update score and show what happened
    update_score()
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# This updates the score on the screen
def update_score():
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {computer_score}")

# Resets the scores to zero
def reset_game():
    global user_score, computer_score
    user_score = 0  # Start over for user
    computer_score = 0  # Start over for computer
    update_score()  # Show new scores

# Closes the game window
def close_game():
    root.destroy()  # Closes the app

# Main window setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")  # Window title
root.configure(bg='#333333')  # Dark gray background

# Start scores at 0
user_score = 0
computer_score = 0

# Buttons for Rock, Paper, Scissors
rock_button = tk.Button(root, text="Rock", width=15, height=2, bg="#ff6666", fg="white", font=("Arial", 12),
                        command=lambda: determine_winner("Rock"))
rock_button.pack(pady=5)  # Add some padding

paper_button = tk.Button(root, text="Paper", width=15, height=2, bg="#66b3ff", fg="white", font=("Arial", 12),
                         command=lambda: determine_winner("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, height=2, bg="#ffcc66", fg="white", font=("Arial", 12),
                            command=lambda: determine_winner("Scissors"))
scissors_button.pack(pady=5)

# Score label setup
score_label = tk.Label(root, text=f"Your Score: {user_score}   Computer Score: {computer_score}", font=("Arial", 14),
                       bg="#333333", fg="white")
score_label.pack(pady=10)

# Reset and Close buttons
reset_button = tk.Button(root, text="Reset Game", width=15, height=2, bg="#ffcc99", fg="black", font=("Arial", 12),
                         command=reset_game)
reset_button.pack(pady=5)

close_button = tk.Button(root, text="Close Game", width=15, height=2, bg="#ff9999", fg="black", font=("Arial", 12),
                         command=close_game)
close_button.pack(pady=5)

# Start the game loop
root.mainloop()
