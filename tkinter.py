
import tkinter as tk

from click import command
from emailit import *

root=tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
email_address=tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    weekly
    emailadd=email_address.get()
    emailto(emailadd)
    email_address.set("")

def weeklyplan():
    email_label = tk.Label(root, text = 'Email address: ', font=('calibre',10, 'bold'))

    # creating a entry for input
    # name using widget Entry
    email_entry = tk.Entry(root,textvariable = email_address, font=('calibre',10,'normal'))


    # creating a button using the widget
    # Button that will call the submit function
    submit_button=tk.Button(root,text = 'Submit', command = submit)
	
        
    # placing the label and entry in
    # the required position using grid
    # method
    email_label.grid(row=0,column=0)
    email_entry.grid(row=0,column=1)
    submit_button.grid(row=2,column=1)
    
    
# creating a label 
welcome="What are you looking for"
welcome=tk.Label(root,text='',font=('calibre',15, 'bold'))

dailyp=tk.Label(root,text='Daily meal plan',font=('calibre',12, 'bold'), command=daily)
weeklyp=tk.Label(root,text='Weekly meal plan',font=('calibre',15, 'bold'), command=weeklyplan)





