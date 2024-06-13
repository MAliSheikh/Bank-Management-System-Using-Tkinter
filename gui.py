from datetime import datetime
import tkinter as tk
from tkinter import *
from sqlite3 import Error
from tkinter import ttk
from tkinter import ttk, messagebox
from administrator1 import *
from customer1 import *
from PIL import Image, ImageTk

class WelcomeScreen:
    def __init__(self, window):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Welcome")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)

        # Load the image file
        # bg_image = Image.open("D:\SEMESTER 5\PROG OF AI\Project\Project poi in progress\rm314-adj-05-a.png")
        bg_image = Image.open("D:\\SEMESTER 5\\PROG OF AI\\Project\\Project poi in progress\\rm314-adj-05-a.png")
        # Resize the image to fit the window size
        resized_image = bg_image.resize((self.window_width, self.window_height))
        self.resized_bg_image = ImageTk.PhotoImage(resized_image)

        # Create canvas
        self.Canvas1 = tk.Canvas(window, width=self.window_width, height=self.window_height)
        self.Canvas1.pack()

        # Display background image
        self.Canvas1.create_image(0, 0, anchor=tk.NW, image=self.resized_bg_image)


        #logo
        logo_image = Image.open(r"D:\SEMESTER 5\PROG OF AI\Project\Project poi in progress\management.png").convert("RGBA")
        resized_logo = logo_image.resize((100, 100))
        self.logo = ImageTk.PhotoImage(resized_logo)
        self.logo_label = tk.Label(window, image=self.logo, background="#00264a")
        self.logo_label.place(relx=0.2, rely=0.41, height=100 ,width=90)
        
        logo_image1 = Image.open(r"D:\SEMESTER 5\PROG OF AI\Project\Project poi in progress\management.png").convert("RGBA")
        resized_logo1 = logo_image.resize((100, 100))
        self.logo1 = ImageTk.PhotoImage(resized_logo1)
        self.logo1_label = tk.Label(window, image=self.logo, background="#00264a")
        self.logo1_label.place(relx=0.617, rely=0.41, height=100 ,width=90)
        
        # Button
        self.Button1 = tk.Button(self.Canvas1, command=self.selectEmployee, activebackground="#ececec",
                                 activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3",
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''EMPLOYEE''')
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.place(relx=0.2, rely=0.6, height=24, width=90)

        self.Button2 = tk.Button(self.Canvas1, command=self.selectCustomer, activebackground="#ececec",
                                 activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3",
                                 foreground="#f9f9f9", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''CUSTOMER''')
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.place(relx=0.617, rely=0.6, height=24, width=87)

        self.Label1 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#FFFFFF",
                               text='''PLEASE SELECT YOUR ROLE''')
        self.Label1.place(relx=0.28, rely=0.21, height=31, width=250)

    def selectEmployee(self):
        # self.window.withdraw()
        adminLogin(tk.Toplevel())

    def selectCustomer(self):
        # self.window.withdraw()
        CustomerLogin(tk.Toplevel())

if __name__ == "__main__":
    root = tk.Tk()
    welcome_screen = WelcomeScreen(root)
    root.mainloop()
