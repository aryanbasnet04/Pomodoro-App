from tkinter import *
import math

# ---------------------
# ------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
  window.after_cancel(timer)
  canvas.itemconfig(canvasText,text="00:00")
  TimerLabel.config(text="Timer")
  global reps
  reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
  global reps
  reps+=1

  workSec=WORK_MIN*60
  shortBreakSec=SHORT_BREAK_MIN*60
  longBreakSec=LONG_BREAK_MIN*60

  # If its the 8th rep:
  if reps%8==0:
    countDown(longBreakSec)

  # If it's the 2th,4th,6th rep
  elif reps%2==0:
    countDown(shortBreakSec)
    TimerLabel.config(text="Short Break")
  else:
    countDown(workSec)
    TimerLabel.config(text="Work")

def countDown(count):

  countMin=math.floor(count/60)
  countSec=count%60

  if countSec<10:
    countSec=f"0{countSec}"
  canvas.itemconfig(canvasText,text=f"{countMin}:{countSec}")
  if count>0:
    global timer
    timer=window.after(1000,countDown,count-1)
  else:
    startTimer()
    marks=""
    workSession=math.floor(reps/2)
    for _ in range(workSession):
      marks+="✅"
    checkMark.config(text=marks)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- 
import time

# ---------------------------- UI SETUP ------------------------------- 
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,background=YELLOW)




TimerLabel=Label(text="Timer",font=(FONT_NAME,45,"bold"),bg=YELLOW,fg=GREEN)
TimerLabel.grid(row=0,column=1)

canvas=Canvas(width=200,height=223,background=YELLOW,highlightthickness=0)
tomatoImage=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomatoImage)
canvasText=canvas.create_text(100,130,text="25:00",fill="white",font=(FONT_NAME,35,"bold"))

canvas.grid(row=1,column=1)


startButton=Button(text="Start",bg=YELLOW,highlightthickness=0,command=startTimer)
startButton.grid(row=2,column=0)


resetButton=Button(text="Reset",bg=YELLOW,highlightthickness=0,command=resetTimer)
resetButton.grid(row=2,column=2)

checkMark=Label(bg=YELLOW)
checkMark.grid(row=3,column=1)


window.mainloop()