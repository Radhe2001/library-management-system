from tkinter import *
import mysql.connector
from datetime import datetime
import pytz

# establishing mysql connection
con = mysql.connector.connect(host="localhost",port=3306,user="root",password="1234",database="lms")
cur = con.cursor()


# defining issue book interface
class IssueBook:
    def __init__(self,registration_number):
        self.registration_number = registration_number
        # creating root
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.title("Library Management System")
        self.bookName = StringVar()
        
        # creating heading label
        label1 = Label(self.root, text="Issue Book",fg="Blue",font="italic",pady=10)
        label1.place(x=180,y=50)
        
        
        # creating first label
        label2 = Label(self.root, text="Book name : ",fg="red",font="italic")
        label2.place(x=100,y=190)
        
        # search input field
        bookName_entry = Entry(self.root,textvariable = self.bookName, font=('calibre',10,'normal'))
        bookName_entry.place(x=210,y=190)
        

        # creating button for issuing book
        btn1 = Button(self.root, text = 'Issue', bd = '6',fg="white",bg="brown",command=self.issue)
        btn1.place(x=170,y=260)
        
        # creating third label
        self.label3 = Label(self.root,fg="red",font="italic")
        self.label3.place(x=160,y=330)

        self.root.mainloop()
        
        
    def issue(self):
        bookName = str(self.bookName.get())
        try:
            cur.execute("select * from book_list where book_name = \'%s\'"%bookName)
            result = cur.fetchall()
            if not(len(result)==1):
                self.label3.config(text="no such book exists")
            elif result[0][3]==0:
                self.label3.config(text="book is not available , sorry")
            else:
                try:
                    cur.execute("update book_list set avl_book = %s where book_name = \'%s\'"%((result[0][3]-1),bookName))
                    con.commit()
                    date = str(datetime.now(pytz.timezone('Asia/Kolkata')))
                    try:
                        query = "insert into book_log values(%s,%s,%s,%s)"
                        tuple = (self.registration_number,result[0][0],date,"Issue")
                        cur.execute(query,tuple)
                        con.commit()
                    except:
                        print("failed to issue book")
                    self.label3.config(text="book issued")
                except:
                    print("sql exception")
        except:
            print("sql exception")


# defining submit book inerface
class SubmitBook:
    def __init__(self,registration_number):
        self.registration_number = registration_number
        # creating root
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.title("Library Management System")
        self.bookName = StringVar()
        
        # creating heading label
        label1 = Label(self.root, text="Submit Book",fg="Blue",font="italic",pady=10)
        label1.place(x=180,y=50)
        
        
        # creating first label
        label2 = Label(self.root, text="Book name : ",fg="red",font="italic")
        label2.place(x=100,y=190)
        
        # search input field
        bookName_entry = Entry(self.root,textvariable = self.bookName, font=('calibre',10,'normal'))
        bookName_entry.place(x=210,y=190)
        

        # creating button for issuing book
        btn1 = Button(self.root, text = 'Submit', bd = '6',fg="white",bg="brown",command=self.submit)
        btn1.place(x=170,y=260)
        
        # creating third label
        self.label3 = Label(self.root,fg="red",font="italic")
        self.label3.place(x=160,y=330)

        self.root.mainloop()
        
        
    def submit(self):
        bookName = str(self.bookName.get())
        try:
            cur.execute("select * from book_list where book_name = \'%s\'"%bookName)
            result = cur.fetchall()
            if not(len(result)==1):
                self.label3.config(text="no such book exists")
            else:
                try:
                    cur.execute("update book_list set avl_book = %s where book_name = \'%s\'"%((result[0][3]+1),bookName))
                    con.commit()
                    date = str(datetime.now(pytz.timezone('Asia/Kolkata')))
                    try:
                        query = "insert into book_log values(%s,%s,%s,%s)"
                        tuple = (self.registration_number,result[0][0],date,"Submit")
                        cur.execute(query,tuple)
                        con.commit()
                    except:
                        print("failed to submit book")
                    self.label3.config(text="book submitted")
                except:
                    print("sql exception")
        except:
            print("sql exception")


# defining student interface page
class StudentInterface:
    def __init__(self,registation_number):
        self.registration_number = registation_number
        # creating root
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title("Library Management System")
        self.bookName = StringVar()
        
        # creating heading label
        label1 = Label(self.root, text="Greetings of the day",fg="Blue",font="italic",pady=10)
        label1.place(x=180,y=50)
        
        # creating sub-heading label
        label2 = Label(self.root, text="how may i help you ?",fg="Blue",font="italic",pady=10)
        label2.place(x=180,y=90)

        # search label
        label3 = Label(self.root, text="Search book",fg="red",font=('calibre',15,'bold'))
        label3.place(x=360,y=150)
        
        # another label
        label4 = Label(self.root, text="Book name :",fg="red",font=('calibre',10,'bold'))
        label4.place(x=310,y=190)
        
        # search input field
        pass_entry = Entry(self.root,textvariable = self.bookName, font=('calibre',10,'normal'))
        pass_entry.place(x=400,y=190)
        
        # creating first label
        label5 = Label(self.root, text="Issue book",fg="red",font="italic")
        label5.place(x=190,y=310)
        
        # creating second label
        label6 = Label(self.root, text="Submit book",fg="red",font="italic")
        label6.place(x=190,y=380)

        # creating button for issuing book
        btn1 = Button(self.root, text = 'Issue', bd = '6',fg="white",bg="brown",command=self.issue)
        btn1.place(x=330,y=310)

        # creating button for submit book
        btn2 = Button(self.root, text = 'Submit', bd = '6',fg="white",bg="brown",command=self.submit)
        btn2.place(x=330,y=380)  
        
        # creating button for issuing book
        btn3 = Button(self.root, text = 'Search', bd = '6',fg="white",bg="brown",command=self.search)
        btn3.place(x=390,y=240)

        self.root.mainloop()
        
    def issue(self):
        self.root.destroy()
        IssueBook(self.registration_number)
    
    def submit(self):
        self.root.destroy()
        SubmitBook(self.registration_number)
    
    def search(self):
        
        book = str(self.bookName.get())
        
        try:
            cur.execute("select * from book_list where book_name = \'%s\'"%book)
            result = cur.fetchall()
            
            if len(result) ==0:
                print("no such book")
            else:
                # creating parent
                parent = Tk()
                parent.geometry("400x400")
                parent.title("Library Management System")
                
                # creating heading label
                label1 = Label(parent, text="Search result",fg="Blue",font="italic",pady=10)
                label1.place(x=180,y=50)
                
                
                label2 = Label(parent, text="Book Name : ",fg="Blue",font="italic",pady=10)
                label2.place(x=80,y=150)
                
                label3 = Label(parent, text="Author : ",fg="Blue",font="italic",pady=10)
                label3.place(x=80,y=200)
                
                label4 = Label(parent, text="Available book : ",fg="Blue",font="italic",pady=10)
                label4.place(x=80,y=250)
                
                label5 = Label(parent,text=result[0][1],fg="Blue",font="italic",pady=10)
                label5.place(x=230,y=150)
                
                label6 = Label(parent,text=result[0][2],fg="Blue",font="italic",pady=10)
                label6.place(x=230,y=200)
                
                label7 = Label(parent,text=result[0][3],fg="Blue",font="italic",pady=10)
                label7.place(x=230,y=250)
                
                parent.mainloop()
        except:
            print("sql exception")


# defining student registration page
class StudentRegister:
    # constructor
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title("Library Management System")
        
        self.registration=StringVar()
        self.password=StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        self.course = StringVar()

        # creating heading label
        label1 = Label(self.root, text="Student Login",fg="Blue",font="italic",pady=30)
        label1.place(x=260,y=50)

        # creating registration id label
        label2 = Label(self.root, text="Enter registration id",fg="red",font=('calibre',10,'bold'))
        label2.place(x=170,y=150)
        
        # creating password label
        label3 = Label(self.root, text="Enter password",fg="red",font=('calibre',10,'bold'))
        label3.place(x=170,y=190)
        
        # creating name label
        label4 = Label(self.root, text="Enter name",fg="red",font=('calibre',10,'bold'))
        label4.place(x=170,y=230)
        
        # creating email label
        label5 = Label(self.root, text="Enter email",fg="red",font=('calibre',10,'bold'))
        label5.place(x=170,y=270)
        
        # creating contact label
        label6 = Label(self.root, text="Enter contact",fg="red",font=('calibre',10,'bold'))
        label6.place(x=170,y=310)
        
        # creating course label
        label7 = Label(self.root, text="Enter course",fg="red",font=('calibre',10,'bold'))
        label7.place(x=170,y=350)

        # id input field
        reg_entry = Entry(self.root,textvariable = self.registration, font=('calibre',10,'normal'))
        reg_entry.place(x=310,y=150)
        
        # password input field
        pass_entry = Entry(self.root,textvariable = self.password, font=('calibre',10,'normal'))
        pass_entry.place(x=310,y=190)
        
        # name input field
        name_entry = Entry(self.root,textvariable = self.name, font=('calibre',10,'normal'))
        name_entry.place(x=310,y=230)
        
        # email input field
        email_entry = Entry(self.root,textvariable = self.email, font=('calibre',10,'normal'))
        email_entry.place(x=310,y=270)
        
        # contact input field
        contact_entry = Entry(self.root,textvariable = self.contact, font=('calibre',10,'normal'))
        contact_entry.place(x=310,y=310)
        
        # course input field
        course_entry = Entry(self.root,textvariable = self.course, font=('calibre',10,'normal'))
        course_entry.place(x=310,y=350)
        
        # creating button for student registration
        btn1 = Button(self.root, text = 'Register', bd = '6',fg="white",bg="brown",command=self.register)
        btn1.place(x=290,y=390)  
        
        self.label8 = Label(self.root,fg="blue",font=('calibre',10,'bold'))
        self.label8.place(x=290,y=450)
        
        
        # creating second label
        label9 = Label(self.root, text="Login",fg="red",font=('calibre',10,'bold'))
        label9.place(x=230,y=500)
        
        # creating button for student login
        btn2 = Button(self.root, text = 'Login', bd = '6',fg="white",bg="brown",command=self.login)
        btn2.place(x=290,y=490) 
         

        self.root.mainloop()
        
        
    # login finction definition
    def login(self):
        self.root.destroy()
        StudentLogin()
        
            
            
    def register(self):
        reg = int(self.registration.get())
        password = str(self.password.get())
        name = str(self.name.get())
        email = str(self.email.get())
        contact = str(self.contact.get())
        course = str(self.course.get())
         
        try:
            cur.execute("select * from student_details where registration_id = %s"%reg)
            result = cur.fetchall()
            if len(result)==1:  
                self.label8.config(text="user already exists")
            else:
                try:
                    query = "insert into student_details values(%s,%s,%s,%s,%s,%s)"
                    tuple = (reg,password,name,email,contact,course)
                    cur.execute(query,tuple)
                    con.commit()
                    self.label8.config(text="registered successfully")
                except :
                    self.label8.config(text="Failed to register")
        except:
            print("mysql exception occured")


# defining student login page
class StudentLogin:
    # constructor
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("400x500")
        self.root.title("Library Management System")
        
        self.registration=StringVar()
        self.password=StringVar()

        # creating heading label
        label1 = Label(self.root, text="Student Login",fg="Blue",font="italic",pady=50)
        label1.place(x=160,y=50)

        # creating first label
        label2 = Label(self.root, text="Enter registration id",fg="red",font=('calibre',10,'bold'))
        label2.place(x=70,y=180)
        
        # creating second label
        label3 = Label(self.root, text="Enter password",fg="red",font=('calibre',10,'bold'))
        label3.place(x=70,y=250)

        # id input field
        reg_entry = Entry(self.root,textvariable = self.registration, font=('calibre',10,'normal'))
        reg_entry.place(x=210,y=180)
        
        # password input field
        pass_entry = Entry(self.root,textvariable = self.password, font=('calibre',10,'normal'))
        pass_entry.place(x=210,y=250)
        
        # creating button for student login
        btn2 = Button(self.root, text = 'Login', bd = '6',fg="white",bg="brown",command=self.login)
        btn2.place(x=190,y=320)  
        
        self.label4 = Label(self.root,fg="blue",font=('calibre',10,'bold'))
        self.label4.place(x=190,y=370)
        
        # creating second label
        label5 = Label(self.root, text="Register yourself",fg="red",font=('calibre',10,'bold'))
        label5.place(x=70,y=430)
        
        # creating button for student login
        btn3 = Button(self.root, text = 'Register', bd = '6',fg="white",bg="brown",command=self.register)
        btn3.place(x=190,y=420)  

        self.root.mainloop()
        
        
    # login finction definition
    def login(self):
        reg = int(self.registration.get())
        password = str(self.password.get())
         
        try:
            cur.execute("select * from student_details where registration_id = %s"%reg)
            result = cur.fetchall()
            if len(result)==1:
                if password==result[0][1]:
                    self.registration_number = reg
                    self.root.destroy()
                    StudentInterface(self.registration_number)
                else:
                    self.label4.config(text="wrong password")
            else:
                self.label4.config(text="student is not registered")
        except:
            print("mysql exception occured")
            
            
    def register(self):
        self.root.destroy()
        StudentRegister()
        

# defining admin interface
class AdminInterface:
    # constructor
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title("Library Management System")
        
        self.bookId=StringVar()
        self.bookName=StringVar()
        self.author = StringVar()
        self.avlBook = StringVar()

        # creating heading label
        label1 = Label(self.root, text="Add Book",fg="Blue",font="italic",pady=30)
        label1.place(x=260,y=50)

        # creating book id label
        label2 = Label(self.root, text="Enter Book Id",fg="red",font=('calibre',10,'bold'))
        label2.place(x=170,y=150)
        
        # creating book name label
        label3 = Label(self.root, text="Enter Book Name",fg="red",font=('calibre',10,'bold'))
        label3.place(x=170,y=190)
        
        # creating author label
        label4 = Label(self.root, text="Enter Author",fg="red",font=('calibre',10,'bold'))
        label4.place(x=170,y=230)
        
        # creating available book label
        label5 = Label(self.root, text="Enter available book",fg="red",font=('calibre',10,'bold'))
        label5.place(x=170,y=270)
        

        # book id input field
        bookId_entry = Entry(self.root,textvariable = self.bookId, font=('calibre',10,'normal'))
        bookId_entry.place(x=310,y=150)
        
        # bookName input field
        bookName_entry = Entry(self.root,textvariable = self.bookName, font=('calibre',10,'normal'))
        bookName_entry.place(x=310,y=190)
        
        # author input field
        author_entry = Entry(self.root,textvariable = self.author, font=('calibre',10,'normal'))
        author_entry.place(x=310,y=230)
        
        # avlBook input field
        avlBook_entry = Entry(self.root,textvariable = self.avlBook, font=('calibre',10,'normal'))
        avlBook_entry.place(x=310,y=270)
        
        
        # creating button for adding book
        btn1 = Button(self.root, text = 'Add', bd = '6',fg="white",bg="brown",command=self.add)
        btn1.place(x=290,y=390)  
        
        self.label6 = Label(self.root,fg="blue",font=('calibre',10,'bold'))
        self.label6.place(x=230,y=450)
        

        self.root.mainloop()
        

            
    def add(self):
        bookId = int(self.bookId.get())
        bookName = str(self.bookName.get())
        author = str(self.author.get())
        avlBook = int(self.avlBook.get())
         
        
        try:
            query = "insert into book_list values(%s,%s,%s,%s)"
            tuple = (bookId,bookName,author,avlBook)
            cur.execute(query,tuple)
            con.commit()
            self.label6.config(text="book added successfully")
        except :
            self.label6.config(text="Failed to add")
        

# Admin login page
class AdminLogin:
    
    # constructor
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.title("Library Management System")
        
        self.registration=StringVar()
        self.password=StringVar()

        # creating heading label
        label1 = Label(self.root, text="Admin Login",fg="Blue",font="italic",pady=50)
        label1.place(x=160,y=50)

        # creating first label
        label2 = Label(self.root, text="Enter employee id",fg="red",font=('calibre',10,'bold'))
        label2.place(x=70,y=180)
        
        # creating second label
        label3 = Label(self.root, text="Enter password",fg="red",font=('calibre',10,'bold'))
        label3.place(x=70,y=250)

        # id input field
        reg_entry = Entry(self.root,textvariable = self.registration, font=('calibre',10,'normal'))
        reg_entry.place(x=210,y=180)
        
        # password input field
        pass_entry = Entry(self.root,textvariable = self.password, font=('calibre',10,'normal'))
        pass_entry.place(x=210,y=250)
        
        # creating button for admin login
        btn2 = Button(self.root, text = 'Login', bd = '6',fg="white",bg="brown",command=self.login)
        btn2.place(x=190,y=320)  
        
        self.label4 = Label(self.root,fg="blue",font=('calibre',10,'bold'))
        self.label4.place(x=190,y=370)

        self.root.mainloop()
        
        
    # login finction definition
    def login(self):
        reg = int(self.registration.get())
        password = str(self.password.get())
         
        try:
            cur.execute("select * from admin_details where emp_id = %s"%reg)
            result = cur.fetchall()
            if len(result)==1:
                if password==result[0][2]:
                    self.root.destroy()
                    AdminInterface()
                else:
                    self.label4.config(text="wrong password")
            else:
                self.label4.config(text="Invalid employee id")
        except:
            print("mysql exception occured")
        

# home page
class Main:
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.title("Library Management System")

        # creating heading label
        label1 = Label(self.root, text="Login Page",fg="Blue",font="italic",pady=50)
        label1.place(x=180,y=50)

        # creating first label
        label2 = Label(self.root, text="Student Login",fg="red",font="italic")
        label2.place(x=90,y=180)
        
        # creating second label
        label3 = Label(self.root, text="Admin Login",fg="red",font="italic")
        label3.place(x=90,y=250)

        # creating button for student login
        btn1 = Button(self.root, text = 'Login', bd = '6',fg="white",bg="brown",command=self.studentLogin)
        btn1.place(x=230,y=180)

        # creating button for admin login
        btn2 = Button(self.root, text = 'Login', bd = '6',fg="white",bg="brown",command=self.adminLogin)
        btn2.place(x=230,y=250)  

        self.root.mainloop()
        
        
    def studentLogin(self):
        self.root.destroy()
        StudentLogin()
        
        
    def adminLogin(self):
        self.root.destroy()
        AdminLogin()
        

Main()
con.close()