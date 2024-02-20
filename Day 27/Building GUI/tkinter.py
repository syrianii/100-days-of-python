import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="New text",font=("Arial",14,"bold"))
my_label.grid(column = 0,row =0)


def button_clicked():
  my_label['text'] = input.get()
  
button = tkinter.Button(text="click me",command=button_clicked)
button.grid(row = 1,column=1)

new_button = tkinter.Button(text="new button")
new_button.grid(column=2,row=0)
input = tkinter.Entry()
input.grid(column=4,row=4)



window.mainloop()



