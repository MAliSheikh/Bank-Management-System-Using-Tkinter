# Customer have option of Deposit, Withdraw with tax amount minus, Check Branch Info, Check Balance, Change Password, Take Loan If balance is greater than 3000, and Exit
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from administrator1 import *
from PIL import Image, ImageTk

ACCOUNT_NO = 0

class CustomerLogin(tk.Toplevel):
    def __init__(self, window=None):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Costumer Login")
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
                               text='''COSTUMER LOGIN''')
        self.Label1.place(relx=0.367, rely=0.18, height=41, width=170)



        self.Label2 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''ENTER USER NAME : ''')
        self.Label2.place(relx=0.25, rely=0.35, height=21, width=100)

       
        self.Entry1 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry1.place(relx=0.5, rely=0.35, height=21, relwidth=0.264)
         #Place Holder
        self.placeholder_text = "Enter name here..."
        self.Entry1.insert(0, self.placeholder_text)
        self.Entry1.bind("<FocusIn>", self.on_entry_click)
        self.Entry1.bind("<FocusOut>", self.on_entry_leave)
        self.Entry1.place(relx=0.5, rely=0.35, height=21, relwidth=0.264)



        self.Label3 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''ENTER PIN : ''')
        self.Label3.place(relx=0.25, rely=0.45, height=21, width=100)

        self.Entry2 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry2.place(relx=0.5, rely=0.45, height=21, relwidth=0.264)

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
        #Back button
        # self.Button2 = tk.Button(window,  
        #                          activebackground="#ececec",
        #                          background="#00406c", 
        #                          foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''Back''')
        # self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
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
            self.Entry2.config(foreground='gray', show='')



    def login(self):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        # Get the name and pin 
        username = self.Entry1.get()
        pin = self.Entry2.get()

        # check name and pin in the database
        c.execute("SELECT id FROM CustomerInfo WHERE username = ? AND pin = ?", (username, pin))
        
        # Assign id to ACCOUNT_NO
        global ACCOUNT_NO
        
        customer = c.fetchone()
        print(customer)
        ACCOUNT_NO = customer[0]
        
        if customer is not None:
            print("Login successful")
            messagebox.showinfo("Login", "Login successful")
            # self.window.destroy() 
            CustomerMenu(Toplevel(self.window))
            self.window.withdraw()  # Hide the login window
        else:
            print("Invalid name or pin")
        conn.close()
        
        
        

class CustomerMenu(tk.Toplevel):
    def __init__(self, window):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Costumer Menu")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)

        # Create a canvas for the buttons
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
                               text='''COSTUMER MENU''')
        self.Label1.place(relx=0.367, rely=0.1, height=41, width=154)

        self.canvas = tk.Canvas(window, background="#FFFFFF", borderwidth="0", insertbackground="black", relief="ridge", selectbackground="blue", selectforeground="white")
        self.canvas.place(relx=0.120, rely=0.228, relheight=0.55, relwidth=0.75)

        # Create buttons
        self.deposit_button = tk.Button(self.canvas, text="Deposit", command=self.deposit, activebackground="#ececec", activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.deposit_button.place(relx=0.12, rely=0.2, height=24, width=127)

        self.withdraw_button = tk.Button(self.canvas, text="Withdraw", command=self.withdraw, activebackground="#ececec", activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.withdraw_button.place(relx=0.12, rely=0.4, height=24, width=127)

        self.check_branch_info_button = tk.Button(self.canvas, text="Check Branch Info", command=self.check_branch_info, activebackground="#ececec", activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.check_branch_info_button.place(relx=0.12, rely=0.6, height=24, width=127)

        self.check_balance_button = tk.Button(self.canvas, text="Check Balance", command=self.check_balance, activebackground="#ececec", activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.check_balance_button.place(relx=0.55, rely=0.2, height=24, width=127)

        self.change_password_button = tk.Button(self.canvas, text="Change Password", command=self.change_password, activebackground="#ececec", activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.change_password_button.place(relx=0.55, rely=0.4, height=24, width=127)

        self.take_loan_button = tk.Button(self.canvas, text="Take Loan", command=self.take_loan, activebackground="#ececec", activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", font="-family {Segoe UI} -size 10 -weight bold")
        self.take_loan_button.place(relx=0.55, rely=0.6, height=24, width=127)
        #Back button
        # self.Button2 = tk.Button(window,  
        #                          activebackground="#ececec",
        #                          background="#00406c", 
        #                          foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''Back''')
        # self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")

    def deposit(self):
        Deposit(Toplevel(self.window))
        
        
    def withdraw(self):
        Withdraw(Toplevel(self.window))

    def check_branch_info(self):
        CheckBranchInfo(Toplevel(self.window))
    
    def check_branch_info(self):
        CheckBranchInfo(self.window)
    
    def check_balance(self):
        CheckBalance(self.window)

    def change_password(self):
        ChaangePin(Toplevel(self.window))

    def take_loan(self):
        Loan(Toplevel(self.window))
    




    
class Deposit:
    def __init__(self, window=None):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Deposit")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)


        # Create a canvas for the buttons
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
                               text='''DEPOSIT AMOUNT''')
        self.Label1.place(relx=0.367, rely=0.21, height=41, width=154)

        # self.Label2 = tk.Label(window, background="#023047", disabledforeground="#a3a3a3",
        #                        font="-family {Segoe UI} -size 10", foreground="#ffffff",
        #                        text='''Account Number''')
        # self.Label2.place(relx=0.283, rely=0.311, height=21, width=104)

        # self.Entry1 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
        #                       foreground="#000000")
        # self.Entry1.place(relx=0.517, rely=0.311, height=20, relwidth=0.164)

        self.Label3 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10", foreground="#ffffff",
                               text='''AMOUNT : ''')
        self.Label3.place(relx=0.283, rely=0.35, height=21, width=64)

        self.Entry2 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry2.place(relx=0.46, rely=0.35, height=21, relwidth=0.264)

        self.Button1 = tk.Button(window, command=self.deposit, activebackground="#ececec",
                                background="#00406c", 
                                foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0",
                                text='''DEPOSIT''')
        self.Button1.place(relx=0.367, rely=0.5, height=41, width=154)
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
        #Back button
        # self.Button2 = tk.Button(window,  
        #                          activebackground="#ececec",
        #                          background="#00406c", 
        #                          foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''Back''')
        # self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
        # deposit function
    def deposit(self):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        # Get the account number and amount
        global ACCOUNT_NO
        account_number = ACCOUNT_NO
        amount = self.Entry2.get()

        # check account number in the database
        c.execute("SELECT * FROM CustomerInfo WHERE id = ?", (account_number,))
        customer = c.fetchone()

        if customer is not None:
            print("Deposit successful")
            # Update the balance in the database
            c.execute("UPDATE CustomerInfo SET initial_deposit = initial_deposit + ? WHERE id = ?", (amount, account_number))
            conn.commit()
            messagebox.showinfo("Deposit", "Deposit successful")
        else:
            print("Invalid number")
        conn.close()
        
        # Hide the deposit window
        self.window.withdraw()
        
        #Back button
        self.Button2 = tk.Button(self.window,activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''Back''')
        self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
    
    
class Withdraw:
    def __init__(self, window=None):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Withdraw")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)

         # Create a canvas for the buttons
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
                               text='''Withdraw''')
        self.Label1.place(relx=0.367, rely=0.2, height=41, width=154)


        self.Label3 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10", foreground="#ffffff",
                               text='''ENTER AMOUNT : ''')
        self.Label3.place(relx=0.2, rely=0.35, height=21, width=120)

        self.Entry2 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry2.place(relx=0.48, rely=0.35, height=21, relwidth=0.264)

        self.Button1 = tk.Button(window, command=self.withdraw, activebackground="#ececec",
                                background="#00406c", 
                                foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0",
                                text='''Withdraw''')
        self.Button1.place(relx=0.367, rely=0.49, height=41, width=154)
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
        #Back button
        # self.Button2 = tk.Button(window,  
        #                          activebackground="#ececec",
        #                          background="#00406c", 
        #                          foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''Back''')
        # self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
        # deposit function

    def withdraw(self):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        # Get the account number and amount
        global ACCOUNT_NO
        account_number = ACCOUNT_NO
        amount = int(self.Entry2.get())

        # check account number in the database
        c.execute("SELECT initial_deposit FROM CustomerInfo WHERE id = ?", (account_number,))
        customer = c.fetchone()

        if customer is not None and customer[0] >= int(amount):
            print("Deposit successful")
            # Update the balance in the database
            c.execute("UPDATE CustomerInfo SET initial_deposit = initial_deposit - ? WHERE id = ?", (int(amount) + 25, account_number))
            conn.commit()
            messagebox.showinfo("Withdraw", "Withdraw successful with tax amount of 25")
        else:
            print("Invalid Amount")
            messagebox.showinfo("Withdraw", "Invalid Amount")
        conn.close()
        
        # Hide the deposit window
        self.window.withdraw()

        


class CheckBranchInfo(tk.Toplevel):
    def __init__(self, window=None):
        super().__init__(window)  # Call the __init__ method of the superclass
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.geometry(f"{self.window_width}x{self.window_height}")
        self.title("Check Branch Information")
        self.minsize(500, 600)
        self.maxsize(500, 600)
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#00406c", foreground="#ffffff")
        style.configure("TEntry", font=("Helvetica", 12))


        # self.Label1 = tk.Label(window, background="#023047", disabledforeground="#a3a3a3",
        #                        font="-family {Segoe UI} -size 13 -weight bold", foreground="#ffffff",
        #                        text='''BRANCH INFORMATION''')
        # self.Label1.place(relx=0.367, rely=0.089, height=41, width=154)
        self.account_id_label = ttk.Label(self, text="Branch Information", style="TLabel")
        self.account_id_label.pack(pady=10)
        
        self.check_button = ttk.Button(self, text="Check Branch Info", command=self.check_account_summary)
        self.check_button.pack(pady=10)

        self.summary_text = tk.Text(self, height=10, width=40, bg="#d9d9d9", font=("Helvetica", 12))
        self.summary_text.pack(pady=10)
        
    
    def check_account_summary(self):    
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        
        c.execute("SELECT branch_number, branch_name FROM CustomerInfo where id = ?", (ACCOUNT_NO,))
        branch_info = c.fetchone() 
        conn.close()

        if branch_info is not None:  
            summary = f"Branch Code: {branch_info[0]}\n"  
            summary += f"Branch Name: {branch_info[1]}\n" 

            self.summary_text.delete(1.0, tk.END)
            self.summary_text.insert(tk.END, summary)

        
        


class CheckBalance(tk.Toplevel):
    def __init__(self, window=None):
        super().__init__(window)  
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.geometry(f"{self.window_width}x{self.window_height}")
        self.title("Check Acoount Balance")
        self.minsize(500, 600)
        self.maxsize(500, 600)
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#023047", foreground="#ffffff")
        style.configure("TEntry", font=("Helvetica", 12))


        # self.Label1 = tk.Label(window, background="#023047", disabledforeground="#a3a3a3",
        #                        font="-family {Segoe UI} -size 13 -weight bold", foreground="#ffffff",
        #                        text='''BRANCH INFORMATION''')
        # self.Label1.place(relx=0.367, rely=0.089, height=41, width=154)
        self.account_id_label = ttk.Label(self, text="Check Balance", style="TLabel")
        self.account_id_label.pack(pady=10)
        
        self.check_button = ttk.Button(self, text="Check Balance", command=self.check_account_balance)
        self.check_button.pack(pady=10)

        self.summary_text = tk.Text(self, height=10, width=40, bg="#d9d9d9", font=("Helvetica", 12))
        self.summary_text.pack(pady=10)
        
    
    def check_account_balance(self):    
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        
        c.execute("SELECT initial_deposit FROM CustomerInfo where id = ?", (ACCOUNT_NO,))
        balance = c.fetchone()  
        conn.close()

        if balance is not None:  
            summary = f"Account No: {ACCOUNT_NO}\n"  
            summary += f"Branch Name: {balance[0]}\n" 

            self.summary_text.delete(1.0, tk.END)
            self.summary_text.insert(tk.END, summary)


     
     
class ChaangePin:
    def __init__(self, window=None):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Withdraw")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)
        window.configure(background="#023047")
        window.configure(cursor="arrow")

         # Create a canvas for the buttons
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
                            text='''CHANGE PASSWORD''')
        self.Label1.place(relx=0.367, rely=0.25, height=41, width=165)

        self.Label3 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10", foreground="#ffffff",
                               text='''NEW PIN : ''')
        self.Label3.place(relx=0.3, rely=0.4, height=21, width=70)

        self.Entry2 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry2.place(relx=0.48, rely=0.4, height=21, relwidth=0.264)

        self.Button1 = tk.Button(window, command=self.change_pin, activebackground="#ececec",
                                background="#00406c", 
                                foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0",
                                text='''CHANGE PIN''')
        self.Button1.place(relx=0.367, rely=0.55, height=41, width=154)
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        #Back button
        self.Button2 = tk.Button(window,  
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''Back''')
        self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
        # changepin function
    def change_pin(self):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        # Get the account number and amount
        global ACCOUNT_NO
        account_number = ACCOUNT_NO
        new_pin = self.Entry2.get()

        # check account number in the database
        c.execute("SELECT * FROM CustomerInfo WHERE id = ?", (account_number,))
        customer = c.fetchone()

        if customer is not None:
            print("Pin Change successful")
            # Update the balance in the database
            c.execute("UPDATE CustomerInfo SET pin = ? WHERE id = ?", (new_pin, account_number))
            conn.commit()
            messagebox.showinfo("Pin Change", "Pin Change successful")
        else:
            print("Invalid Pin")
        conn.close()
        
        # Hide the deposit window
        self.window.withdraw()
           
        
  
class Loan:
    def __init__(self, window=None):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Withdraw")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)
        window.configure(background="#023047")
        window.configure(cursor="arrow")

         # Create a canvas for the buttons
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
                               text='''LOAN''')
        self.Label1.place(relx=0.367, rely=0.25, height=41, width=154)

        self.Label3 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10", foreground="#ffffff",
                               text='''ENTER AMOUNT :''')
        self.Label3.place(relx=0.2, rely=0.45, height=21, width=130)

        self.Entry2 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry2.place(relx=0.48, rely=0.45, height=21, relwidth=0.264)

        self.Button1 = tk.Button(window, command=self.take_loan, activebackground="#ececec",
                                background="#00406c", 
                                foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0",
                                text='''TAKE LOAN''')
        self.Button1.place(relx=0.367, rely=0.6, height=41, width=154)
        #Back button
        # self.Button2 = tk.Button(window,  
        #                          activebackground="#ececec",
        #                          background="#00406c", 
        #                          foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''Back''')
        # self.Button2.place(relx=0.7, rely=0.9, height=25, width=100)
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        
        # Loan function
    def take_loan(self):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        # Get the account number and amount
        global ACCOUNT_NO
        account_number = ACCOUNT_NO
        amount = int(self.Entry2.get())

        # check account number in the database
        c.execute("SELECT initial_deposit,account_type FROM CustomerInfo WHERE id = ?", (account_number,))
        customer = c.fetchone()
        print(customer[1])
        # Loan will only for those whose account balance is greater than 3000 and type is current
        if customer is not None and customer[0] > 3000 and customer[1] == "Current":
            print("Loan successful")
            # Update the balance in the database
            c.execute("UPDATE CustomerInfo SET initial_deposit = initial_deposit + ? WHERE id = ?", (amount, account_number))
            conn.commit()
            messagebox.showinfo("Loan Approved", "Loan has been approved")
            
        else:
            messagebox.showinfo("Loan Denied", "Account type is saving, can't take loan")
            print("Invalid Amount")
        self.window.withdraw()

         
    

