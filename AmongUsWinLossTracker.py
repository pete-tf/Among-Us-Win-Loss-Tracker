import d3dshot
import cv2
import pytesseract
import sys
import os
import time
import threading
import numpy as np
from tkinter import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def addImpWin():
    global impWin
    (impWin:=impWin+1)
    global totalWin
    (totalWin:=totalWin+1)
    impWinField.configure(text=impWin)
    with open('impostorWin.txt','w+') as impostorWinFile:
        impostorWinFile.write(str(impWin))
    outputToFile()

def remImpWin():
    global impWin
    (impWin:=impWin-1)
    global totalWin
    (totalWin:=totalWin-1)
    impWinField.configure(text=impWin)
    with open('impostorWin.txt','w+') as impostorWinFile:
        impostorWinFile.write(str(impWin))
    outputToFile()

def addCrewWin():
    global crewWin
    (crewWin:=crewWin+1)
    global totalWin
    (totalWin:=totalWin+1)
    crewWinField.configure(text=crewWin)
    with open('crewWin.txt','w+') as crewWinFile:
        crewWinFile.write(str(crewWin))
    outputToFile()

def remCrewWin():
    global crewWin
    (crewWin:=crewWin-1)
    global totalWin
    (totalWin:=totalWin-1)
    crewWinField.configure(text=crewWin)
    with open('crewWin.txt','w+') as crewWinFile:
        crewWinFile.write(str(crewWin))
    outputToFile()

def addImpLoss():
    global impLoss
    (impLoss:=impLoss+1)
    global totalLoss
    (totalLoss:=totalLoss+1)
    impLossField.configure(text=impLoss)
    with open('impostorLoss.txt','w+') as impostorLossFile:
        impostorLossFile.write(str(impLoss))
    outputToFile()

def remImpLoss():
    global impLoss
    (impLoss:=impLoss-1)
    global totalLoss
    (totalLoss:=totalLoss+1)
    impLossField.configure(text=impLoss)
    with open('impostorLoss.txt','w+') as impostorLossFile:
        impostorLossFile.write(str(impLoss))
    outputToFile()

def addCrewLoss():
    global crewLoss
    (crewLoss:=crewLoss+1)
    global totalLoss
    (totalLoss:=totalLoss+1)
    crewLossField.configure(text=crewLoss)
    with open('crewLoss.txt','w+') as crewLossFile:
        crewLossFile.write(str(impLoss))
    outputToFile()

def remCrewLoss():
    global crewLoss
    (crewLoss:=crewLoss-1)
    global totalLoss
    (totalLoss:=totalLoss+1)
    crewLossField.configure(text=crewLoss)
    with open('crewLoss.txt','w+') as crewLossFile:
        crewLossFile.write(str(impLoss))
    outputToFile()

def manualWin():
    global role
    global roleColor
    global bottomButton1text
    global bottomButton1color
    global bottomButton2text
    global bottomButton2color
    bottomButton1text = "Manual Crewmate"
    bottomButton1color = "blue"
    bottomButton2text = "Manual Impostor"
    bottomButton2color = "red"
    if role == "Impostor":
        addImpWin()
        role = "In Lobby"
        roleColor = "black"
        updateRole()
    if role == "Crewmate":
        addCrewWin()
        role = "In Lobby"
        roleColor = "black"
        updateRole()

def manualLoss():
    global role
    global roleColor
    global bottomButton1text
    global bottomButton1color
    global bottomButton2text
    global bottomButton2color
    bottomButton1text = "Manual Crewmate"
    bottomButton1color = "blue"
    bottomButton2text = "Manual Impostor"
    bottomButton2color = "red"
    if role == "Impostor":
        addImpLoss()
        role = "In Lobby"
        roleColor = "black"
        updateRole()
    if role == "Crewmate":
        addCrewLoss()
        role = "In Lobby"
        roleColor = "black"
        updateRole()

def manualCrew():
    global role
    global roleColor
    global bottomButton1text
    global bottomButton1color
    global bottomButton2text
    global bottomButton2color
    role = "Crewmate"
    roleColor = "blue"
    bottomButton1text = "Manual Win"
    bottomButton1color = "white"
    bottomButton2text = "Manual Loss"
    bottomButton2color = "white"
    updateRole()
    print("Manually set to Crewmate")

def manualImpostor():
    global role
    global roleColor
    global bottomButton1text
    global bottomButton1color
    global bottomButton2text
    global bottomButton2color
    role = "Impostor"
    roleColor = "red"
    bottomButton1text = "Manual Win"
    bottomButton1color = "white"
    bottomButton2text = "Manual Loss"
    bottomButton2color = "white"
    updateRole()    
    print("Manually set to Crewmate")

def bottomButton1():
    if role == "Impostor" or role == "Crewmate":
        manualWin()
    elif role == "In Lobby":
        manualCrew()

def bottomButton2():
    if role == "Impostor" or role == "Crewmate":
        manualLoss()
    elif role == "In Lobby":
        manualImpostor()

def updateRole():
    global role
    global roleColor
    global bottomButton1text
    global bottomButton1color
    global bottomButton2text
    global bottomButton2color
    currentRole.configure(text=role, bg=roleColor)
    bottomButton1.configure(text=bottomButton1text, bg=bottomButton1color)
    bottomButton2.configure(text=bottomButton2text, bg=bottomButton2color)
    renewGUI()

def renewGUI():
    gui.update()
    gui.update_idletasks()

def outputToFile():
    with open('winLossStats.txt','w+') as winLossFile:
        global outputVar
        outputVar = str("Currently " + str(role) + '\n' + "-- Winrate --" + '\n' + "Impostor: " + str(impWin) + " - " + str(impLoss) + '\n' + "Crewmate: " + str(crewWin)  + " - " + str(crewLoss) + '\n')
        winLossFile.write(outputVar)
        

def exitApp():
    os._exit(1)


def loopingImages():
    i = 1
    while i == 1:
        imageCapture()




def imageCapture():
    # d.screenshot_to_disk(region=(370, 100, 1545, 350))
    
    # capture = d.screenshot(region=(370, 100, 1545, 350))
    # gray = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    ret, thresh = cv2.threshold((cv2.cvtColor((d.screenshot(region=(leftBound, topBound, rightBound, bottomBound))), cv2.COLOR_BGR2GRAY)), 20, 255, cv2.THRESH_BINARY)

    # cv2.imshow("Screenshot",thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    numTotalPixel = thresh.shape[0] * thresh.shape[1]
    numWhitePixel = cv2.countNonZero(thresh)
    darkPercent = numWhitePixel / numTotalPixel * 100
    
    # blur = cv2.blur((cv2.threshold((cv2.cvtColor((d.screenshot(region=(370, 100, 1545, 350))), cv2.COLOR_BGR2GRAY)), 20, 255, cv2.THRESH_BINARY)),(5,5))
    # cv2.imshow("Screenshot",blur)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows
    # print(numTotalPixel)
    # print(numWhitePixel)
    # print(darkPercent)
    if ( darkPercent < 35 ):
        result = pytesseract.image_to_string(thresh)
        result = result.lower()
    else:
        result = ""
        print("No Scan.")


    global impWin
    global impLoss
    global crewWin
    global crewLoss
    global role
    global roleColor
    global bottomButton1text
    global bottomButton1color
    global bottomButton2text
    global bottomButton2color

    print(result)
    if "impostor" in result and "impostor?" not in result:
        role = "Impostor"
        roleColor = "red"
        bottomButton1text = "Manual Win"
        bottomButton1color = "white"
        bottomButton2text = "Manual Loss"
        bottomButton2color = "white"
        updateRole()
        print("Waiting for 60 seconds.")
        time.sleep(60)
    elif "crewmate" in result or "crewmnate" in result:
        role = "Crewmate"
        roleColor = "blue"
        bottomButton1text = "Manual Win"
        bottomButton1color = "white"
        bottomButton2text = "Manual Loss"
        bottomButton2color = "white"
        updateRole()
        print("Waiting for 60 seconds.")
        time.sleep(60)
    elif "victory" in result:
        if role == "Impostor":
            addImpWin()
            role = "In Lobby"
            roleColor = "black"
            bottomButton1text = "Manual Crewmate"
            bottomButton1color = "blue"
            bottomButton2text = "Manual Impostor"
            bottomButton2color = "red"
            updateRole()
        if role == "Crewmate":
            addCrewWin()
            role = "In Lobby"
            roleColor = "black"
            bottomButton1text = "Manual Crewmate"
            bottomButton1color = "blue"
            bottomButton2text = "Manual Impostor"
            bottomButton2color = "red"
            updateRole()
    elif "defeat" in result:
        if role == "Impostor":
            addImpLoss()
            role = "In Lobby"
            roleColor = "black"
            bottomButton1text = "Manual Crewmate"
            bottomButton1color = "blue"
            bottomButton2text = "Manual Impostor"
            bottomButton2color = "red"
            updateRole()
            time.sleep(5)
        if role == "Crewmate":
            addCrewLoss()
            role = "In Lobby"
            roleColor = "black"
            bottomButton1text = "Manual Crewmate"
            bottomButton1color = "blue"
            bottomButton2text = "Manual Impostor"
            bottomButton2color = "red"
            updateRole()
            time.sleep(5)
    else:
        print(role)
        print("Nothing Done.")

    time.sleep(1)
    #imageCapture()






script_dir = os.path.dirname(os.path.abspath(__file__))
tesspath = resource_path('Tesseract\\tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = os.path.join(tesspath)

d = d3dshot.create(capture_output="numpy")
resolution = str(d.display)
resolution = resolution.split("resolution=",1)[1]
resolution = resolution.split("rotation=",1)[0]
xRes = int(resolution.split("x",1)[0])
yRes = int(resolution.split("x",1)[1])

leftBound = int( xRes * 0.192708 )
topBound = int( yRes * 0.09259259259259 )
rightBound = int( xRes * 0.8046875 )
bottomBound = int( yRes * 0.324074074074074 )

impWin = 0
impLoss = 0
crewWin = 0
crewLoss = 0
totalWin = 0
totalLoss = 0



if os.path.isfile('impostorWin.txt'):
    with open('impostorWin.txt') as impostorWinFile:
        impWin = int(impostorWinFile.read())
else:
    with open('impostorWin.txt','w+') as impostorWinFile:
        impostorWinFile.write("0")
        impWin = 0

if os.path.isfile('impostorLoss.txt'):
    with open('impostorLoss.txt') as impostorLossFile:
        impLoss = int(impostorLossFile.read())
else:
    with open('impostorLoss.txt','w+') as impostorLossFile:
        impostorLossFile.write("0")
        impLoss = 0

if os.path.isfile('crewWin.txt'):
    with open('crewWin.txt') as crewWinFile:
        crewWin = int(crewWinFile.read())
else:
    with open('crewWin.txt','w+') as crewWinFile:
        crewWinFile.write("0")
        crewWin = 0

if os.path.isfile('crewLoss.txt'):
    with open('crewLoss.txt') as crewLossFile:
        crewLoss = int(crewLossFile.read())
else:
    with open('crewLoss.txt','w+') as crewLossFile:
        crewLossFile.write("0")
        crewLoss = 0

# if os.path.isfile('config.ini'):
#     with open('config.ini') as configFile:
#         for line in configFile:
#             if re.search('##', line) is None:
#                 outputConfig = line
#                 outputVar = str(outputConfig)
# else:
#     with open('config.ini','w+') as configFile:
#         outputVar = str("Currently " + str(role) + '\n' + "-- Winrate --" + '\n' + "Impostor: " + str(impWin) + " - " + str(impLoss) + '\n' + "Crewmate: " + str(crewWin)  + " - " + str(crewLoss) + '\n')
#         configFile.write(outputVar)

if not os.path.isfile('winLossStats.txt'):
    with open('winLossStats.txt','w+') as winLossFile:
        winLossFile.write("")
    
        


role = "In Lobby"
roleColor = "black"

bottomButton1text = "Manual Crewmate"
bottomButton1color = "blue"

bottomButton2text = "Manual Impostor"
bottomButton2color = "red"


impWinField = ""
impLossField = ""
CrewWinField = ""
CrewLossField = ""

imCap = threading.Thread(target=loopingImages)
imCap.start()

time.sleep(.5)

imCap2 = threading.Thread(target=loopingImages)
imCap2.start()


if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="black") 
    gui.title("Among Us Win/Loss") 
    gui.geometry("230x350")
    gui.protocol("WM_DELETE_WINDOW", exitApp)
    gui.wm_attributes("-topmost", 1)
    
    currentRole = Label(gui, text=role, fg='white', bg=roleColor, height=2, width=32)
    currentRole.grid(row=0, column=0, columnspan=3)

    impWinDesc = Label(gui, text="Impostor Wins", fg='white', bg='black', height=1,width=30)
    impWinDesc.grid(row=1, column=0, columnspan=3)
    
    impWinField = Label(gui, text=impWin, fg='black', bg='white', height=1,width=7)
    impWinField.grid(row=2, column=1)
    
    buttonAddImpWin = Button(gui, text=' + ', fg='black', bg='white',
                            command=addImpWin, height=1,width=7)
    buttonAddImpWin.grid(row=2, column=2)
    
    buttonRemImpWin = Button(gui, text=' - ', fg='black', bg='white',
                            command=remImpWin, height=1,width=7)
    buttonRemImpWin.grid(row=2, column=0)
    
    impLossDesc = Label(gui, text="Impostor Losses", fg='white', bg='black', height=1,width=30)
    impLossDesc.grid(row=3, column=0, columnspan=3)
    
    impLossField = Label(gui, text=impLoss, fg='black', bg='white', height=1,width=7)
    impLossField.grid(row=4, column=1)
    
    buttonAddImpLoss = Button(gui, text=' + ', fg='black', bg='white',
                            command=addImpLoss, height=1,width=7)
    buttonAddImpLoss.grid(row=4, column=2)
    
    buttonRemImpLoss = Button(gui, text=' - ', fg='black', bg='white',
                            command=remImpLoss, height=1,width=7)
    buttonRemImpLoss.grid(row=4, column=0)

    crewWinDesc = Label(gui, text="Crewmate Wins", fg='white', bg='black', height=1,width=30)
    crewWinDesc.grid(row=5, column=0, columnspan=3)
    
    crewWinField = Label(gui, text=crewWin, fg='black', bg='white', height=1,width=7)
    crewWinField.grid(row=6, column=1)
    
    buttonAddCrewWin = Button(gui, text=' + ', fg='black', bg='white',
                            command=addCrewWin, height=1,width=7)
    buttonAddCrewWin.grid(row=6, column=2)
    
    buttonRemCrewWin = Button(gui, text=' - ', fg='black', bg='white',
                            command=remCrewWin, height=1,width=7)
    buttonRemCrewWin.grid(row=6, column=0)


    
    crewLossDesc = Label(gui, text="Crewmate Losses", fg='white', bg='black', height=1,width=30)
    crewLossDesc.grid(row=7, column=0, columnspan=3)
    
    crewLossField = Label(gui, text=crewLoss, fg='black', bg='white', height=1,width=7)
    crewLossField.grid(row=8, column=1)
    
    buttonAddCrewLoss = Button(gui, text=' + ', fg='black', bg='white',
                            command=addCrewLoss, height=1,width=7)
    buttonAddCrewLoss.grid(row=8, column=2)
    
    buttonRemCrewLoss = Button(gui, text=' - ', fg='black', bg='white',
                            command=remCrewLoss, height=1,width=7)
    buttonRemCrewLoss.grid(row=8, column=0)

    bottomButton1 = Button(gui, text=bottomButton1text, fg='black', bg=bottomButton1color, command=bottomButton1, height=1,width=30)
    bottomButton1.grid(row=9,column=0,columnspan=3)

    bottomButton2 = Button(gui, text=bottomButton2text, fg='black', bg=bottomButton2color, command=bottomButton2, height=1,width=30)
    bottomButton2.grid(row=10,column=0,columnspan=3)

    blankRow = Label(gui, text="   ", fg='white', bg='black', height=1,width=30)
    blankRow.grid(row=11, column=0, columnspan=3)

    buttonQuit = Button(gui, text="Quit", fg='black', bg='white', command=exitApp, height=1,width=30)
    buttonQuit.grid(row=12,column=0,columnspan=3)
    
    gui.mainloop()

