import tkinter as tk
import random

score = 0
com_score = 0


def sth(a):
    global score, com_score, text_box
    text_box.destroy()

    # computer choice
    ls = ['rock', 'paper', 'scissors']
    computer = random.choice(ls)
    # print(com)

    # draw
    if a == computer:
        print('draw')
    # user won
    elif a == 'rock' and computer == 'scissors':
        score += 1
        print('win')
    elif computer == 'rock' and a == 'paper':
        score += 1
        print('win')
    elif a == 'scissors' and computer == 'paper':
        score += 1
        print('win')
    else:  # com wins
        com_score += 1
        print('lost')

    text_box = tk.Label(root, bg='#ffff00')
    text_box.configure(text=f"""
    Your choice : {a}
    Comp's choice : {computer}
    Your score : {score}
    Computer's score: {com_score}
    """)
    text_box.grid(row=3, sticky='W', pady=10, ipadx=20)


# creating the main window
root = tk.Tk()
# root properties
root.geometry('340x300')
root.title('Rock, paper, scissors Game')
root.resizable(0, 0)

text_box = tk.Label(root, bg='#ffff00')

# buttons
rock = tk.Button(master=root, text='Rock', bg='#0099cc', font=('Courier', 9), width=7, command=lambda: sth('rock'))
paper = tk.Button(master=root, text='Paper', bg='#ff80aa', font=('Courier', 9), width=7, command=lambda: sth('paper'))
scissors = tk.Button(master=root, text='scissors', bg='#00e600', font=('Courier', 9), width=7,
                     command=lambda: sth('scissors'))
rock.grid(ipadx=10, padx=80)
paper.grid(ipadx=10, padx=80, row=1)
scissors.grid(ipadx=10, padx=80, row=2)

root.mainloop()
