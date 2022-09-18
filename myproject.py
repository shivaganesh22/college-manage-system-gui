
from asyncio.windows_events import NULL
from audioop import add
from ctypes.wintypes import SIZE
from re import search
from tkinter import *
import csv
from tkinter import messagebox
from turtle import color, width
from unicodedata import name
from tkinter import ttk
def viewapp():
    view=Tk()
    view.title("View Applications")
    tv=ttk.Treeview(view,columns=(1,2,3,4,5,6,7,8,9),show="headings")
    tv.pack()
    tv.column(1, width=100)
    tv.column(2, width=100)
    tv.column(3, width=100)
    tv.column(4, width=50)
    tv.column(5, width=60)
    tv.column(6, width=60)
    tv.column(7, width=50)
    tv.column(8, width=50)
    tv.column(9, width=200)


    tv.heading(1,text="FULL NAME")
    tv.heading(2,text="HALL TICKET")
    tv.heading(3,text="RANK")
    tv.heading(4,text="CODE")
    tv.heading(5,text="BRANCH")
    tv.heading(6,text="GENDER")
    tv.heading(7,text="CASTE")
    tv.heading(8,text="MOBILE")
    tv.heading(9,text="EMAIL")
  
    
    with open("applications.csv","r") as f:
        r=csv.reader(f)
        for row in r :
            if len(row)!=0:
                tv.insert('','end',values=row) 

                

    mainloop()
def apply():
    apply=Tk()
    def applyclg():
        data=[]
        data.append(fn.get().title())
        data.append(ht.get())
        data.append(int(rk.get()))
        data.append(code.get().upper())
        data.append(bran.get())
        data.append(gen.get())
        data.append(cas.get())
        data.append(int(no.get()))
        data.append(email.get().lower())
        with open("colleges.csv","r") as f:
            found=0
            branch=[]
            r=csv.reader(f)
            for row in r:
                for column in row:
                    if row[0]==data[3]:
                        found=1
                        branch.append(column)
            f.close()      
        list=["AI","IT","CSE","CS","ECE","CIV","MEC"]
        if data[4]=="AI":
            i=3
        elif data[4]=="IT":
            i=4
        elif data[4]=="CSE":
            i=5
        elif data[4]=="CS":
            i=6
        elif data[4]=="ECE":
            i=7
        elif data[4]=="CIV":
            i=8
        elif data[4]=="MEC":
            i=9 
        if data[0]=='' or data[1]=='' or data[2]=='' or data[3]=='' or data[4]=='' or data[5]==''  or data[6]=='' or data[7]=='' or data[8]=='':
            Label(apply,text="Enter all details",fg="red").place(x=50,y=340)
        elif found==0:
            Label(apply,text="College not found",fg="red").place(x=50,y=340)
        elif data[2]>(int(branch[i])) :
            Label(apply,text="You are not Eligible",fg="red").place(x=50,y=340)
        elif found==1 :
            with open("applications.csv","a") as f:
                w=csv.writer(f)
                w.writerows([data])
            apply.destroy()
            messagebox.showinfo("Success","Applied Successfully")
    
            
        
            

                        
       

     
    gender=["Male","Female"]
    caste=["BC","ST","OC","SC"]
    apply.geometry("300x400")
    apply.title("Apply College")
    Label(apply,text="Full Name").place(x=50,y=30)
    
    Label(apply,text="Hall Ticket").place(x=50,y=60)
    Label(apply,text="Rank").place(x=50,y=90)
    Label(apply,text="College Code").place(x=50,y=120)
    Label(apply,text="Branch").place(x=50,y=150)
    Branch=["AI","IT","CSE","CS","ECE","CIV","MEC"]
    bran=StringVar(apply)
    bran.set(Branch[0])
    OptionMenu(apply,bran,*Branch).place(x=140,y=150)
    Label(apply,text="Gender").place(x=50,y=180)
    gen=StringVar(apply)
    gen.set(gender[0])
    OptionMenu(apply,gen,*gender).place(x=140,y=180)
    Label(apply,text="Caste").place(x=50,y=210)
    cas=StringVar(apply)
    cas.set(caste[0])
    OptionMenu(apply,cas,*caste).place(x=140,y=210)
    Label(apply,text="Contact No").place(x=50,y=240)
    Label(apply,text="Email").place(x=50,y=270)
    fn=Entry(apply)
    fn.place(x=140,y=30)
    ht=Entry(apply)
    rk=Entry(apply)
    no=Entry(apply)
    email=Entry(apply)
    code=Entry(apply)
    ht.place(x=140,y=60)
    rk.place(x=140,y=90)
    code.place(x=140,y=120)
    no.place(x=140,y=240)
    email.place(x=140,y=270)
    Button(apply,text="Apply",fg="blue",bg="#ccff66",command=applyclg,width=10).place(x=170,y=300)
    Button(apply,text="Cancel",fg="blue",bg="#ccff66",command=apply.destroy,width=10).place(x=50,y=300)
    
    mainloop
def viewreg():
    viewreg=Tk()
    viewreg.title("Registered Students")
    tv=ttk.Treeview(viewreg,columns=(1,2,3),show="headings")
    tv.pack()
    tv.heading(1,text="Name")
    tv.heading(2,text="Hall Ticket")
    tv.heading(3,text="Username")
    with open("users.csv","r") as f:
        r=csv.reader(f)
        for row in r :
            if len(row)!=0:
                tv.insert('','end',values=row) 
    mainloop
def searchclg():
    searchclg=Tk()
    def search():
        data=[]
        c=code.get().upper()
        with open("colleges.csv","r") as f:
            w=csv.reader(f)
            found=0
            for row in w:
                for column in row:
                    if row[0]==c:
                        data.append(column)
                        print(data)
                        found=1
            if found==1:
                Label(searchclg,text=data[1]).place(x=120,y=50)
                Label(searchclg,text=data[2]).place(x=120,y=75)
                Label(searchclg,text=data[3]).place(x=120,y=100)
                Label(searchclg,text=data[4]).place(x=120,y=125)
                Label(searchclg,text=data[5]).place(x=120,y=150)
                Label(searchclg,text=data[6]).place(x=120,y=175)
                Label(searchclg,text=data[7]).place(x=120,y=200)
                Label(searchclg,text=data[8]).place(x=120,y=225)
                Label(searchclg,text=data[9]).place(x=120,y=250)
                Label(searchclg,text=data[10]).place(x=120,y=275)
            else :
                Label(searchclg,text="College not found",fg="red").place(x=50,y=350)
                        

        
       

    searchclg.title("Search College")
    searchclg.geometry("300x400")
    Label(searchclg,text="CODE").place(x=50,y=25)
    code=Entry(searchclg)
    code.place(x=120,y=25)
    Label(searchclg,text="NAME").place(x=50,y=50)
    Label(searchclg,text="ADDRESS").place(x=50,y=75)
    Label(searchclg,text="AI").place(x=50,y=100)
    Label(searchclg,text="IT").place(x=50,y=125)
    Label(searchclg,text="CSE").place(x=50,y=150)
    Label(searchclg,text="CS").place(x=50,y=175)
    Label(searchclg,text="ECE").place(x=50,y=200)
    Label(searchclg,text="CIV").place(x=50,y=225) 
    Label(searchclg,text="MEC").place(x=50,y=250)
    Label(searchclg,text="FEE").place(x=50,y=275)
    Button(searchclg,text="Search",width=10,command=search,fg="blue",bg="#ccff66").place(x=165,y=320)
    Button(searchclg,text="Cancel",width=10,command=searchclg.destroy,fg="blue",bg="#ccff66").place(x=50,y=320)
    mainloop()
def addclg():
    addclg=Tk()
    def add():
        data=[]
        data.append(code.get().upper())
        data.append(name.get().title())
        data.append(address.get().title())
        data.append(int(ai.get()))
        data.append(int(it.get()))
        data.append(int(cse.get()))
        data.append(int(cs.get()))
        data.append(int(ece.get()))
        data.append(int(civ.get()))
        data.append(int(mec.get()))
        data.append(int(fee.get()))
        if data[0]=='' or data[1]=='' or data[2]=='' or data[3]=='' or data[4]=='' or data[5]==''  or data[6]=='' or data[7]=='' or data[8]=='' or data[9]=='' or data[10]=='':
            Label(addclg,text="Enter all details",fg="red").place(x=50,y=350)
        else :
            with open("colleges.csv","a") as f:
                r=csv.writer(f)
                r.writerows([data])
            addclg.destroy()
            messagebox.showinfo("Success","College Added")

    addclg.title("Add College")
    addclg.geometry("300x400")
    Label(addclg,text="CODE").place(x=50,y=25)
    code=Entry(addclg)
    code.place(x=120,y=25)
    Label(addclg,text="NAME").place(x=50,y=50)
    name=Entry(addclg)
    name.place(x=120,y=50)
    Label(addclg,text="ADDRESS").place(x=50,y=75)
    address=Entry(addclg)
    address.place(x=120,y=75)
    Label(addclg,text="AI").place(x=50,y=100)
    ai=Entry(addclg)
    ai.place(x=120,y=100)
    Label(addclg,text="IT").place(x=50,y=125)
    it=Entry(addclg)
    it.place(x=120,y=125)
    Label(addclg,text="CSE").place(x=50,y=150)
    cse=Entry(addclg)
    cse.place(x=120,y=150)
    Label(addclg,text="CS").place(x=50,y=175)
    cs=Entry(addclg)
    cs.place(x=120,y=175)
    Label(addclg,text="ECE").place(x=50,y=200)
    ece=Entry(addclg)
    ece.place(x=120,y=200)
    Label(addclg,text="CIV").place(x=50,y=225)
    civ=Entry(addclg)
    civ.place(x=120,y=225)
    Label(addclg,text="MEC").place(x=50,y=250)
    mec=Entry(addclg)
    mec.place(x=120,y=250)
    Label(addclg,text="FEE").place(x=50,y=275)
    fee=Entry(addclg)
    fee.place(x=120,y=275)
    Button(addclg,text="Add",width=10,command=add,fg="blue",bg="#ccff66").place(x=165,y=320)
    Button(addclg,text="Cancel",width=10,command=addclg.destroy,fg="blue",bg="#ccff66").place(x=50,y=320)
    mainloop()

def editclg():
    editclg=Tk()
    def edit():
        data=[]
        data.append(code.get().upper())
        data.append(name.get().title())
        data.append(address.get().title())
        data.append(int(ai.get()))
        data.append(int(it.get()))
        data.append(int(cse.get()))
        data.append(int(cs.get()))
        data.append(int(ece.get()))
        data.append(int(civ.get()))
        data.append(int(mec.get()))
        data.append(int(fee.get()))
        if data[0]=='' or data[1]=='' or data[2]=='' or data[3]=='' or data[4]=='' or data[5]==''  or data[6]=='' or data[7]=='' or data[8]=='' or data[9]=='' or data[10]=='':
            Label(editclg,text="Enter all details",fg="red").place(x=50,y=350)

        else :
            with open("colleges.csv","r") as f:
                r=csv.reader(f)
                found=0
                details=[]
                for row in r:
                    if len(row)!=0:
                        if row[0]==data[0]:
                           details.append(data)
                           found=1
                        else:
                            details.append(row) 
            f.close()
        if found==1:
            with open ("colleges.csv","w") as f:
                w=csv.writer(f)
                w.writerows(details)
            f.close()
            editclg.destroy()
            messagebox.showinfo("Success","Data Updated")
        else:
            Label(editclg,text="College not found check college code",fg="red").place(x=50,y=350)

    


        
    editclg.title("Edit College")
    editclg.geometry("300x400")
    Label(editclg,text="CODE").place(x=50,y=25)
    code=Entry(editclg)
    code.place(x=120,y=25)
    Label(editclg,text="NAME").place(x=50,y=50)
    name=Entry(editclg)
    name.place(x=120,y=50)
    Label(editclg,text="ADDRESS").place(x=50,y=75)
    address=Entry(editclg)
    address.place(x=120,y=75)
    Label(editclg,text="AI").place(x=50,y=100)
    ai=Entry(editclg)
    ai.place(x=120,y=100)
    Label(editclg,text="IT").place(x=50,y=125)
    it=Entry(editclg)
    it.place(x=120,y=125)
    Label(editclg,text="CSE").place(x=50,y=150)
    cse=Entry(editclg)
    cse.place(x=120,y=150)
    Label(editclg,text="CS").place(x=50,y=175)
    cs=Entry(editclg)
    cs.place(x=120,y=175)
    Label(editclg,text="ECE").place(x=50,y=200)
    ece=Entry(editclg)
    ece.place(x=120,y=200)
    Label(editclg,text="CIV").place(x=50,y=225)
    civ=Entry(editclg)
    civ.place(x=120,y=225)
    Label(editclg,text="MEC").place(x=50,y=250)
    mec=Entry(editclg)
    mec.place(x=120,y=250)
    Label(editclg,text="FEE").place(x=50,y=275)
    fee=Entry(editclg)
    fee.place(x=120,y=275)
    Button(editclg,text="Edit",width=10,command=edit,fg="blue",bg="#ccff66").place(x=165,y=320)
    Button(editclg,text="Cancel",width=10,command=editclg.destroy,fg="blue",bg="#ccff66").place(x=50,y=320)
    mainloop()
def viewclg():
    viewclg=Tk()
    viewclg.title("View Colleges")
    
    tv=ttk.Treeview(viewclg,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings")
    tv.pack()
    tv.column(1, width=50)
    tv.column(4, width=50)
    tv.column(5, width=50)
    tv.column(6, width=50)
    tv.column(7, width=50)
    tv.column(8, width=50)
    tv.column(9, width=50)
    tv.column(10, width=50)
    tv.column(11, width=50)

    tv.heading(1,text="CODE")
    tv.heading(2,text="NAME")
    tv.heading(3,text="ADDRESS")
    tv.heading(4,text="AI")
    tv.heading(5,text="IT")
    tv.heading(6,text="CSE")
    tv.heading(7,text="CS")
    tv.heading(8,text="ECE")
    tv.heading(9,text="CIV")
    tv.heading(10,text="MEC")
    tv.heading(11,text="FEE")
    
    with open("colleges.csv","r") as f:
        r=csv.reader(f)
        for row in r :
            if len(row)!=0:
                tv.insert('','end',values=row) 

                

    mainloop()
def main():
    
    main=Tk()
    def alogin():
        main.destroy()
        alogin=Tk()
        alogin.title("Admin Login")
        alogin.geometry("300x150")
        def admin():
            qq=au.get().lower()
            qp=ap.get()
            
            if qq=="admin" and qp=="1234":
                alogin.destroy()
                admin=Tk()
                admin.title("Admin Menu")
                admin.geometry("300x400")
                Button(admin,text="Add College",command=addclg,fg="blue",bg="skyblue",width=20).place(x=80,y=80)
                Button(admin,text="Edit College",command=editclg,fg="blue",bg="yellow",width=20).place(x=80,y=110)
                Button(admin,text="View Colleges",command=viewclg,fg="blue",bg="#7FFFD4",width=20).place(x=80,y=140)
                Button(admin,text="View Applications",command=viewapp,fg="blue",bg="orange",width=20).place(x=80,y=170)
                Button(admin,text="View Registered Students",command=viewreg,fg="blue",bg="#50C878",width=20).place(x=80,y=200)
                Button(admin,text="Exit",command=exit,fg="red",width=20).place(x=80,y=230)
                
                
                mainloop()
            else:
                Label(alogin,text="Invalid Login Credentials",fg="red").place(x=50,y=110)

        Label(alogin,text="Username").place(x=50,y=25)
        Label(alogin,text="Password").place(x=50,y=50)
        au=Entry(alogin)
        ap=Entry(alogin)
        au.place(x=120,y=25)
        ap.place(x=120,y=50)
    
        Button(alogin,text="Login",fg="blue",bg="#ccff66",command=admin,width=10).place(x=170,y=80)
        Button(alogin,text="Cancel",fg="blue",bg="#ccff66",command=exit,width=10).place(x=50,y=80)
        mainloop()
    
    def student():
        main.destroy()
        
        student=Tk()
        
        def login():
           student.destroy()
           login=Tk()
           login.title("Student login")
           login.geometry("300x150")
           def forgot():
            forgot=Tk()
            def getpass():

                use=e1.get().lower()
                
                print(use)
                with open("users.csv","r") as f:
    
                    found=0
                    r=csv.reader(f)
                    for row in r:
                        if len(row)!=0:
                            if use==row[2]:
                                Label(forgot,text=row[3]).place(x=120,y=50)
                                found=1
                                break
                if found==0:
                    Label(forgot,text="User not found!...",fg="red").place(x=50,y=110)
            forgot.title("Forgot Password")
            forgot.geometry("300x150")
            Label(forgot,text="Username").place(x=50,y=25)
            Label(forgot,text="Password").place(x=50,y=50)
            e1=Entry(forgot)
            e1.place(x=120,y=25)
            Button(forgot,text="Get Password",fg="blue",bg="#ccff66",command=getpass,width=10).place(x=170,y=80)
            
            mainloop

    
           def menu():
            det=[]
            det.append(e1.get().lower())
            det.append(e2.get())
           
            
            with open("users.csv","r") as f:
                found=0
                r=csv.reader(f) 
                for row in r:
                    if len(row)!=0:
                        if row[2]==det[0] and row[3]==det[1]:
                            login.destroy()
                            menu=Tk()
                            
                            menu.title("Student menu")
                            menu.geometry("300x400")
                            Button(menu,text="View Colleges",command=viewclg,fg="blue",bg="skyblue",width=20).place(x=80,y=100)
                            Button(menu,text="Search College",command=searchclg,fg="blue",bg="orange",width=20).place(x=80,y=160)
                            Button(menu,text="Apply College",command=apply,fg="blue",bg="yellow",width=20).place(x=80,y=130)
                            Button(menu,text="Exit",fg="red",command=exit,width=20).place(x=80,y=190) 
                            found=1
                            mainloop()
                if(found==0):
                    Label(login,text="Invalid Login Credentials!...",fg="red").place(x=50,y=110)



           Label(login,text="Username").place(x=50,y=25)
           Label(login,text="Password").place(x=50,y=50)
           e1=Entry(login)
           e2=Entry(login)
           e1.place(x=120,y=25)
           e2.place(x=120,y=50)
           Button(login,text="Login",fg="blue",bg="#ccff66",command=menu,width=10).place(x=170,y=80)
           Button(login,text="Forgot Password",fg="blue",bg="#ccff66",command=forgot,width=15).place(x=50,y=80)
           mainloop()
   
        def signup():

           
           signup=Tk()
           signup.title("Signup")
           signup.geometry("300x200")
           

           def register():
            acc=[]
            
            acc.append(na.get().title())
            acc.append(ht.get())
            acc.append(un.get().lower())
            acc.append(pw.get())
            
            if acc[0]==''or acc[1]=='' or acc[2]==''or acc[3]=='' :
                Label(signup,text="Enter all Details!...",fg="red").place(x=50,y=150)
            else:
                
                
                with open("users.csv","a") as f:
                    w=csv.writer(f)
                    w.writerows([acc])
                
                
                signup.destroy()
                messagebox.showinfo("Success","Registered Successful")             
                f.close()
           Label(signup,text="Full Name").place(x=50,y=25)
           Label(signup,text="Hall Ticket").place(x=50,y=50)
           Label(signup,text="Username").place(x=50,y=75)
           Label(signup,text="Password").place(x=50,y=100)
           na=Entry(signup)
           ht=Entry(signup)
           un=Entry(signup)
           pw=Entry(signup)
           na.place(x=120,y=25)
           ht.place(x=120,y=50)
           un.place(x=120,y=75)
           pw.place(x=120,y=100)
           Button(signup,text="Signup",fg="blue",bg="#ccff66",command=register,width=10).place(x=160,y=125)
           Button(signup,text="Login",fg="blue",bg="#ccff66",command=signup.destroy,width=10).place(x=50,y=125)
           mainloop()

        
        student.title("Student login and signup")
        student.geometry("300x400")
        
        Button(student,text="Login",fg="blue",command=login,width=20,bg="#ffcc66").place(x=80,y=120)
        Button(student,text="Signup",fg="blue",command=signup,width=20,bg="#50C878").place(x=80,y=150)
        Button(student,text="Exit",fg="red",command=exit,width=20).place(x=80,y=180)
        mainloop()

    main.title("College Management System")
    main.geometry("300x400")
    Label(main,text="COLLEGE MANAGEMENT SYSTEM",fg="red",bg="yellow").place(x=60,y=60)
    Button(main,text="Admin",command=alogin,fg="red",bg="#ffcc66",width=20).place(x=80,y=120)
    Button(main,text="Student",command=student,fg="blue",bg="#89c35c",width=20).place(x=80,y=150)
    Label(main,text="PROJECT  BY :",fg="red",bg="yellow").place(x=210,y=300)

    Label(main,text="SHIVAGANESH  :21EG112B26",bg="#ffcccc").place(x=130,y=325)

    
    
    mainloop()




main()