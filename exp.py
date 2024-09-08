from tkinter import *
import random
import pygame

pygame.init()
win = pygame.mixer.Sound('WinSound.wav')
lose = pygame.mixer.Sound('LoseSound.wav')
tie = pygame.mixer.Sound('TieSound.wav')


def start_game():
    player_name = entry_player.get()
    scolbl.config(text=f"{player_name} Score : ")
    plbl.config(text=f"{player_name} :")


    name_entry_frame.pack_forget()  
    frm1.pack()
    frm2.pack()
    frm3.pack()
    frm4.pack()
    frm5.pack()
    frm6.pack()
    frm7.pack()
    frm8.pack()
    frm9.pack()
    frm10.pack()
    frm11.pack()
    frm12.pack()
    frm13.pack()
    frm14.pack()
    frm15.pack()
    frm16.pack()
    exit_button.pack(side="bottom",padx=10,pady=20)



top = Tk()
back = PhotoImage(file="background.png")
main_bg = Label(top,image=back)
main_bg.place(relheight=1,relwidth=1)
top.title("Rock Paper Scissors")
top.geometry("600x600")
icon = PhotoImage(file="images.png")
top.iconphoto(True,icon)


name_entry_frame = Frame(top,bg="#011c0a")

player_label = Label(name_entry_frame, text="Enter Your Name:", font=("Helvetica", 20), fg="White",bg="#011c0a")
player_label.pack(side="top",pady=30)

entry_player = Entry(name_entry_frame, font=("Helvetica", 20))
entry_player.pack(pady=40)

start_button = Button(name_entry_frame, text="Start Game", font=("Helvetica", 15), fg="White", bg="Green", command=start_game)
start_button.pack()

name_entry_frame.pack()

frm1 = Frame(top,height = 20,bg = "#011c0a")

frm2 = Frame(top,height = 50,bg = "#011c0a")   

frm3 = Frame(top,height = 20,bg = "#011c0a")

frm4 = Frame(top,height = 40,bg = "#011c0a")

frm5 = Frame(top,height = 20,bg = "#011c0a")

frm6 = Frame(top,height = 20,bg = "#011c0a")

frm7 = Frame(top,height = 20,bg = "#011c0a")

frm8 = Frame(top,height = 50,bg = "#011c0a")

frm9 = Frame(top,height = 20,bg = "#011c0a")

frm10 = Frame(top,height = 40,bg = "#011c0a")

frm11 = Frame(top,height = 20,bg = "#011c0a")

frm12 = Frame(top,height = 30,bg = "#011c0a")

frm13 = Frame(top,height = 20,bg = "#011c0a")

frm14 = Frame(top,height = 30,bg = "#011c0a")

frm15 = Frame(top,height = 20,bg = "#011c0a")

frm16 = Frame(top,height=30,bg = "#011c0a")

global src
global src1
src = 0
src1 = 0

def r():
	pl.config(text = "ROCK",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
	p.config(text = "ROCK  ",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
	val = int(random.randint(1,3))
	if (val == 1):
		comp.config(text = "ROCK",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  ROCK",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "TIED",font = ("Helvetica",20),bg = "#011c0a",fg = "blue")
		tie.play()
	elif (val == 2):
		comp.config(text = "PAPER",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  PAPER",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "COMPUTER WON",font = ("Helvetica",20),bg = "#011c0a",fg = "red")
		lose.play()
		global src
		global src1
		src1+=1
		src-=1
		score.config(text = src)
		score1.config(text=src1)
	else:
		comp.config(text = "SCISSOR",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  SCISSOR",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "YOU WON",font = ("Helvetica",20),bg = "#011c0a",fg = "lime")
		win.play()
		src+=1
		src1-=1
		score.config(text = src)
		score1.config(text = src1)
	rock.config(state = "disable")
	ppr.config(state = "disable")
	sci.config(state = "disable")



def pa():
	pl.config(text = "PAPER",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
	p.config(text = "PAPER  ",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
	val = int(random.randint(1,3))
	if (val == 1):
		comp.config(text = "ROCK",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  ROCK",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "YOU WON",font = ("Helvetica",20),bg = "#011c0a",fg = "lime")
		win.play()
		global src
		global src1
		src1-=1
		src+=1
		score.config(text = src)
		score1.config(text = src1)
	elif (val == 2):
		comp.config(text = "PAPER",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  PAPER",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "TIED",font = ("Helvetica",20),bg = "#011c0a",fg = "blue")
		tie.play()
	else:
		comp.config(text = "SCISSOR",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  SCISSOR",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "COMPUTER WON",font = ("Helvetica",20),bg = "#011c0a",fg = "red")
		lose.play()
		src-=1
		src1+=1
		score1.config(text=src1)
		score.config(text = src)
	rock.config(state = "disable")
	ppr.config(state = "disable")
	sci.config(state = "disable")



def s():
	pl.config(text = "SCISSOR",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
	p.config(text = "SCISSOR  ",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
	val = int(random.randint(1,3))
	if (val == 1):
		comp.config(text = "ROCK",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  ROCK",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "COMPUTER WON",font = ("Helvetica",20),bg = "#011c0a",fg = "red")
		lose.play()
		global src
		global src1
		src-=1
		src+=1
		score1.config(text=src1)
		score.config(text = src)
	elif (val == 2):
		comp.config(text = "PAPER",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  PAPER",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "YOU WON",font = ("Helvetica",20),bg = "#011c0a",fg = "lime")
		win.play()
		src+=1
		src1-=1
		score1.config(text=src1)
		score.config(text = src)
	else:
		comp.config(text = "SCISSOR",font = ("Helvetica",25),bg = "#011c0a",fg = "cyan")
		c.config(text = "  SCISSOR",font = ("Helvetica",20),fg = "orange",bg = "#011c0a")
		fin.config(text = "TIED",font = ("Helvetica",20),bg = "#011c0a",fg = "blue")
		tie.play()
	rock.config(state = "disable")
	ppr.config(state = "disable")
	sci.config(state = "disable")

def res():
	pl.config(text = "")
	p.config(text = "")
	comp.config(text = "")
	c.config(text = "")
	fin.config(text = "")
	rock["state"] = "normal"
	ppr["state"] = "normal"
	sci["state"] = "normal"

tit = Label(frm1,text = "Rock Paper Scissor",font = ("Helvetica",25,"bold","italic"),fg = "yellow",bg = "#011c0a")
tit.pack()

rockp = PhotoImage(file="rocks.png")
rock = Button(frm3,text = "ROCK",font = "Helvetica,bold,200",padx = 10,fg = "#003153",command = r,image=rockp,relief=RAISED,bd=5,compound="top")
rock.pack(side = "left")

rp = Label(frm3,bg = "#011c0a",padx = 15)
rp.pack(side = "left")

paperp = PhotoImage(file="paper.png")
ppr = Button(frm3,text = "PAPER",font = "Helvetica,bold",padx = 10,fg = "#003153",command = pa,image=paperp,relief=RAISED,bd=5,compound="top")
ppr.pack(side = "left")

ps = Label(frm3,bg = "#011c0a",padx = 15)
ps.pack(side = "left")

scissorp = PhotoImage(file="scissors.png")
sci = Button(frm3,text = "SCISSOR",font = "Helvetica,bold",padx = 10,fg = "#003153",command = s,image=scissorp,relief=RAISED,bd=5,compound="top")
sci.pack(side = "left")

complbl = Label(frm5,text = "Computer : ",bg = "#011c0a",fg = "White",font = ("Helvetica",25))
complbl.pack(side = "left")

comp = Label(frm5)
comp.pack(side = "left")

plbl = Label(frm7,bg = "#011c0a",fg = "White",font = ("Helvetica",25))
plbl.pack(side = "left")

pl = Label(frm7)
pl.pack(side = "left")

c = Label(frm9)
c.pack(side = "left")

vs = Label(frm9,text = "vs",font = ("Helvetica",20),bg = "#011c0a",fg = "white")
vs.pack(side = "left")

p = Label(frm9)
p.pack(side = "left")

fin = Label(frm10)
fin.pack()

resbtn = Button(frm12,text = "Reset",font = ("Helvetica",15),fg = "lavender",bg = "teal",command = res,relief=RAISED,bd=5)
resbtn.pack()

scolbl = Label(frm14,font = ("Helvetica",20),bg = "#011c0a",fg = "White")
scolbl.pack(side = "left")

score = Label(frm14,font = ("Helvetica",20),bg = "#011c0a",fg = "white")
score.pack()

scolbl1 = Label(frm16,text="Computer Score : ",font = ("Helvetica",20),bg="#011c0a",fg="White")
scolbl1.pack(side="left")

score1 = Label(frm16,font =("Helvetica",20),bg="#011c0a",fg="white")
score1.pack()

def Close(): 
    top.destroy() 
  
   
exit_button = Button(top, text="Exit",bg="#f51105",fg="white",font=("Helvetcia",10),command=Close,relief=RAISED,bd=5)  


top.mainloop()