from tkinter import *
import pandas as pd 
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("arial", 40,"italic")
WORD_FONT = ("arial",60,"bold")

data={}
row = {}


def next_card():
  global row,flip_timer
  screen.after_cancel(flip_timer)
  row = random.choice(data)
  card.itemconfig(card_language,text = "French",fill="black")
  card.itemconfig(card_word, text=row['French'],fill="black")
  card.itemconfig(card_face, image = card_front)
  flip_timer = screen.after(3000,flip_card)

def right():
  next_card()
  global data,words_to_learn
  data.remove(row)
  to_learn = pd.DataFrame(data)
  to_learn.to_csv("data/words_to_learn.csv",index=False)
  pass


  
def flip_card():
  print('flipped')
  card.itemconfig(card_language,text = "English",fill="white")
  card.itemconfig(card_word, text=row['English'],fill="white")
  card.itemconfig(card_face,image=card_back)


screen = Tk()
screen.configure(padx = 50, pady=50,bg=BACKGROUND_COLOR)
flip_timer=screen.after(3000,flip_card)
try:
  pd_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  print("No such file ... Reading data form french word file")
  pd_data = pd.read_csv("data/french_words.csv")
finally:
  data = pd_data.to_dict('records')
  print(data)

#Canvas
card = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file = "images/card_front.png")
card_back =PhotoImage(file="images/card_back.png")
card_face = card.create_image(400,263,image=card_front)
card_language = card.create_text(400,150,text="",font=LANGUAGE_FONT,fill="black")
card_word = card.create_text(400,263,text='',font=WORD_FONT,fill="black")
card.grid(column = 0,row =0,columnspan=2)


#Buttons
check_mark = PhotoImage(file="images/right.png")
right_button = Button(image=check_mark, highlightthickness=0,command=right)
right_button.grid(column = 1, row =1)


cross = PhotoImage(file="images/wrong.png")
wrong_button = Button(image = cross, highlightthickness=0,command=next_card)
wrong_button.grid(column = 0, row = 1)

next_card()



screen.mainloop()