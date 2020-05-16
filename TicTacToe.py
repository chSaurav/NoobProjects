from tkinter import *
import tkinter.messagebox

def callback(r,c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X',fg='blue',bg='white')
        states[r][c] = 'X'
        player = '0'
    if player == '0' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='0',fg='orange',bg='black')
        states[r][c] = '0'
        player = 'X'
    check_for_winner()

global stop_game

def check_for_winner():
    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i]!=0:
            b[0][i].config(bg='grey')
            b[1][i].config(bg='grey')
            b[2][i].config(bg='grey')
            tkinter.messagebox.showinfo("Congrats")
            stop_game = True
            exit()
        if states[0][0] == states[1][1] == states[2][2]!=0:
            b[0][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[2][2].config(bg='grey')
            tkinter.messagebox.showinfo("Congrats")
            stop_game = True
            exit()
        if states[2][0] == states[1][1] == states[0][2]!=0:
            b[0][2].config(bg='grey')
            b[1][1].config(bg='grey')
            b[2][0].config(bg='grey')
            tkinter.messagebox.showinfo("Congrats")
            stop_game = True
            exit()
        if states[i][0] == states[i][1] == states[i][2]!=0:
            b[i][0].config(bg='grey')
            b[i][1].config(bg='grey')
            b[i][2].config(bg='grey')
            tkinter.messagebox.showinfo("Congrats")
            stop_game = True
            exit()

root = Tk()
root.title("TIC TAC TOE")
b = [[0,0,0],[0,0,0],[0,0,0]]
states = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=("arial",60),width = 4,bg="blue",command=lambda r=i,c=j:callback(r,c))
        b[i][j].grid(row=i,column=j)

player = 'X'
stop_game = False
root.mainloop()
