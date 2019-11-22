from Tkinter import *
##import tkinter

##informations required
def Register_infro():
    name_info = name.get()
    gender_info = gender.get()
    dob_info = dob.get()
    address_info = address.get()
    number_info = number.get()
    email_infro = email.get()

    file = open("Database.txt", "a")
    file.write("Name:" + name_info + "\n")
    file.write("Gender:" + gender_info + "\n")
    file.write("DOB:" + dob_info + "\n")
    file.write("Address:" + address_info + "\n")
    file.write("Phone number:" + number_info + "\n" + "\n" + "\n")
    file.write("Email:" + email_infro + "\n")
    file.close()

    name_entry.delete(0, END)
    gender_entry.delete(0, END)
    dob_entry.delete(0, END)
    address_entry.delete(0, END)
    number_entry.delete(0, END)
    email_entry.delete(0,END)
    

    Label(screen1, text="Registered", font=("calibri", 15),bg="aquamarine").grid(row=11,column=2)

## user input friend's information
def Insert():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("NGE CHARO")
    screen1.geometry("600x550")
    screen1.config(bg="cadetblue")
    global name, gender, dob, address, number,email
    global name_entry, gender_entry, dob_entry, address_entry, number_entry,email_entry
    name = StringVar()
    gender = StringVar()
    dob = StringVar()
    address = StringVar()
    number = StringVar()
    email = StringVar()

    Label(screen1, text="Enter your details",font=("calibri",16,"bold"),bg="cadetblue").grid(row=1,column=2)
    Label(screen1, text=" ",bg="cadetblue").grid(row=1,column=3)

    Label(screen1, text="Name:",font=("calibri",14,"bold"),bg="cadetblue").grid(row=3,column=1)
    name_entry = Entry(screen1, textvariable=name)
    name_entry.grid(row=3,column=2)

    Label(screen1, text="Gender:",font=("calibri",16,"bold"),bg="cadetblue").grid(row=4,column=1)
    gender_entry = Entry(screen1, textvariable=gender)
    gender_entry.grid(row=4,column=2)


    Label(screen1, text="DoB:",font=("calibri",16,"bold"),bg="cadetblue").grid(row=5,column=1)
    dob_entry = Entry(screen1, textvariable=dob)
    dob_entry.grid(row=5,column=2)

    Label(screen1, text="Address:",font=("calibri",16,"bold"),bg="cadetblue").grid(row=6,column=1)
    address_entry = Entry(screen1, textvariable=address)
    address_entry.grid(row=6,column=2)

    Label(screen1, text="Phone Number:",font=("calibri",16,"bold"),bg="cadetblue").grid(row=7,column=1)
    number_entry = Entry(screen1, textvariable=number)
    number_entry.grid(row=7,column=2)

    Label(screen1, text="Email:",font=("calibri",16,"bold"),bg="cadetblue").grid(row=8,column=1)
    email_entry = Entry(screen1, textvariable=email)
    email_entry.grid(row=8,column=2)

    Label(screen1, text=" ",bg="cadetblue").grid(row=9,column=1)
    Button(screen1, text="Enter", width=10, height=1, command=Register_infro,bg="cadetblue").grid(row=9,column=2)
##graph display for the male and female from the list of friends    
def graph():
    import matplotlib.pyplot as p
    global screen3
    screen3 = Toplevel()
    screen3.title("NGE CHARO")
    screen3.geometry("600x550")
    screen3.config(bg="cadetblue")
    Label(screen3, text="Graph: ",width="300",height="2",font=("calibri",20,"bold"),bg="gold2").pack()
    with open("Database.txt", 'r') as f:
        f.seek(0)
        x = f.read()
        count_male = x.count("male")
        count_female = x.count("female")
    gender = ["Male","Female"]
    values = [count_male,count_female]
    p.title("Number of male and female pie graph")
    p.pie(values, labels=gender,autopct='%1.1f%%',shadow=True)
    Label(screen3, text="Number of Male: ", font=("calibri", 12, "bold"),bg="cadetblue").pack()
    Label(screen3, text=count_male,bg="cadetblue").pack()
    Label(screen3, text="Number of Female: ", font=("calibri", 12, "bold"),bg="cadetblue").pack()
    Label(screen3, text=count_female,bg="cadetblue").pack()
    Label(screen3, text=p.show()).pack()
##total no of friends in the list
def total():
    global screen4
    screen4 = Toplevel()
    screen4.title("NGE CHARO")
    screen4.geometry("600x550")
    screen4.config(bg="cadetblue")
    Label(screen4, text="Details Of your Friends",width="300",height="2",font=("calibri",20,"bold"),bg="gold2").pack()
    Label(screen4, text=" ",bg="cadetblue").pack()

    Label(screen4, text="Total Number of Friends: ", font=("calibri", 12, "bold"),bg="cadetblue").pack()
    with open("Database.txt",'r') as f:
        contents = f.read()
        count = contents.count("Name")
    Label(screen4, text=count,bg="cadetblue").pack()
    Label(screen4, text=" ",bg="cadetblue").pack()

def Display():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("NGE CHARO")
    screen2.geometry("600x550")
    screen2.config(bg="cadetblue")
    Label(screen2, text="DISPLAY",width="300",height="2",font=("calibri",40,"bold"),bg="gold2").pack()
    Label(screen2, text=" ",bg="cadetblue").pack()
    
    Label(screen2, text="Select anyone to view Details",font=("calibri",16,"bold"),bg="cadetblue").pack()
    Label(screen2, text=" ",bg="cadetblue").pack()
    Button(screen2, text="Total Friends", bg="deepskyblue", height="2", width="10",font=("calibri",16,"bold"), command= total).pack()
    Label(screen2, text=" ",bg="cadetblue").pack()
    Button(screen2, text="Graph Details", bg="deepskyblue2", height="2", width="10", font=("calibri",16,"bold"), command=graph).pack()
##to know whether the name given by the user is in the list or not    
def Search():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("NGE CHARO")
    screen5.geometry("600x550")
    global search_var,search_entry
    search_var = StringVar()
    screen5.config(bg="cadetblue")
    Label(screen5, text="Enter your friend Name to search from the list",width="300",height="2",font=("calibri",15,"bold"),bg="gold2").pack()
    Label(screen5, text="Search",font=("calibri",14,"bold"),bg="cadetblue").pack()
    search_entry = Entry(screen5, textvariable=search_var)
    search_entry.pack()

    Label(screen5, text=" ",bg="cadetblue").pack()
    Button(screen5, text="search", width=10, height=1, command=search,bg="deepskyblue3").pack()
  
def search():
    search_infro = search_var.get()
    f = open('Database.txt', 'r')
    fr = f.read()

    if search_infro in fr:
        x="This person is in your friend list."
        Label(screen5,text=x,bg="cadetblue").pack()
        
    else:
        y="This person is not in your friend list"
        Label(screen5,text=y,bg="cadetblue").pack()
        
##to delete the information of the person from the list. 
def Delete():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("NGE CHARO")
    screen6.geometry("600x550")
    global name_var,name_entry
    name_var = StringVar()
    screen6.config(bg="cadetblue")
    Label(screen6, text="Enter your friend Name to delete from the list",width="300",height="2",font=("calibri",15,"bold"),bg="gold2").pack()
    Label(screen6, text="Delete",font=("calibri",14,"bold"),bg="cadetblue").pack()
    name_entry = Entry(screen6, textvariable= name_var)
    name_entry.pack()

    Label(screen6, text=" ",bg="cadetblue").pack()
    Button(screen6, text="Delete", width=10, height=1, command=delete,bg="deepskyblue3").pack()

def delete():
    import os
    search_infro = name_var.get()
    f = open('Database.txt', 'r')
    fr = f.read()

    if search_infro in fr:
        os.remove('name_var')
        x="Yes,the name you have enter is in the list and it was deleted"
        Label(screen6,text=x,bg="cadetblue").pack()
        
    else:
        y="No match"
        Label(screen6,text=y,bg="cadetblue").pack()
        

##displays the main home page.
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x550")
    screen.title("Nge charo")
    screen.config(bg="cadetblue")
    Label(text="NGE CHARO",width="300",height="2",font=("calibri",40,"bold"),bg="gold2").pack()
    Label(text=" ",bg="cadetblue").pack()
    Button(text="Insert", bg="deepskyblue", height="2", width="20",font=("calibri",16,"bold"), command=Insert).pack()
    Label(text=" ",bg="cadetblue").pack()
    Button(text="Display", bg="deepskyblue2", height="2", width="20", font=("calibri",16,"bold"), command=Display).pack()
    Label(text=" ",bg="cadetblue").pack()
    Button(text="Search", bg="deepskyblue3", height="2", width="20", font=("calibri",16,"bold"), command=Search).pack()
    Label(text=" ",bg="cadetblue").pack()
    Button(text="Delete", bg="deepskyblue4", height="2", width="20", font=("calibri",16,"bold"), command=Delete).pack()

   
    
    
    screen.mainloop()


main_screen()