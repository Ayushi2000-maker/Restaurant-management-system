from tkinter import *
from tkinter import ttk
import time
root=Tk()
root.title("my restaurant system")
add_item={}
check=[]
prize=[50,50,100,50,50,50,120,150,100,150,50,80]
add={'CORN PIZZA':1,'CHEESE PIZZA':2,'CHOCOLATE PASTRY':3,'VANILLA PASTRY':4,'WHITE SAUCE':5,'RED SAUCE':6,'ITALIC SIZLER':7,'MEXICAN SIZLER':8,'ITALIC BURGER':9,'MEXICAN BURGER':10,'PAPAYA JUICE':11,'CHOCOLATE JUICE':12}
def fun(event):
    listing['bg']='pink'
def fun1(event):
    listing['bg']='white'
def Time():
    l['text']=time.ctime()
    l.after(1000,Time)
def binding(event):
    global cur
    curselect=listing.curselection()[0]
    cur=listing.get(curselect)
def total():
    global l
    l.destroy()
    total=0
    for i,j in add_item.items():
        total=total+prize[i-1]*int(j)
    l=Label(listing,text='Welcome to Khayo piyo  Total=%d'%total,font='times 10 italic')
    l.pack(side=BOTTOM,fill=BOTH)
def add_to_list():
    global l
    l.destroy()
    global index
    global text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12
    if  text1.get() and '1' not in check:
            listing.insert(index,'CORN PIZZA-%s'%text1.get())
            index+=1
            check.append('1')
            add_item[1]=text1.get()    
    if  text2.get() and '2' not in check:
            listing.insert(index,'CHEESE PIZZA-%s'%text2.get())
            index+=1
            check.append('2')
            add_item[2]=text2.get() 
    if  text3.get() and '3' not in check:
            listing.insert(index,'CHOCOLATE PASTRY-%s'%text3.get())
            index+=1
            check.append('3')
            add_item[3]=text3.get() 
    if  text4.get() and '4' not in check:
            listing.insert(index,'VANILLA PASTRY-%s'%text4.get())
            index+=1
            check.append('4')
            add_item[4]=text4.get() 
    if  text5.get() and '5' not in check:
            listing.insert(index,'WHITE SAUCE-%s'%text5.get())
            index+=1
            check.append('5')
            add_item[5]=text5.get() 
    if  text6.get() and '6' not in check:
            listing.insert(index,'RED SAUCE-%s'%text6.get())
            index+=1
            check.append('6')
            add_item[6]=text6.get() 
    if  text7.get() and '7' not in check:
            listing.insert(index,'ITALIC SIZLER-%s'%text7.get())
            index+=1
            check.append('7')
            add_item[7]=text7.get() 
    if text8.get()  and '8' not in check:
            listing.insert(index,'MEXICAN SIZLER-%s'%text8.get())
            index+=1
            check.append('8')
            add_item[8]=text8.get() 
    if  text9.get()  and '9' not in check:
            listing.insert(index,'ITALIC BURGER-%s'%text9.get())
            index+=1
            check.append('9')
            add_item[9]=text9.get() 
    if  text10.get() and '10' not in check:
            listing.insert(index,'MEXICAN BURGER-%s'%text10.get())
            index+=1
            check.append('10')
            add_item[10]=text10.get() 
    if  text11.get() and '11' not in check:
            listing.insert(index,'PAPAYA JUICE-%s'%text11.get())
            index+=1
            check.append('11')
            add_item[11]=text11.get() 
    if  text12.get() and '12' not in check:
            listing.insert(index,'CHOCOLATE JUICE-%s'%text12.get())
            check.append('12')
            add_item[12]=text12.get()     
    index=0    
def delete():
    global l
    l.destroy()
    global cur
    cur=cur.split('-')
    select=add[cur[0]]
    add_item.pop(select)
    listing.delete(ANCHOR)
    
    
index=0
global l
global listing
f1=Frame(root,bg='yellow')
f2=Frame(root,bg='powder blue')
l=Label(root,text='Khayo Piyo Restaurant',bg='black',fg='red',height=1,font='Calibri 20 bold')
l.pack(side=TOP,fill=BOTH)
f1.pack(side=LEFT,expand=YES,fill=BOTH)
f2.pack(side=LEFT,expand=YES,fill=BOTH)
f3=Frame(root,bg='white')
f3.pack(side=LEFT,fill=BOTH,expand=YES)
img=PhotoImage(file='E:\\images\\pizza.png')
l1=Label(f1,bg='white',image=img)
l1.pack(side=TOP,fill=BOTH,padx=12,pady=12,expand=YES)
im=PhotoImage(file='E:\\images\\pastry.png')
l2=Label(f1,bg='white',image=im)
l2.pack(side=TOP,fill=BOTH,padx=12,pady=12,expand=YES)
im1=PhotoImage(file='E:\\images\\pasta.png')
l3=Label(f1,bg='white',image=im1)
l3.pack(side=TOP,fill=BOTH,padx=12,pady=12,expand=YES)
im2=PhotoImage(file='E:\\images\\sizzler.png')
l4=Label(f2,bg='white',image=im2)
l4.pack(side=TOP,fill=BOTH,padx=12,pady=12,expand=YES)
im3=PhotoImage(file='E:\\images\\burger.png')
l5=Label(f2,bg='white',image=im3)
l5.pack(side=TOP,fill=BOTH,padx=12,pady=12,expand=YES)
im4=PhotoImage(file='E:\\images\\juice.png')
l6=Label(f2,bg='white',image=im4)
l6.pack(side=TOP,fill=BOTH,padx=12,pady=12,expand=YES)
listlabel=Label(f3)
listlabel.pack(fill=BOTH,expand=YES)
label1=Label(listlabel,text='RECEIPT',font='Calibri 20 bold')
label1.pack(side=TOP,fill=BOTH)
listing=Listbox(listlabel)
listing.pack(expand=YES,fill=BOTH)
listing.bind('<<ListboxSelect>>',binding)
listing.bind('<Enter>',fun)
listing.bind('<Leave>',fun1)

listlabel=Label(listing)
label1.pack(side=TOP,fill=BOTH)
b2=ttk.Button(f3,text='add',command=add_to_list)
b2.pack(side=LEFT)
b3=ttk.Button(f3,text='delete',command=delete)
b3.pack(side=LEFT)
b4=ttk.Button(f3,text='total',command=total)
b4.pack(side=LEFT)
l=Label(f3)
Time()

l.pack(side=LEFT,fill=BOTH,expand=YES)
la1=Label(l1,text='PIZZA',font='arial 20 bold')
la1.pack(side=TOP,fill=BOTH)
la2=Label(l2,text='PASTRY',font='arial 20 bold')
la2.pack(side=TOP,fill=BOTH)
la3=Label(l3,text='PASTA',font='arial 20 bold')
la3.pack(side=TOP,fill=BOTH)
la4=Label(l4,text='SIZLER',font='arial 20 bold')
la4.pack(side=TOP,fill=BOTH)
la5=Label(l5,text='BURGER',font='arial 20 bold')
la5.pack(side=TOP,fill=BOTH)
la6=Label(l6,text='JUICE',font='arial 20 bold')
la6.pack(side=TOP,fill=BOTH)
label11=Label(l1,bg='white')
label11.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labela=ttk.Label(label11,text='CORN',font='arial 12 bold',width=15)
labela.pack(side=LEFT,padx=10,pady=2)
labela1=ttk.Label(label11,text='50',font='arial 12 bold')
labela1.pack(side=LEFT,padx=10,pady=2,fill=BOTH)
label12=Label(l1,bg='white')
label12.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labelb=ttk.Label(label12,text='CHEESE',font='arial 12 bold',width=15)
labelb.pack(side=LEFT,padx=10,pady=2)
text1=StringVar()
e1=Entry(label11,textvariable=text1,bd=4,relief=RAISED)
e1.pack(side=LEFT)

labelb1=ttk.Label(label12,text='50',font='arial 12 bold')
labelb1.pack(side=LEFT,padx=10,pady=2)
text2=StringVar()
e2=Entry(label12,textvariable=text2,bd=4,relief=RAISED)
e2.pack(side=LEFT)
label11=Label(l2,bg='white')
label11.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labela=ttk.Label(label11,text='CHOCOLATE',font='arial 12 bold',width=15)
labela.pack(side=LEFT,padx=10,pady=2)
labela1=ttk.Label(label11,text='100',font='arial 12 bold')
labela1.pack(side=LEFT,padx=10,pady=2,fill=BOTH)
label12=Label(l2,bg='white')
label12.pack(fill=BOTH,side=TOP,padx=10,pady=10)
text3=StringVar()
e3=Entry(label11,textvariable=text3,bd=4,relief=RAISED)
e3.pack(side=LEFT)
labelb=ttk.Label(label12,text='VANILLA',font='arial 12 bold',width=15)
labelb.pack(side=LEFT,padx=10,pady=2)
labelb1=ttk.Label(label12,text='50',font='arial 12 bold')
labelb1.pack(side=LEFT,padx=10,pady=2)
text4=StringVar()
e4=Entry(label12,textvariable=text4,bd=4,relief=RAISED)
e4.pack(side=LEFT)
label11=Label(l3,bg='white')
label11.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labela=ttk.Label(label11,text='white sauce',font='arial 12 bold',width=15)
labela.pack(side=LEFT,padx=10,pady=2)
labela1=ttk.Label(label11,text='50',font='arial 12 bold')
labela1.pack(side=LEFT,padx=10,pady=2,fill=BOTH)
text5=StringVar()
e5=Entry(label11,textvariable=text5,bd=4,relief=RAISED)
e5.pack(side=LEFT)
label12=Label(l3,bg='white')
label12.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labelb=ttk.Label(label12,text='red sauce',font='arial 12 bold',width=15)
labelb.pack(side=LEFT,padx=10,pady=2)

labelb1=ttk.Label(label12,text='50',font='arial 12 bold')
labelb1.pack(side=LEFT,padx=10,pady=5)
text6=StringVar()
e6=Entry(label12,textvariable=text6,bd=4,relief=RAISED)
e6.pack(side=LEFT)
label11=Label(l4,bg='white')
label11.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labela=ttk.Label(label11,text='ITALIC',font='arial 12 bold')
labela.pack(side=LEFT,padx=10,pady=2)
labela1=ttk.Label(label11,text='120',font='arial 12 bold')
labela1.pack(side=LEFT,padx=10,pady=2,fill=BOTH)
text7=StringVar()
e7=Entry(label11,textvariable=text7,bd=4,relief=RAISED)
e7.pack(side=LEFT)
label12=Label(l4,bg='white')
label12.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labelb=ttk.Label(label12,text='MEXICAN',font='arial 12 bold')
labelb.pack(side=LEFT)
labelb1=ttk.Label(label12,text='150',font='arial 12 bold')
labelb1.pack(side=LEFT,padx=10,pady=5)
text8=StringVar()
e8=Entry(label12,textvariable=text8,bd=4,relief=RAISED)
e8.pack(side=LEFT)
label11=Label(l5,bg='white')
label11.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labela=ttk.Label(label11,text='ITALIC',font='arial 12 bold')
labela.pack(side=LEFT,padx=10,pady=2)
labela1=ttk.Label(label11,text='100',font='arial 12 bold')
labela1.pack(side=LEFT,padx=10,pady=2,fill=BOTH)
text9=StringVar()
e9=Entry(label11,textvariable=text9,bd=4,relief=RAISED)
e9.pack(side=LEFT)
label12=Label(l5,bg='white')
label12.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labelb=ttk.Label(label12,text='MEXICAN',font='arial 12 bold')
labelb.pack(side=LEFT)
labelb1=ttk.Label(label12,text='150',font='arial 12 bold')
labelb1.pack(side=LEFT,padx=10,pady=5)
text10=StringVar()
e10=Entry(label12,textvariable=text10,bd=4,relief=RAISED)
e10.pack(side=LEFT)
label11=Label(l6,bg='white')
label11.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labela=ttk.Label(label11,text='PAPAYA',font='arial 12 bold',width=15)
labela.pack(side=LEFT,padx=10,pady=2)
labela1=ttk.Label(label11,text='50',font='arial 12 bold')
labela1.pack(side=LEFT,padx=10,pady=2,fill=BOTH)
text11=StringVar()
e11=Entry(label11,textvariable=text11,bd=4,relief=RAISED)
e11.pack(side=LEFT)
label12=Label(l6,bg='white')
label12.pack(fill=BOTH,side=TOP,padx=10,pady=10)
labelb=ttk.Label(label12,text='CHOCOLATE',font='arial 12 bold',width=15)
labelb.pack(side=LEFT,padx=10,pady=2)
labelb1=ttk.Label(label12,text='80',font='arial 12 bold')
labelb1.pack(side=LEFT,padx=10,pady=2)
text12=StringVar()
e12=Entry(label12,textvariable=text12,bd=4,relief=RAISED)
e12.pack(side=LEFT)




