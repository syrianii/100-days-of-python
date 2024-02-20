Dimport tkinter

window = tkinter.Tk()
window.title("Miles to kilometer converter")


def convert():
  equal["text"] = round(int(input.get()) * 1.60934,1)

input = tkinter.Entry()
input.grid(column=1,row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column = 2, row = 0)

text = tkinter.Label(text="is equal to")
text.grid(column = 0, row = 1) 

equal = tkinter.Label(text="0")
equal.grid(column = 1,row=1)

km_label = tkinter.Label(text="KM")
km_label.grid(column = 2, row = 1)

button = tkinter.Button(text="Calculate",command=convert)
button.grid(column = 1, row = 2)



window.mainloop()
