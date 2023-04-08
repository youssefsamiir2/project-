import tkinter as tk
import random

# Define the puzzle size
SIZE = 3

# Create the main window
root = tk.Tk()
root.title("Sliding Puzzle")

# Create the puzzle board
board = []
for i in range(SIZE):
    row = []
    for j in range(SIZE):
        if i == SIZE-1 and j == SIZE-1:
            row.append(None)
        else:
            row.append(i*SIZE+j+1)
    board.append(row)

# Shuffle the board
for i in range(100):
    x, y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
    dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    if x+dx >= 0 and x+dx < SIZE and y+dy >= 0 and y+dy < SIZE:
        board[x][y], board[x+dx][y+dy] = board[x+dx][y+dy], board[x][y]

# Create the buttons
buttons = []
for i in range(SIZE):
    row = []
    for j in range(SIZE):
        if board[i][j] is None:
            button = tk.Button(root, text="", width=4, height=2)
        else:
            button = tk.Button(root, text=str(board[i][j]), width=4, height=2)
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Define the move function
def move(i, j):
    if i > 0 and board[i-1][j] is None:
        board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
        buttons[i][j]["text"] = ""
        buttons[i-1][j]["text"] = str(board[i-1][j])
    elif i < SIZE-1 and board[i+1][j] is None:
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        buttons[i][j]["text"] = ""
        buttons[i+1][j]["text"] = str(board[i+1][j])
    elif j > 0 and board[i][j-1] is None:
        board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
        buttons[i][j]["text"] = ""
        buttons[i][j-1]["text"] = str(board[i][j-1])
    elif j < SIZE-1 and board[i][j+1] is None:
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        buttons[i][j]["text"] = ""
        buttons[i][j+1]["text"] = str(board[i][j+1])

    # Check if the puzzle is solved
    if all(board[i][j] == i*SIZE+j+1 for i in range(SIZE) for j in range(SIZE)):
        tk.messagebox.showinfo("Congratulations", "You won!")

# Bind the buttons to the move function
for i in range(SIZE):
    for j in range(SIZE):
        buttons[i][j].config(command=lambda i=i, j=j: move(i, j))

# Run the main loop
root.mainloop()
