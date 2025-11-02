import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("🧠 Quiz Game by Nehal")
root.geometry("700x500")
root.config(bg="#222")

current_quiz = None
question_index = 0
score = 0


quizzes = {
    "Kids Quiz": [
        ("What color is the sky?", ["Blue", "Green", "Yellow", "Red"], "Blue"),
        ("How many legs does a cat have?", ["2", "3", "4", "5"], "4"),
        ("What do cows drink?", ["Milk", "Water", "Juice", "Tea"], "Water"),
    ],
    "Programming Quiz": [
        ("What does HTML stand for?", ["HyperText Markup Language", "HighText Machine Language", "Hot Mail", "How To Make Lasagna"], "HyperText Markup Language"),
        ("Python is a ___ language.", ["Low-level", "High-level", "Assembly", "Machine"], "High-level"),
        ("What symbol starts a comment in Python?", ["//", "#", "/*", "<!--"], "#"),
    ],
    "Countries Quiz": [
        ("Which country has the largest population?", ["China", "India", "USA", "Russia"], "India"),
        ("The capital of Japan is?", ["Beijing", "Tokyo", "Seoul", "Osaka"], "Tokyo"),
        ("Which continent is Egypt in?", ["Asia", "Europe", "Africa", "Australia"], "Africa"),
    ],
    "Math Quiz": [
        ("5 + 7 =", ["10", "11", "12", "13"], "12"),
        ("Square root of 81?", ["9", "8", "7", "6"], "9"),
        ("10 × 10 =", ["100", "10", "20", "90"], "100"),
    ],
    "Science Quiz": [
        ("Water freezes at what temperature?", ["0°C", "10°C", "32°C", "100°C"], "0°C"),
        ("The Earth revolves around?", ["Moon", "Mars", "Sun", "Venus"], "Sun"),
        ("Which gas do we breathe in?", ["CO2", "Oxygen", "Nitrogen", "Helium"], "Oxygen"),
    ],
    "Mental Quiz": [
        ("If 5x = 25, x = ?", ["10", "5", "25", "20"], "5"),
        ("What comes next: 2, 4, 8, 16, ...?", ["18", "20", "32", "30"], "32"),
        ("If you have 3 apples and take away 2, how many left?", ["1", "2", "3", "5"], "1"),
    ],
    "Problem Quiz": [
        ("Ali has 10 pens, gives 4 to Sara. How many left?", ["4", "5", "6", "7"], "6"),
        ("A train runs at 60km/h. How far in 2 hours?", ["100", "120", "90", "80"], "120"),
        ("What is half of 100?", ["20", "30", "40", "50"], "50"),
    ],
    "Computer Science Quiz": [
        ("CPU stands for?", ["Central Power Unit", "Central Processing Unit", "Computer Process Unit", "Control Panel Unit"], "Central Processing Unit"),
        ("Binary code uses which digits?", ["1 & 2", "0 & 1", "2 & 3", "1 & 3"], "0 & 1"),
        ("RAM means?", ["Read Access Memory", "Random Access Memory", "Rapid Action Machine", "Real Actual Memory"], "Random Access Memory"),
    ],
    "Using Laptop Quiz": [
        ("What is the main pointing device?", ["Keyboard", "Mouse", "Screen", "Speaker"], "Mouse"),
        ("Shortcut for copy?", ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + Z"], "Ctrl + C"),
        ("Where is the power button usually?", ["Bottom", "Back", "Top", "Side"], "Top"),
    ],
    "English Quiz": [
        ("What is the plural of 'child'?", ["childs", "children", "childes", "childer"], "children"),
        ("Choose the correct word: He ___ playing.", ["is", "am", "are", "were"], "is"),
        ("Past of 'go' is?", ["gone", "goed", "went", "goes"], "went"),
    ],
}


def start_quiz(quiz_name):
    global current_quiz, question_index, score
    current_quiz = quizzes[quiz_name][:]
    random.shuffle(current_quiz)
    question_index = 0
    score = 0
    show_question()

def show_question():
    for widget in root.winfo_children():
        widget.destroy()

    if question_index < len(current_quiz):
        question, options, _ = current_quiz[question_index]

        tk.Label(root, text=f"Question {question_index+1}", font=("Arial", 18, "bold"), bg="#222", fg="white").pack(pady=10)
        tk.Label(root, text=question, font=("Arial", 16), bg="#222", fg="cyan").pack(pady=10)

        for opt in options:
            tk.Button(root, text=opt, font=("Arial", 14), width=25, bg="#444", fg="white",
                      command=lambda o=opt: check_answer(o)).pack(pady=5)
    else:
        show_result()

def check_answer(selected):
    global question_index, score
    correct = current_quiz[question_index][2]
    if selected == correct:
        score += 1
        messagebox.showinfo("✅ Correct!", f"'{selected}' is correct!")
    else:
        messagebox.showerror("❌ Wrong!", f"'{selected}' is wrong!\nCorrect answer: {correct}")
    question_index += 1
    show_question()

def show_result():
    for widget in root.winfo_children():
        widget.destroy()

    total = len(current_quiz)
    tk.Label(root, text="🎯 Final Result", font=("Arial", 22, "bold"), bg="#222", fg="gold").pack(pady=20)
    tk.Label(root, text=f"Score: {score} / {total}", font=("Arial", 20), bg="#222", fg="white").pack(pady=10)

    if score == total:
        msg = "🏆 Perfect!"
    elif score > total * 0.6:
        msg = "👏 Great Job!"
    else:
        msg = "Keep Practicing!"

    tk.Label(root, text=msg, font=("Arial", 18), bg="#222", fg="lightgreen").pack(pady=10)
    tk.Button(root, text="🏠 Back to Menu", font=("Arial", 14), bg="orange", command=main_menu).pack(pady=20)

def main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="🧠 QUIZ CATEGORIES", font=("Arial", 22, "bold"), bg="#222", fg="white").pack(pady=20)

    for qname in quizzes.keys():
        tk.Button(root, text=qname, font=("Arial", 14), width=30, bg="#333", fg="cyan",
                  command=lambda name=qname: start_quiz(name)).pack(pady=5)

    tk.Label(root, text="Created by Muhammad Nehal", bg="#222", fg="gray", font=("Arial", 12)).pack(side="bottom", pady=10)

main_menu()
root.mainloop()
