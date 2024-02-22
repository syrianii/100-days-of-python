from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  letters = ['a','b','c','d','e','f','g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  symbols =['!','#','%','$','&','(',')','*','+']

  
  random_array = []
  
  
  random_array = [choice(letters) for _ in range(randint(8,10))]
  random_array = random_array + [choice(symbols) for _ in range(randint(2,6))]
  random_array = random_array + [choice(numbers) for _ in range(randint(2,6))]
  
  shuffle(random_array)
  
  password = "".join(random_array)
  password_entry.insert(0,password)
  pyperclip.copy(password)
  
  

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
  
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {
    website:{
      "email":email,
      "password":password,
    }
  }

  if len(website) == 0 or len(password) == 0:
    messagebox.showerror("Error", "Please fill in all fields")
  else:
  
      try: 
        with open("data.json","r") as data_file:
        # reading old data
         data = json.load(data_file)
          
      except json.JSONDecodeError:
        with open("data.json",'w') as data_file:
          json.dump(new_data,data_file,indent = 4)
        # updating old data
    
      else:
        data.update(data)

        with open("data.json","w") as data_file:
          #saving updated data
         json.dump(data,data_file, indent=4)
       
        data_file.close()
        
      finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
  

# ---------------------------- SEARCH ------------------------------- #
def find_password():
  website = website_entry.get()

  try: 

   with open("data.json","r") as data_file:
    # reading old data
    data = json.load(data_file,)
   

  except:
   messagebox.showinfo("Error", "Error opening the file")
  
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title="website", message=f"Email: {email}\nPassword: {password}")
    else:
       messagebox.showinfo(title="Error", message=f"{website} was not found in database")
      
    
      
   

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx = 20, pady = 20)


canvas = Canvas(width = 200, height = 200)
img = PhotoImage(file = 'logo.png')
canvas.create_image(100,100,image = img)
canvas.grid(column = 1, row = 0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column = 0, row =1)

username_label = Label(text="Username/Email:")
username_label.grid(column = 0, row = 2)

password_label = Label(text="Password: ")
password_label.grid(column = 0, row = 3)


# Entries
website_entry = Entry(width = 21)
website_entry.grid(column = 1, row = 1,  )
website_entry.focus()
email_entry = Entry(width=34)
email_entry.grid(column = 1, row = 2, columnspan=2)
email_entry.insert(0,"someEmail@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column = 1, row = 3)


# buttons
generate_button = Button(text="Generate ",width = 8,command = generate_password)
generate_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width = 36,command=save)
add_button.grid(column = 1, row = 5, columnspan=2)

search_button = Button(text="Search",width= 8, command = find_password)
search_button.grid(column = 2,row = 1)


window.mainloop()