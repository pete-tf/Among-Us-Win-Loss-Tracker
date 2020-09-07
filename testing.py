# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *


impWin = 0
impLoss = 0 
crewWin = 0 
crewLoss = 0

def addImpWin():
    global impWin
    (impWin:=impWin+1)
    impWinField.configure(text=impWin)

def remImpWin():
    global impWin
    (impWin:=impWin-1)
    impWinField.configure(text=impWin)

def addCrewWin():
    global crewWin
    (crewWin:=crewWin+1)
    crewWinField.configure(text=crewWin)

def remCrewWin():
    global crewWin
    (crewWin:=crewWin-1)
    crewWinField.configure(text=crewWin)

def addImpLoss():
    global impLoss
    (impLoss:=impLoss+1)
    impLossField.configure(text=impLoss)

def remImpLoss():
    global impLoss
    (impLoss:=impLoss-1)
    impLossField.configure(text=impLoss)

def addCrewLoss():
    global crewLoss
    (crewLoss:=crewLoss+1)
    crewLossField.configure(text=crewLoss)

def remCrewLoss():
    global crewLoss
    (crewLoss:=crewLoss-1)
    crewLossField.configure(text=crewLoss)

def renewGUI():
    gui.update()

def exitApp():
    os._exit(1)

role = "Impostor"
roleColor = "red"

# Driver code 
if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="black") 
    gui.title("Among Us Win/Loss") 
    gui.geometry("230x375")
    
    currentRole = Label(gui, text=role, fg='white', bg=roleColor, height=2, width=32)
    currentRole.grid(row=0, column=0, columnspan=3)
    
    # impWinDesc = Label(gui, text="Number of Impostor Wins", fg='white', bg='black', height=1,width=30)
    # impWinDesc.grid(row=0, column=0, columnspan=3)
    
    impWinField = Label(gui, text=impWin, fg='black', bg='white', height=1,width=7)
    impWinField.grid(row=1, column=1)
    
    buttonAddImpWin = Button(gui, text=' + ', fg='black', bg='white',
                            command=addImpWin, height=1,width=7)
    buttonAddImpWin.grid(row=1, column=2)
    
    buttonRemImpWin = Button(gui, text=' - ', fg='black', bg='white',
                            command=remImpWin, height=1,width=7)
    buttonRemImpWin.grid(row=1, column=0)
    
    crewWinDesc = Label(gui, text="Number of Crewmate Wins", fg='white', bg='black', height=1,width=30)
    crewWinDesc.grid(row=2, column=0, columnspan=3)
    
    crewWinField = Label(gui, text=crewWin, fg='black', bg='white', height=1,width=7)
    crewWinField.grid(row=3, column=1)
    
    buttonAddCrewWin = Button(gui, text=' + ', fg='black', bg='white',
                            command=addCrewWin, height=1,width=7)
    buttonAddCrewWin.grid(row=3, column=2)
    
    buttonRemCrewWin = Button(gui, text=' - ', fg='black', bg='white',
                            command=remCrewWin, height=1,width=7)
    buttonRemCrewWin.grid(row=3, column=0)

    impLossDesc = Label(gui, text="Number of Impostor Losses", fg='white', bg='black', height=1,width=30)
    impLossDesc.grid(row=4, column=0, columnspan=3)
    
    impLossField = Label(gui, text=impLoss, fg='black', bg='white', height=1,width=7)
    impLossField.grid(row=5, column=1)
    
    buttonAddImpLoss = Button(gui, text=' + ', fg='black', bg='white',
                            command=addImpLoss, height=1,width=7)
    buttonAddImpLoss.grid(row=5, column=2)
    
    buttonRemImpLoss = Button(gui, text=' - ', fg='black', bg='white',
                            command=remImpLoss, height=1,width=7)
    buttonRemImpLoss.grid(row=5, column=0)
    
    crewLossDesc = Label(gui, text="Number of Crewmate Losses", fg='white', bg='black', height=1,width=30)
    crewLossDesc.grid(row=6, column=0, columnspan=3)
    
    crewLossField = Label(gui, text=crewLoss, fg='black', bg='white', height=1,width=7)
    crewLossField.grid(row=7, column=1)
    
    buttonAddCrewLoss = Button(gui, text=' + ', fg='black', bg='white',
                            command=addCrewLoss, height=1,width=7)
    buttonAddCrewLoss.grid(row=7, column=2)
    
    buttonRemCrewLoss = Button(gui, text=' - ', fg='black', bg='white',
                            command=remCrewLoss, height=1,width=7)
    buttonRemCrewLoss.grid(row=7, column=0)
    
    blankRow = Label(gui, text="   ", fg='white', bg='black', height=1,width=30)
    blankRow.grid(row=8, column=0, columnspan=3)

    buttonQuit = Button(gui, text="Quit", fg='black', bg='white', command=exitApp, height=1,width=30)
    buttonQuit.grid(row=9,column=0,columnspan=3)
    
    
    
    
    
    gui.mainloop()

