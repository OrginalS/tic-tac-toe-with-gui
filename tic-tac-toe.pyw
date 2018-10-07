from tkinter import *
from tkinter import messagebox
root = Tk()
move = 1
one = two = three = four = five = six = seven = eight = nine = ""
x_wins = 0
o_wins = 0
score = StringVar()
score.set("X "+str(x_wins)+" : "+str(o_wins)+" O")


def reset_game():
    global one, two, three, four, five, six, seven, eight, nine
    global move
    move = 1
    one = two = three = four = five = six = seven = eight = nine = ""
    canvas1.delete("all"), canvas2.delete("all"), canvas3.delete("all"), canvas4.delete("all"), canvas5.delete("all"), canvas6.delete("all"), canvas7.delete("all"), canvas8.delete("all"), canvas9.delete("all")


def game_logic():
    global one, two, three, four, five, six, seven, eight, nine
    global x_wins, o_wins
    if one == "x" and two == "x" and three == "x" or four == "x" and five == "x" and six == "x" or seven == "x" and eight == "x" and nine == "x" or one == "x" and four == "x" and seven == "x" or two == "x" and five == "x" and eight == "x" or three =="x" and six == "x" and nine == "x" or one =="x" and five == "x" and nine == "x" or three == "x" and five == "x" and seven == "x":
        x_wins += 1
        score.set("X " + str(x_wins) + " : " + str(o_wins) + " O")
        messagebox.showinfo("tic-tac-toe", "X wins!")
        one = two = three = four = five = six = seven = eight = nine = "end"
    elif one == "o" and two == "o" and three == "o" or four == "o" and five == "o" and six == "o" or seven == "o" and eight == "o" and nine == "o" or one == "o" and four == "o" and seven == "o" or two == "o" and five == "o" and eight == "o" or three =="o" and six == "o" and nine == "o" or one =="o" and five == "o" and nine == "o" or three == "o" and five == "o" and seven == "o":
        o_wins += 1
        score.set("X " + str(x_wins) + " : " + str(o_wins) + " O")
        messagebox.showinfo("tic-tac-toe", "O wins!")
        one = two = three = four = five = six = seven = eight = nine = "end"
    elif move >=10:
        score.set("X " + str(x_wins) + " : " + str(o_wins) + " O")
        messagebox.showinfo("tic-tac-toe", "Draw!")
        one = two = three = four = five = six = seven = eight = nine = "end"


def put(event, pos, poscheck):
    global move
    global one, two, three, four, five, six, seven, eight, nine
    if poscheck == "":
        if pos == 1:
            if move % 2 == 0:
                canvas1.create_oval(25, 25, 175, 175, width=5, outline="blue")
                one = "o"
            else:
                canvas1.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas1.create_line(25, 175, 175, 25, fill="green", width=5)
                one = "x"
        if pos == 2:
            if move % 2 == 0:
                canvas2.create_oval(25, 25, 175, 175, width=5, outline="blue")
                two = "o"
            else:
                canvas2.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas2.create_line(25, 175, 175, 25, fill="green", width=5)
                two = "x"
        if pos == 3:
            if move % 2 == 0:
                canvas3.create_oval(25, 25, 175, 175, width=5, outline="blue")
                three = "o"
            else:
                canvas3.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas3.create_line(25, 175, 175, 25, fill="green", width=5)
                three = "x"
        if pos == 4:
            if move % 2 == 0:
                canvas4.create_oval(25, 25, 175, 175, width=5, outline="blue")
                four = "o"
            else:
                canvas4.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas4.create_line(25, 175, 175, 25, fill="green", width=5)
                four = "x"
        if pos == 5:
            if move % 2 == 0:
                canvas5.create_oval(25, 25, 175, 175, width=5, outline="blue")
                five = "o"
            else:
                canvas5.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas5.create_line(25, 175, 175, 25, fill="green", width=5)
                five = "x"
        if pos == 6:
            if move % 2 == 0:
                canvas6.create_oval(25, 25, 175, 175, width=5, outline="blue")
                six = "o"
            else:
                canvas6.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas6.create_line(25, 175, 175, 25, fill="green", width=5)
                six = "x"
        if pos == 7:
            if move % 2 == 0:
                canvas7.create_oval(25, 25, 175, 175, width=5, outline="blue")
                seven = "o"
            else:
                canvas7.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas7.create_line(25, 175, 175, 25, fill="green", width=5)
                seven = "x"
        if pos == 8:
            if move % 2 == 0:
                canvas8.create_oval(25, 25, 175, 175, width=5, outline="blue")
                eight = "o"
            else:
                canvas8.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas8.create_line(25, 175, 175, 25, fill="green", width=5)
                eight = "x"
        if pos == 9:
            if move % 2 == 0:
                canvas9.create_oval(25, 25, 175, 175, width=5, outline="blue")
                nine = "o"
            else:
                canvas9.create_line(25, 25, 175, 175, fill="green", width=5)
                canvas9.create_line(25, 175, 175, 25, fill="green", width=5)
                nine = "x"
        move += 1
        game_logic()


root.title("tic-tac-toe")
canvas1 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas1.grid(row=0, column=0)
canvas1.bind("<Button-1>", lambda self: put(self, 1, one))
canvas2 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas2.grid(row=0, column=1)
canvas2.bind("<Button-1>", lambda self: put(self, 2, two))
canvas3 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas3.grid(row=0, column=2)
canvas3.bind("<Button-1>", lambda self: put(self, 3, three))
canvas4 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas4.grid(row=1, column=0)
canvas4.bind("<Button-1>", lambda self: put(self, 4, four))
canvas5 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas5.grid(row=1, column=1)
canvas5.bind("<Button-1>", lambda self: put(self, 5, five))
canvas6 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas6.grid(row=1, column=2)
canvas6.bind("<Button-1>", lambda self: put(self, 6, six))
canvas7 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas7.grid(row=2, column=0)
canvas7.bind("<Button-1>", lambda self: put(self, 7, seven))
canvas8 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas8.grid(row=2, column=1)
canvas8.bind("<Button-1>", lambda self: put(self, 8, eight))
canvas9 = Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")
canvas9.grid(row=2, column=2)
canvas9.bind("<Button-1>", lambda self: put(self, 9, nine))
reset = Button(root, text="Reset game!", command=reset_game)
reset.grid(row=0, column=4)
scorelabel = Label(root, textvariable=score)
scorelabel.config(font=("Courier", 30))
scorelabel.grid(row=1, column=4)

root.mainloop()