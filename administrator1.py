import os  
from datetime import datetime
import tkinter as tk
from tkinter import *
from sqlite3 import Error
import sqlite3
from tkinter import ttk
import datetime
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from gui import WelcomeScreen


# class for admin login
class adminLogin:
    def __init__(self, window=None, welcome_screen=None):
        self.window = window
        self.welcome_screen = welcome_screen
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Administrator Login")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)

        bg_image = Image.open("D:\\SEMESTER 5\\PROG OF AI\\Project\\Project poi in progress\\rm314-adj-05-a.png")

        # Resize the image to fit the window size
        resized_image = bg_image.resize((self.window_width, self.window_height))
        self.resized_bg_image = ImageTk.PhotoImage(resized_image)

        # Create canvas
        self.Canvas1 = tk.Canvas(window, width=self.window_width, height=self.window_height)
        self.Canvas1.pack()

        # Display background image
        self.Canvas1.create_image(0, 0, anchor=tk.NW, image=self.resized_bg_image)

        self.Label1 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#ffffff",
                               text='''ADMIN LOGIN''')
        self.Label1.place(relx=0.367, rely=0.18, height=41, width=160)



        self.Label2 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''ENTER NAME : ''')
        self.Label2.place(relx=0.25, rely=0.35, height=21, width=100)

       
        self.Entry1 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry1.place(relx=0.5, rely=0.35, height=20, relwidth=0.264)
         #Place Holder
        self.placeholder_text = "Enter name here..."
        self.Entry1.insert(0, self.placeholder_text)
        self.Entry1.bind("<FocusIn>", self.on_entry_click)
        self.Entry1.bind("<FocusOut>", self.on_entry_leave)
        self.Entry1.place(relx=0.5, rely=0.35, height=20, relwidth=0.264)



        self.Label3 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''ENTER PIN : ''')
        self.Label3.place(relx=0.25, rely=0.45, height=21, width=100)

        self.Entry2 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry2.place(relx=0.5, rely=0.45, height=20, relwidth=0.264)

         #Place Holder
        self.placeholder_text2 = "Enter your pin..."
        self.Entry2.insert(0, self.placeholder_text2)
        self.Entry2.bind("<FocusIn>", self.on_entry_click2)
        self.Entry2.bind("<FocusOut>", self.on_entry_leave2)
        self.Entry2.place(relx=0.5, rely=0.45, height=20, relwidth=0.264)


        self.Button1 = tk.Button(window, 
                                 command=self.login, 
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''LOGIN''')
        self.Button1.place(relx=0.367, rely=0.6, height=41, width=154)  # Adjust the relx, rely, height, and width as needed
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")

        #Back button goes to the main menu
        # self.Button2 = tk.Button(window,  activebackground="#ececec", background="#00406c", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''Back''')
        # self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
    
        # self.window.destroy()

    #Feild1
    def on_entry_click(self, event):
        if self.Entry1.get() == self.placeholder_text:
            self.Entry1.delete(0, tk.END)
            self.Entry1.config(foreground='Black')

    def on_entry_leave(self, event):
        if self.Entry1.get() == '':
            self.Entry1.insert(0, self.placeholder_text)
            self.Entry1.config(foreground='gray')
    #feild2
    def on_entry_click2(self, event):
        if self.Entry2.get() == self.placeholder_text2:
            self.Entry2.delete(0, tk.END)
            self.Entry2.config(foreground='Black', show='x')

    def on_entry_leave2(self, event):
        if self.Entry2.get() == '':
            self.Entry2.insert(0, self.placeholder_text2)
            self.Entry2.config(foreground='gray', show='')  # Adjust the relx, rely, height, and width as needed

        
    def login(self):
        
        id = int(self.Entry1.get())
        password = self.Entry2.get()
        print(id,password)
        
        if id == 123 and password == '123':
                print("Login successful")
                messagebox.showinfo("Login Successful", "Login successful")
                # Redirect to adminMenu screen here
                AdminMenu(Toplevel(self.window))
        else:
                messagebox.showerror("Login Failed", "Invalid credentials")
                print("Invalid credentials")



class AdminMenu:
    def __init__(self, window):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Create Account")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)

        bg_image = Image.open("D:\\SEMESTER 5\\PROG OF AI\\Project\\Project poi in progress\\rm314-adj-05-a.png")

        # Resize the image to fit the window size
        resized_image = bg_image.resize((self.window_width, self.window_height))
        self.resized_bg_image = ImageTk.PhotoImage(resized_image)

        # Create canvas
        self.Canvas1 = tk.Canvas(window, width=self.window_width, height=self.window_height)
        self.Canvas1.pack()

        # Display background image
        self.Canvas1.create_image(0, 0, anchor=tk.NW, image=self.resized_bg_image)

        # Create a canvas for the buttons
        self.canvas = tk.Canvas(window, background="#ffffff", borderwidth="0", insertbackground="black",
                                relief="ridge", selectbackground="blue", selectforeground="white")
        self.canvas.place(relx=0.190, rely=0.228, relheight=0.496, relwidth=0.622)

        # Create buttons
        self.create_account_button = tk.Button(self.canvas, text="Create Account", command=self.create_account,
                                               activebackground="#ececec", activeforeground="#000000",
                                               background="#023047", disabledforeground="#a3a3a3",
                                               foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                               highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.create_account_button.place(relx=0.161, rely=0.333, height=24, width=127)

        self.check_account_summary_button = tk.Button(self.canvas, text="Check Account Summary", command=self.check_account_summary,
                                                      activebackground="#ececec", activeforeground="#000000",
                                                      background="#023047", disabledforeground="#a3a3a3",
                                                      foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                                      highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.check_account_summary_button.place(relx=0.161, rely=0.583, height=24, width=187)
        #Back button
        # self.Button2 = tk.Button(window,  
        #                          activebackground="#ececec",
        #                          background="#00406c", 
        #                          foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''Back''')
        # self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")

    
    def create_account(self):
        create_account_window = CreateCustomerAccount(self.window)

    def check_account_summary(self):
        check_account_window = CheckAccountSummary(self.window)

    def __del__(self):
        self.conn.close()




class CreateCustomerAccount(tk.Toplevel):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.geometry(f"{self.window_width}x{self.window_height}")
        self.title("Create Customer Account")
        self.minsize(500, 600)
        self.maxsize(500, 600)

        # Name
        self.Label1 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='FULL NAME : ')
        self.Label1.place(relx=0.15, rely=0.099, height=27, width=175)

        self.Entry1 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry1.place(relx=0.6, rely=0.099, height=20, relwidth=0.302)

        # Username
        self.Label16 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='USER NAME : ')
        self.Label16.place(relx=0.15, rely=0.174, height=27, width=175)

        self.Entry16 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry16.place(relx=0.6, rely=0.174, height=20, relwidth=0.302)

        # Date Of Birth
        self.Label2 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff",
                               highlightcolor="black", text='DOB(DD/MM/YYYY) : ')
        self.Label2.place(relx=0.15, rely=0.238, height=27, width=175)

        self.Entry2 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry2.place(relx=0.6, rely=0.238, height=20, relwidth=0.302)

        # Gender
        self.Label3 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='GENDER : ')
        self.Label3.place(relx=0.15, rely=0.397, height=27, width=175)

        self.gender = tk.StringVar()

        self.Radiobutton3 = tk.Radiobutton(self, activebackground="#ececec", activeforeground="#000000",
                                           background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                           highlightcolor="black", justify='left', variable=self.gender, value="Male",
                                           text='Male')
        self.Radiobutton3.place(relx=0.55, rely=0.397, relheight=0.055, relwidth=0.175)

        self.Radiobutton4 = tk.Radiobutton(self, activebackground="#ececec", activeforeground="#000000",
                                           background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                           highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                           variable=self.gender, value="Female", text='Female')
        self.Radiobutton4.place(relx=0.7, rely=0.397, relheight=0.055, relwidth=0.175)

        # Nationality
        self.Label4 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='NATIONALITY : ')
        self.Label4.place(relx=0.15, rely=0.471, height=21, width=175)

        self.Entry4 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry4.place(relx=0.6, rely=0.471, height=20, relwidth=0.302)

        # Phone number
        self.Label5 = tk.Label(self, activebackground="#f9f9f9", activeforeground="black", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff",
                               highlightcolor="black", text='MOBILE NUMBER : ')
        self.Label5.place(relx=0.15, rely=0.323, height=22, width=175)

        self.Entry5 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry5.place(relx=0.6, rely=0.323, height=20, relwidth=0.302)

        # Account type
        self.Label6 = tk.Label(self, activebackground="#f9f9f9", activeforeground="black", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='ACCOUNT TYPE : ')
        self.Label6.place(relx=0.15, rely=0.545, height=26, width=175)

        self.acc_type = tk.StringVar()

        self.Radiobutton1 = tk.Radiobutton(self, activebackground="#ececec", activeforeground="#000000",
                                           background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                           highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                           variable=self.acc_type, value="Savings", text='Savings')
        
        self.Radiobutton1.place(relx=0.59, rely=0.55, relheight=0.057, relwidth=0.151)

        self.Radiobutton1_1 = tk.Radiobutton(self, activebackground="#ececec", activeforeground="#000000",
                                             background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                             highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                             variable=self.acc_type, value="Current", text='Current')
        self.Radiobutton1_1.place(relx=0.75, rely=0.55, relheight=0.057, relwidth=0.175)
        
        # PIN
        self.Label8 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='PIN : ')
        self.Label8.place(relx=0.15, rely=0.619, height=21, width=175)
        self.Entry8 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white", show="*")  # Show asterisks for PIN
        self.Entry8.place(relx=0.6, rely=0.619, height=20, relwidth=0.302)

        # Initial Deposit
        self.Label9 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='INITIAL DEPOSIT : ')
        self.Label9.place(relx=0.15, rely=0.693, height=21, width=175)
        self.Entry9 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry9.place(relx=0.6, rely=0.693, height=20, relwidth=0.302)

        # Loan Amount
        self.Label10 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                                disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                                highlightcolor="black", text='LOAN AMOUNT : ')
        self.Label10.place(relx=0.15, rely=0.767, height=21, width=175)
        self.Entry10 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                                font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                                highlightcolor="black", insertbackground="black", selectbackground="blue",
                                selectforeground="white")
        self.Entry10.place(relx=0.6, rely=0.767, height=20, relwidth=0.302)

        # Branch Number
        self.Label11 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                                disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                                highlightcolor="black", text='BRANCH NUMBER : ')
        self.Label11.place(relx=0.15, rely=0.841, height=21, width=175)
        self.Entry11 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                                font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                                highlightcolor="black", insertbackground="black", selectbackground="blue",
                                selectforeground="white")
        self.Entry11.place(relx=0.6, rely=0.841, height=20, relwidth=0.302)

        # Branch Name
        self.Label12 = tk.Label(self, activebackground="#f9f9f9", activeforeground="white", background="#00406c",
                                disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                                highlightcolor="black", text='BRANCH NAME : ')
        self.Label12.place(relx=0.15, rely=0.915, height=21, width=175)
        self.Entry12 = tk.Entry(self, background="#cae4ff", disabledforeground="#a3a3a3",
                                font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                                highlightcolor="black", insertbackground="black", selectbackground="blue",
                                selectforeground="white")
        self.Entry12.place(relx=0.6, rely=0.915, height=20, relwidth=0.302)
        
        self.save_button = tk.Button(self, text="SAVE", command=self.get_unique_username, background="#00406c", foreground="#ffffff")
        self.save_button.place(relx=0.7, rely=0.95, anchor='center', width=100)  # Adjust the position as needed
        self.save_button.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
    def save_data(self):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        

        # Get values from the form
        name = self.Entry1.get()
        username = self.Entry16.get()
        dob = self.Entry2.get()
        gender = self.gender.get()
        nationality = self.Entry4.get()
        phone = self.Entry5.get()
        account_type = self.acc_type.get()
        pin = self.Entry8.get()
        initial_deposit = float(self.Entry9.get())
        loan_amount = float(self.Entry10.get())
        branch_number = int(self.Entry11.get())
        branch_name = self.Entry12.get()

        values = (name, username, dob, gender, nationality, phone, account_type, pin, initial_deposit, loan_amount, branch_number, branch_name)
        
        c.execute("""
            INSERT INTO CustomerInfo (name, username, dob, gender, nationality, phone, account_type, pin, initial_deposit, loan_amount, branch_number, branch_name)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, values)

        conn.commit()
        conn.close()
        self.destroy()  # Close the window after submitting the data    
        
    def get_unique_username(self):
        conn = sqlite3.connect('bank.db')  # replace with your database name
        c = conn.cursor()
        
        c.execute("""
            CREATE TABLE IF NOT EXISTS CustomerInfo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                username TEXT,
                dob TEXT,
                gender TEXT,
                nationality TEXT,
                phone TEXT,
                account_type TEXT,
                pin TEXT,
                initial_deposit REAL,
                loan_amount REAL,
                branch_number INTEGER,
                branch_name TEXT,
                DateTime datetime DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        username = self.Entry16.get()
        c.execute("SELECT * FROM CustomerInfo WHERE username=?", (username,))
        result = c.fetchone()

        if result:
            messagebox.showinfo("Username taken", "This username is taken. Please choose another one.")
        else:
            self.save_data()
            messagebox.showinfo("Success", "Account created successfully!")

        conn.commit()
        conn.close()
  
  
  
      
class CheckAccountSummary(tk.Toplevel):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Check Account Summary")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)

        bg_image = Image.open("D:\\SEMESTER 5\\PROG OF AI\\Project\\Project poi in progress\\rm314-adj-05-a.png")

        # Resize the image to fit the window size
        resized_image = bg_image.resize((self.window_width, self.window_height))
        self.resized_bg_image = ImageTk.PhotoImage(resized_image)

        # Create canvas
        self.Canvas1 = tk.Canvas(window, width=self.window_width, height=self.window_height)
        self.Canvas1.pack()

        # Display background image
        self.Canvas1.create_image(0, 0, anchor=tk.NW, image=self.resized_bg_image)
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#023047", foreground="#ffffff")
        style.configure("TEntry", font=("Helvetica", 12))

        self.account_username_label = ttk.Label(self, text="Account User name")
        self.account_username_label.pack(pady=10)
        self.account_username_entry = ttk.Entry(self)
        self.account_username_entry.pack(pady=5)
        style.configure("Custom.TButton", background="#00406c", foreground="#ffffff")
        
        self.check_button = ttk.Button(self, text="CHECK SUMMRY", command=self.check_account_summary, style="Custom.TButton")
        self.check_button.pack(pady=10)

        self.summary_text = tk.Text(self, height=10, width=40, bg="#ffffff", font=("Helvetica", 12))
        self.summary_text.pack(pady=10)

    def check_account_summary(self):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        username = self.account_username_entry.get()

        c.execute("SELECT * FROM CustomerInfo WHERE username = ?", (username,))
        account_info = c.fetchone()

        if account_info:
            summary = f"Account ID: {account_info[0]}\n"
            summary += f"Name: {account_info[1]}\n"
            summary += f"User Name: {account_info[2]}\n"
            summary += f"Date of Birth: {account_info[3]}\n"
            summary += f"Gender: {account_info[5]}\n"
            summary += f"Nationality: {account_info[6]}\n"
            summary += f"Email: {account_info[7]}\n"
            summary += f"Address: {account_info[8]}\n"
            summary += f"Phone: {account_info[9]}\n"
            summary += f"Account Type: {account_info[10]}\n"
            summary += f"Initial Deposit: {account_info[11]}\n"
            summary += f"Loan Amount: {account_info[12]}\n"

            self.summary_text.delete(1.0, tk.END)
            self.summary_text.insert(tk.END, summary)
        else:
            messagebox.showerror("Error", "Account not found.")

        conn.close()


