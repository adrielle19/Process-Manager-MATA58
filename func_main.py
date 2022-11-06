import tkinter as tk
from tkinter import *

def open_win(window,p,q,o):

    newWindow = Toplevel(window)
    newWindow.title("Execução")
    newWindow.geometry("{}x{}".format(450+int((p-1)/10)*300,400+(p*70)))

    counter=0
    j=0
    for i in range(p):
        if counter==10:
            counter=0
            j+=1
        txt = Label(newWindow, text='Processo: {}'.format(i+1), font=17)
        txt.place(x=150+j*300, y=15+((i+1-(j*10))*90))
        txt = Label(newWindow, text='Inicio do processo:')
        txt.place(x=100+j*300, y=50+((i+1-(j*10))*90))

        btn = Entry(newWindow,justify='center')
        btn.place(x=220+j*300, y=50+((i+1-(j*10))*90))
        counter+=1