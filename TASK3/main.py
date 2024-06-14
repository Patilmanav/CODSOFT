'''
TASK 3
PASSWORD GENERATOR
A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to generate a password of the specified length.
Display the Password: Print the generated password on the screen.
'''

import tkinter as tk
from tkinter import ttk,font,scrolledtext
import string
import random

class GUI():
    def __init__(self,master) -> None:
        
        self.len_text = tk.IntVar()
        self.ch_capital = tk.IntVar()
        self.ch_small = tk.IntVar()
        self.ch_digit = tk.IntVar()
        self.ch_special_char = tk.IntVar()
        ch_font =font.Font(size=10)
        
        main_lbl = tk.Label(master=master,text="PASSWORD GENERATOR",padx=20,pady=20,font=font.Font(weight="bold"))
        main_lbl.grid(column=0,row=0,columnspan=2)
        
        len_lbl = tk.Label(master=master,text="Enter The length: ",padx=10,pady=10)
        len_lbl.grid(column=0,row=1)
        
        len_et = tk.Entry(master=master,textvariable=self.len_text)
        len_et.grid(column=1,row=1,padx=15,pady=10)
        
        len_lbl = tk.Label(master=master,text="Select Atleast One: ",padx=10,pady=10,font=font.Font(weight="bold",size=12))
        len_lbl.grid(column=0,row=2,columnspan=2)
        
        chbox1 = tk.Checkbutton(master=master,text="Capital letters (A - Z)",variable=self.ch_capital,font=ch_font)
        chbox1.grid(column=0,row=3,columnspan=2,padx=15,pady=(5,5),sticky=tk.W)
        
        chbox2 = tk.Checkbutton(master=master,text="Small letters (a - z)",variable=self.ch_small,font=ch_font)
        chbox2.grid(column=0,row=4,columnspan=2,padx=15,pady=(5,5),sticky=tk.W)
        
        chbox3 = tk.Checkbutton(master=master,text="Digits (0 - 9)",variable=self.ch_digit,font=ch_font)
        chbox3.grid(column=0,row=5,columnspan=2,padx=15,pady=(5,5),sticky=tk.W)
        
        chbox4 = tk.Checkbutton(master=master,text="Special Characters (@#$...)",variable=self.ch_special_char,font=ch_font)
        chbox4.grid(column=0,row=6,columnspan=2,padx=15,pady=(5,5),sticky=tk.W)
        
        submit = tk.Button(master=master,text="Generate Password",command=self.generatePassword)
        submit.grid(column=0,row=7,columnspan=2,padx=15,pady=5)
        
        self.pass_lbl = tk.Label(master=master,text="Your password is  ",font=font.Font(size=11),wraplength=180)
        self.pass_lbl.grid(column=0,row=8,padx=15,pady=5,columnspan=3)
        self.textArea = scrolledtext.ScrolledText(master=master,wrap = tk.WORD,width = 40,height = 5,font = ("Times New Roman", 15))
        self.textArea.tag_config("colored",foreground="red")
        
        self.textArea.grid(column=0,row=9,columnspan=2)
    
    def generatePassword(self):        
        characters = ""
        password = ""
        if(self.ch_capital.get()):
            characters+= string.ascii_uppercase
        
        if(self.ch_small.get()):
            characters+= string.ascii_lowercase
        
        if(self.ch_digit.get()):
            characters+= string.digits
        
        if(self.ch_special_char.get()):
            characters+= string.punctuation
        
        if self.len_text.get() <= 0:
            self.textArea.delete("1.0",tk.END)
            self.textArea.insert(tk.INSERT,"ERROR: Lenth should not be 0 or negative","colored")            
            
        else:
            try:
                for i in range(self.len_text.get()):
                    password += random.choice(characters)
                    self.textArea.delete("1.0",tk.END)
                    self.textArea.insert(tk.INSERT,password,"colored")            
                    
            except IndexError as ie:
                self.textArea.delete("1.0",tk.END)
                self.textArea.insert(tk.INSERT,"Please Select Aleast One CheckBox","colored")            
                
            except Exception as e:
                self.textArea.delete("1.0",tk.END)
                self.textArea.insert(tk.INSERT,str(e),"colored")            
                
root = tk.Tk()
# root.geometry("300x400")
root.resizable(False,False)
GUI(root)
root.mainloop()