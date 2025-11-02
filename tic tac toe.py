
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("❌⭕ Nehal's Tic Tac Toe Game")
root.geometry("400x500")
root.resizable(False, False)

# Global variables
player = "X"
x_score = 0
o_score = 0
draws = 0


turn_label = Label(root, text="Player X's Turn", font=("Arial", 16))
turn_label.pack(pady=10)


score_frame = Frame(root)
score_frame.pack(pady=10)

Label(score_frame, text="🏆 Scoreboard", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
x_score_label = Label(score_frame, text=f"X Wins: {x_score}", font=("Arial", 12))
x_score_label.grid(row=1, column=0, padx=10)
o_score_label = Label(score_frame, text=f"O Wins: {o_score}", font=("Arial", 12))
o_score_label.grid(row=1, column=1, padx=10)
draw_label = Label(score_frame, text=f"Draws: {draws}", font=("Arial", 12))
draw_label.grid(row=1, column=2, padx=10)


frame = Frame(root)
frame.pack()


buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    global x_score, o_score, draws
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            highlight_winner([(i, 0), (i, 1), (i, 2)])
            declare_winner(buttons[i][0]["text"])
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            highlight_winner([(0, i), (1, i), (2, i)])
            declare_winner(buttons[0][i]["text"])
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        declare_winner(buttons[0][0]["text"])
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        declare_winner(buttons[0][2]["text"])
        return True

    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        draws += 1
        update_scores()
        messagebox.showinfo("Draw", "It's a draw!")
        reset_board()
        return True
    return False

def highlight_winner(coords):
    for i, j in coords:
        buttons[i][j].config(bg="lightgreen")

def declare_winner(winner):
    global x_score, o_score
    if winner == "X":
        x_score += 1
    else:
        o_score += 1
    update_scores()
    messagebox.showinfo("Winner!", f"🎉 Player {winner} wins! 🎉")
    reset_board()

def update_scores():
    x_score_label.config(text=f"X Wins: {x_score}")
    o_score_label.config(text=f"O Wins: {o_score}")
    draw_label.config(text=f"Draws: {draws}")

def click(row, col):
    global player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        if check_winner():
            return
        player = "O" if player == "X" else "X"
        turn_label.config(text=f"Player {player}'s Turn")

def reset_board():
    global player
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="SystemButtonFace")
    player = "X"
    turn_label.config(text="Player X's Turn")

def clear_scores():
    global x_score, o_score, draws
    x_score = o_score = draws = 0
    update_scores()
    reset_board()

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda r=i, c=j: click(r, c))
        buttons[i][j].grid(row=i, column=j)


control_frame = Frame(root)
control_frame.pack(pady=20)

Button(control_frame, text="🔁 Reset Game", command=reset_board, width=15, bg="#e1e1e1").grid(row=0, column=0, padx=10)
Button(control_frame, text="🧹 Clear Scores", command=clear_scores, width=15, bg="#f5c6cb").grid(row=0, column=1, padx=10)

root.mainloop()
