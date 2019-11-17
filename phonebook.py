from Tkinter import *
import tkMessageBox
import sqlite3

con=sqlite3.Connection('PhonebookDB')
cur=con.cursor()
cur.execute('PRAGMA foreign_keys=on')
cur.execute('create table if not exists contact(id integer primary key autoincrement,FName Varchar(20),MName Varchar(20),LName Varchar(20),Company Varchar(20),Address Varchar(20),City Varchar(20),PIN char(6),Web Varchar(20),DOB date)')
cur.execute('create table if not exists phone(id integer,type varchar(8),phone number(10), primary key(id,phone), constraint fk_phone foreign key(id) references contact(id) on delete cascade)')
cur.execute('create table if not exists email(id integer,email_type varchar(8),email varchar(30), primary key(id,email), constraint fk_email foreign key(id) references contact(id) on delete cascade)')
types={0:'Home',1:'Office',2:'Personal'}

root=Tk()
icon=PhotoImage(file="phonebook-icon.gif")
Label(root, image=icon).grid(row=0,column=2)
Label(root, text="First Name").grid(row=1,column=1)
e1=Entry(root,width=37)
e1.grid(row=1,column=2)
Label(root, text="Middle Name").grid(row=2,column=1)
e2=Entry(root,width=37)
e2.grid(row=2,column=2)
Label(root, text="Last Name").grid(row=3,column=1)
e3=Entry(root,width=37)
e3.grid(row=3,column=2)
Label(root, text="Company Name").grid(row=4,column=1)
e4=Entry(root,width=37)
e4.grid(row=4,column=2)
Label(root, text="Address").grid(row=5,column=1)
e5=Entry(root,width=37)
e5.grid(row=5,column=2)
Label(root, text="City").grid(row=6,column=1)
e6=Entry(root,width=37)
e6.grid(row=6,column=2)
Label(root, text="PinCode").grid(row=7,column=1)
e7=Entry(root,width=37)
e7.grid(row=7,column=2)
Label(root, text="Website URL").grid(row=8,column=1)
e8=Entry(root,width=37)
e8.grid(row=8,column=2)
Label(root, text="Date of Birth").grid(row=9,column=1)
e9=Entry(root,width=37)
e9.grid(row=9,column=2)
Label(root, text= "Phone Number", fg='blue',font=(None, 11)).grid(row=10,column=1)
Label(root, text="Phone Number(Home):").grid(row=11,column=1)
e10=Entry(root,width=37)
e10.grid(row=11,column=2)
c=0
phones=[]
phones.append(e10)
def addPhone():
    global c
    global phones
    if c>1:
        tkMessageBox.showerror('Too many Phones', 'Sorry! You cannot Add more than 3 phone numbers')
        return 
    Label(root, text="Phone Number({0}) :".format(types[d+1])).grid(row=12+c,column=1)
    e=Entry(root,width=37)
    e.grid(row=12+c,column=2)
    c+=1
    phones.append(e)
    Button(root,text='+',command=addPhone).grid(row=11+c,column=3)
    print "Phone Field Added"
Button(root,text='+',command=addPhone).grid(row=11,column=3)
Label(root, text= "Email ", fg='blue',font=(None, 11)).grid(row=15,column=1)
Label(root, text="Email(Home) :").grid(row=16,column=1)
e11=Entry(root,width=37)
e11.grid(row=16,column=2)
d=0
emails=[]
emails.append(e11)
def addEmail():
    global d
    global emails
    if d>1:
        tkMessageBox.showerror('Too many Emails', 'Sorry! You cannot Add more than 3 Email addresses.')
        return 
    Label(root, text="Email({0}) :".format(types[d+1])).grid(row=17+d,column=1)
    e=Entry(root,width=37)
    e.grid(row=17+d,column=2)
    d+=1
    emails.append(e)
    Button(root,text='+',command=addEmail).grid(row=16+d,column=3)
    print "Email Field Added"
Button(root,text='+',command=addEmail).grid(row=16,column=3)
Label(root,text='   ').grid(row=25,column=3)
Label(root,text='           ').grid(row=25,column=7)
def clear():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    e7.delete(0, 'end')
    e8.delete(0, 'end')
    e9.delete(0, 'end')
    for i in phones:
        i.delete(0, 'end')
    for i in emails:
        i.delete(0, 'end')
###################################################
def save():
    cur.execute("insert into contact(FName,Mname,LName,Company,Address,City,PIN,Web,DOB) values(?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
    cur.execute('select id from contact order by id desc')
    idd=cur.fetchall()
    idd=idd[0][0]
    for i in range(len(phones)):
        cur.execute("insert into phone values(?,?,?)",(idd,types[i],phones[i].get()))
    for i in range(len(emails)):
        cur.execute("insert into email values(?,?,?)",(idd,types[i],emails[i].get()))
    print 'Contact :-'
    for i in cur.execute('select * from contact order by id'):
        print i
    print 'Phone :-'
    for i in cur.execute('select * from phone order by id'):
        print i
    print 'Email :-'
    for i in cur.execute('select * from email order by id'):
        print i
    con.commit()
    tkMessageBox.showinfo('Success', 'Contact Saved')
    print 'SAVED'
    clear()
Button(root,text='Save',command=save).grid(row=22,column=1)

def edit(idd=0):
    
    def show_search(e=0):
        
        def details(event=0):
            if idd==0:
                widget = event.widget
                selection=widget.curselection()
                l=[]
                entries=[]
                cur.execute("select * from contact where id = {0}".format((int)(names[(selection[0])][0])))
                det=cur.fetchall()
                for i in range(1,10):
                    l.append((str)(det[0][i]))
                root1.destroy()
                root2=Tk()
                Label(root2,text="EDIT",fg='blue',font=(None,20)).grid(row=1,column=2)
                att=['Full Name : ','Middle name : ','Last name : ','Company : ','Address : ','City : ','PIN : ','Website : ','Date of Birth  : ']
                for i in range(9):
                    Label(root2,text=att[i],font=(None,13)).grid(row=i+2,column=1)
                    e=Entry(root2,width=37)
                    e.grid(row=i+2,column=3)
                    e.insert(0,l[i])
                    entries.append(e)
                Label(root2,text='Email : ',font=(None,13)).grid(row=12,column=1)
                cur.execute("select email from email where id = {0}".format((int)(names[(selection[0])][0])))
                temp=cur.fetchall()
                l1=[]
                entries_mail=[]
                for i in temp:
                    l1.append((str)(i[0]))
                g=12    
                for i in l1:
                    e=Entry(root2,width=37)
                    e.grid(row=g,column=3)
                    e.insert(0,i)
                    entries_mail.append(e)
                    g+=1
                Label(root2,text='Phone : ',font=(None,13)).grid(row=15,column=1)
                cur.execute("select phone from phone where id = {0}".format((int)(names[(selection[0])][0])))
                temp=cur.fetchall()
                l2=[]
                entries_phone=[]
                for i in temp:
                    l2.append((str)(i[0]))
                g=15    
                for i in l2:
                    e=Entry(root2,width=37)
                    e.grid(row=g,column=3)
                    e.insert(0,i)
                    entries_phone.append(e)
                    g+=1
                def push():
                    cur.execute("update contact set FName='{0}',Mname='{1}',LName='{2}',Company='{3}',Address='{4}',City='{5}',PIN='{6}',Web='{7}',DOB='{8}' where id={9}".format(entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get(),entries[5].get(),entries[6].get(),entries[7].get(),entries[8].get(),(int)(names[(selection[0])][0])))
                    for i in range(len(entries_phone)):
                        cur.execute("update phone set phone={0} where id={1} and phone={2}".format(entries_phone[i].get(),(int)(names[(selection[0])][0]),temp[i][0]))
                    for i in range(len(entries_mail)):
                        cur.execute("update email set email='{0}' where id={1} and email='{2}'".format(entries_mail[i].get(),(int)(names[(selection[0])][0]),l1[i]))
                    con.commit()
                    tkMessageBox.showinfo('Success', 'Contact Saved')
                    print 'SAVED'
                Button(root2,text="Save",command=push).grid(row=20,column=2)
                root2.mainloop()
            else:
                selection=idd
                l=[]
                entries=[]
                cur.execute("select * from contact where id = {0}".format(idd))
                det=cur.fetchall()
                for i in range(1,10):
                    l.append((str)(det[0][i]))
                root2=Tk()
                Label(root2,text="EDIT",fg='blue',font=(None,20)).grid(row=1,column=2)
                att=['Full Name : ','Middle name : ','Last name : ','Company : ','Address : ','City : ','PIN : ','Website : ','Date of Birth  : ']
                for i in range(9):
                    Label(root2,text=att[i],font=(None,13)).grid(row=i+2,column=1)
                    e=Entry(root2,width=37)
                    e.grid(row=i+2,column=3)
                    e.insert(0,l[i])
                    entries.append(e)
                Label(root2,text='Email : ',font=(None,13)).grid(row=12,column=1)
                cur.execute("select email from email where id = {0}".format(idd))
                temp=cur.fetchall()
                l1=[]
                entries_mail=[]
                for i in temp:
                    l1.append((str)(i[0]))
                g=12    
                for i in l1:
                    e=Entry(root2,width=37)
                    e.grid(row=g,column=3)
                    e.insert(0,i)
                    entries_mail.append(e)
                    g+=1
                Label(root2,text='Phone : ',font=(None,13)).grid(row=15,column=1)
                cur.execute("select phone from phone where id = {0}".format(idd))
                temp=cur.fetchall()
                l2=[]
                entries_phone=[]
                for i in temp:
                    l2.append((str)(i[0]))
                g=15    
                for i in l2:
                    e=Entry(root2,width=37)
                    e.grid(row=g,column=3)
                    e.insert(0,i)
                    entries_phone.append(e)
                    g+=1
                def push():
                    cur.execute("update contact set FName='{0}',Mname='{1}',LName='{2}',Company='{3}',Address='{4}',City='{5}',PIN='{6}',Web='{7}',DOB='{8}' where id={9}".format(entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get(),entries[5].get(),entries[6].get(),entries[7].get(),entries[8].get(),idd))
                    for i in range(len(entries_phone)):
                        cur.execute("update phone set phone={0} where id={1} and phone={2}".format(entries_phone[i].get(),idd,temp[i][0]))
                    for i in range(len(entries_mail)):
                        cur.execute("update email set email='{0}' where id={1} and email='{2}'".format(entries_mail[i].get(),idd,l1[i]))
                    con.commit()
                    tkMessageBox.showinfo('Success', 'Contact Saved')
                    print 'SAVED'
                Button(root2,text="Save",command=push).grid(row=20,column=2)
                root2.mainloop()
        if idd==0:
            lb.delete(0,END)
            var= (str)(se.get())+e.char
            cur.execute("select id,fname,mname,lname from contact where FName like '%{0}%' or MName like '%{0}%' or LName like '%{0}%'".format(var))
            names=cur.fetchall()
            for i in names:
                t=((i[1])+' '+(i[2])+' '+(i[3]))
                print t
                lb.insert(END,t)
        else:
            details()
        lb.bind('<<ListboxSelect>>',details)
    if idd==0:
        root1=Tk()
        root1.geometry('350x450')
        Label(root1,text="SEARCH    PAGE",fg='blue',font=(None,15)).grid(row=1,column=1)
        se=Entry(root1,width=57)
        se.grid(row=2,column=1)
        lb=Listbox(root1,width=57,height=23,selectmode=SINGLE)
        lb.grid(row=3,column=1)
        
        se.bind('<Key>',show_search)
        root1.mainloop()
        print 'Searched'
    else:
        show_search()  
    
    print 'EDIT'




def search():    
    root1=Tk()
    root1.geometry('350x450')
    Label(root1,text="SEARCH    PAGE",fg='blue',font=(None,15)).grid(row=1,column=1)
    se=Entry(root1,width=57)
    se.grid(row=2,column=1)
    lb=Listbox(root1,width=57,height=23,selectmode=SINGLE)
    lb.grid(row=3,column=1)
   
    def show_search(e):
        lb.delete(0,END)
        var= (str)(se.get())+e.char
        cur.execute("select id,fname,mname,lname from contact where FName like '%{0}%' or MName like '%{0}%' or LName like '%{0}%'".format(var))
        names=cur.fetchall()
        for i in names:
            t=((i[1])+' '+(i[2])+' '+(i[3]))
            print t
            lb.insert(END,t)
        def details(event):
            widget = event.widget
            selection=widget.curselection()
            l=[]
            cur.execute("select type,phone from phone where id = {0}".format((int)(names[(selection[0])][0])))
            temp=cur.fetchall()
            s=''
            for i in temp:
                s+='({0}){1}'.format((str)(i[0]),(str)(i[1]))
                s+='    '
            l.append(s)
            cur.execute("select * from contact where id = {0}".format((int)(names[(selection[0])][0])))
            det=cur.fetchall()
            idd=det[0][0]
            for i in range(1,10):
                l.append((str)(det[0][i]))
            root1.destroy()
            root2=Tk()
            Label(root2,text="Details",fg='blue',font=(None,20)).grid(row=1,column=2)
            att=['Phone Number : ','Full Name : ','Middle name : ','Last name : ','Company : ','Address : ','City : ','PIN : ','Website : ','Date of Birth  : ']
            for i in range(10):
                Label(root2,text=att[i],font=(None,13)).grid(row=i+2,column=1)
                Label(root2,text=l[i],font=(None,12)).grid(row=i+2,column=3)
            Label(root2,text='Email : ',font=(None,13)).grid(row=12,column=1)
            cur.execute("select email_type,email from email where id = {0}".format((int)(names[(selection[0])][0])))
            temp=cur.fetchall()
            l1=[]
            for i in temp:
                l1.append('({0}) {1}'.format((str)(i[0]),(str)(i[1])))
            g=12    
            for i in l1:
                Label(root2,text=i,font=(None,12)).grid(row=g,column=3)
                g+=1
            def call_edit():
                edit(idd)
            def call_delete():
                ch=tkMessageBox.askyesno('Success', 'Are You sure you want to DELETE This Contact')
                if ch==True:
                    cur.execute('delete from contact where id={0}'.format(idd))
                    con.commit()
                    print idd
                    root2.destroy()
                    tkMessageBox.showinfo('Success', 'Deleted Contact')
                else:
                    tkMessageBox.showinfo('Operation Aborted', 'Contact NOT Deleted ')
                
            Button(root2,text='Edit',command=call_edit).grid(row=20,column=1)
            Button(root2,text='Delete',command=call_delete).grid(row=20,column=3)
            root2.mainloop()
        lb.bind('<<ListboxSelect>>',details)
            
    se.bind('<Key>',show_search)
    root1.mainloop()
    print 'Searched'







Button(root,text='Search',command=search).grid(row=22,column=2)
def close():
    print 'Closed'
    root.destroy()
Button(root,text='Close',command=close).grid(row=22,column=3)








Label(root,text='           ').grid(row=21,column=4)    
Button(root,text='Edit',command=edit).grid(row=22,column=5)
root.mainloop()
