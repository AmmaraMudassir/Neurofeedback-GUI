
import Tkinter
import os
import sqlite3
import shutil
import tkMessageBox
from Tkinter import Tk, Menu, Canvas
import xlwt
import time

from time import sleep
import serial
from serial import Serial
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import PIL
from PIL import Image, ImageTk

def nothing1():
    answer = tkMessageBox.askquestion( 'Welcome to NeuroFeedback', "Are you a new entry?")

    if answer == 'no':

        root1 = Tk()
        lab_1 = Tkinter.Label(root1, text="Please enter your ID Number")
        global ID
        ID=Tkinter.IntVar()
        ent_1 = Tkinter.Entry(root1, text= ID)
        lab_1.grid(row=0)
        ent_1.grid(row=0, column=1)


        def p():
            per_id=ID.get()
            list_of_files = os.listdir('C:/Users/AMMAR ZAHID/Desktop/potentiometer/emotiv')
            if per_id in list_of_files:
             ans=tkMessageBox.showinfo("Saved","Kindly process to next step")
             print ("saved")



        b = Tkinter.Button(root1, text="submit", bg='blue', fg='white', command=p)
        b.grid(columnspan=4)

        root1.mainloop()

    elif answer  ==  'yes':
        root.geometry('500x500')
        root.title("Registration Form")

        Name = Tkinter.StringVar()
        Age = Tkinter.StringVar()
        var_chk = Tkinter.IntVar()
        Session = Tkinter.IntVar()
        Day = Tkinter.IntVar()

        def database():
            Name1 = Name.get()
            age = Age.get()
            gender = var_chk.get()
            session = Session.get()
            day = Day.get()
            

            if gender == 1:
                ID_number = 12000
                ID_number += 1
                dirName = str(ID_number)
                while os.path.exists(dirName):
                    ID_number = int(dirName)
                    ID_number += 1
                    dirName = str(ID_number)
                print dirName


            if gender == 2:
                ID_number = 11000
                ID_number += 1
                dirName = str(ID_number)
                while os.path.exists(dirName):
                    ID_number = int(dirName)
                    ID_number += 1
                    dirName = str(ID_number)

                print dirName






            ask=tkMessageBox.showinfo("Registration Successfull",dirName + " is your ID number.kindly remember this for next time login.")
            os.mkdir(dirName)
            v=os.getcwd()
            print v
            #path='C:/Users/AMMAR ZAHID/Desktop/potentiometer/emotiv/'+ dirName 
            #os.mkdir( path, day )
            #os.makedirs(os.path.join(dirName, day))


            wb = xlwt.Workbook()
            sheet1 = wb.add_sheet('Sheet 1')
            sheet1.write(0, 0, "Name")
            sheet1.write(0, 1, Name1)
            sheet1.write(1, 0, "Session")
            sheet1.write(1, 1, session)
            sheet1.write(2, 0, "Age")
            sheet1.write(2, 1, age)
            sheet1.write(3, 0, "Gender")
            if gender == 1:
             sheet1.write(3, 1,"Male")
            elif gender ==2:
                sheet1.write(3, 1, "Female")
            sheet1.write(4, 0, "Day")
            sheet1.write(4,1,day)
            wb.save('user_info.xls')

            # path = 'C:/Users/s33us/.PyCharmCE2019.1/config/scratches/' + dirName + '/'
            # filename = os.path.join(path, file)
            shutil.move("user_info.xls", dirName)
            


        label_0 = Tkinter.Label(root, text="Registration form", bg='white', width=20, font=("bold", 20))
        label_0.place(x=65, y=85)

        label_1= Tkinter.Label(root, text="Name", width=20, font=("bold", 10))
        label_1.place(x=70, y=130)

        entry_1= Tkinter.Entry(root, textvar=Name, width=20)
        entry_1.place(x=250, y=130)

        label_2= Tkinter.Label(root, text="Age", width=20, font=("bold", 10))
        label_2.place(x=70, y=180)

        entry_2 = Tkinter.Entry(root, textvar=Age)
        entry_2.place(x=250, y=180)

        label_3 = Tkinter.Label(root, text="Gender", width=20, font=("bold", 10))
        label_3.place(x=70, y=230)

        Tkinter.Radiobutton(root, text="Male", padx=5, variable=var_chk, value=1).place(x=250, y=230)
        Tkinter.Radiobutton(root, text="Female", padx=20, variable=var_chk, value=2).place(x=310, y=230)

        label_4 = Tkinter.Label(root, text="Session", width=20, font=("bold", 10))
        label_4.place(x=70, y=280)

        entry_3 = Tkinter.Entry(root, textvar=Session)
        entry_3.place(x=250, y=280)

        label_4 = Tkinter.Label(root, text="Day", width=20, font=("bold", 10))
        label_4.place(x=70, y=330)
        entry_4 = Tkinter.Entry(root, textvar=Day)
        entry_4.place(x=250, y=330)

        Tkinter.Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=70, y=380)
        Tkinter.Button(root, text="Next",width=20, bg='brown', fg='white', command=lambda:[baseline()]).place(x=250, y=380)
        root.mainloop()

        

def ed():
    print("Quit")
    root.quit()
def baseline():
    root=Tkinter.Toplevel()
    #root.geometry("730x450")
    root.title("Testing")
    img2 = ImageTk.PhotoImage(Image.open("efg.jpg"))
    w, h = img2.width(), img2.height() 
    canvas = Canvas(root, width=w , height=h)
    canvas.pack(fill = "both")
    canvas.create_image(0, 0, anchor=Tkinter.NW, image=img2)
    canvas.image = img2
    Tkinter.Button(root,text= "BASELINE RECORDING", width= 30, bg= "blue", fg= "white", command= testing).place(x=100, y=50)
    Tkinter.Button(root,text= "START TRAINING", width= 30, bg= "blue", fg= "white", command= EEG).place(x=100, y=100)
    Tkinter.Button(root, text= "GO BACK", width= 30, bg= "blue", fg= "white", command= nothing1).place(x=100, y= 150)
def testing():
    import Data_collection3
    from Data_collection3 import CollectData

def alpha():
    print 'Alpha'+str(v1.get())
    #print 'beta'+str(v2.get())
    #print 'gamma'+str(v3.get())
    #print 'theta'+str(v4.get())
    #print 'delta'+str(v5.get())
    #print 'channel 1'+str(v6.get())
    #print 'channel 2'+str(v7.get())
    if v1.get()== 1 and v2.get()==0 and v6.get()==1:
     print "Alpha channel 1"
     import Data_collection
     from Data_collection import CollectData
    elif v1.get()==1 and v2.get()==1 and v6.get()==1:
     print "Alpha and beta channel 1"
     import Data_collection2
     from Data_collection2 import CollectData

def EEG():

    frame1=Tkinter.Toplevel()
    frame1.title("selection of Band and Channel")
    frame2=Tkinter.Frame(frame1)
    frame2.pack(side="left")
    label=Tkinter.Label(frame2, text="Select band",bg='light blue', font=("bold", 10))
    label.pack()
    global v1
    v1=Tkinter.IntVar()
    box1=Tkinter.Checkbutton(frame2, text="Alpha",variable=v1)
    box1.pack()
    global v2
    v2=Tkinter.IntVar()
    box2=Tkinter.Checkbutton(frame2, text="Beta", variable=v2)
    box2.pack()
    global v3
    v3=Tkinter.IntVar()
    box3=Tkinter.Checkbutton(frame2, text="Gamma", variable=v3)
    box3.pack()
    global v4
    v4=Tkinter.IntVar()
    box4=Tkinter.Checkbutton(frame2, text="Theta", variable=v4)
    box4.pack()
    global v5
    v5=Tkinter.IntVar()
    box5=Tkinter.Checkbutton(frame2, text="Delta", variable=v5)
    box5.pack()
    frame3=Tkinter.Frame(frame1)
    frame3.pack(side="left")
    labe2=Tkinter.Label(frame3, text="Select channel",bg='light blue', font=("bold", 10))
    labe2.pack()
    global v6
    v6=Tkinter.IntVar()
    box6=Tkinter.Checkbutton(frame3, text="Channel 1", variable=v6)
    box6.pack()
    global v7
    v7=Tkinter.IntVar()
    box7=Tkinter.Checkbutton(frame3, text="Channel 2", variable=v7)
    box7.pack()
    global v8
    v8=Tkinter.IntVar()
    box8=Tkinter.Checkbutton(frame3, text="Channel 3", variable=v8)
    box8.pack()
    global v9
    v9=Tkinter.IntVar()
    box9=Tkinter.Checkbutton(frame3, text="Channel 4", variable=v9)
    box9.pack()
    global v10
    v10=Tkinter.IntVar()
    box10=Tkinter.Checkbutton(frame3, text="Channel 5", variable=v10)
    box10.pack()
    global v11
    v11=Tkinter.IntVar()
    box11=Tkinter.Checkbutton(frame3, text="Channel 6", variable=v11)
    box11.pack()
    global v12
    v12=Tkinter.IntVar()
    box12=Tkinter.Checkbutton(frame3, text="Channel 7", variable=v12)
    box12.pack()
    global v13
    v13=Tkinter.IntVar()
    box13=Tkinter.Checkbutton(frame3, text="Channel 8", variable=v13)
    box13.pack()
    global v14
    v14=Tkinter.IntVar()
    box14=Tkinter.Checkbutton(frame3, text="Channel 9", variable=v14)
    box14.pack()
    global v15
    v15=Tkinter.IntVar()
    box15=Tkinter.Checkbutton(frame3, text="Channel 10", variable=v15)
    box15.pack()
    global v16
    v16=Tkinter.IntVar()
    box16=Tkinter.Checkbutton(frame3, text="Channel 11", variable=v16)
    box16.pack()
    global v17
    v17=Tkinter.IntVar()
    box17=Tkinter.Checkbutton(frame3, text="Channel 12", variable=v17)
    box17.pack()
    global v18
    v18=Tkinter.IntVar()
    box18=Tkinter.Checkbutton(frame3, text="Channel 13", variable=v18)
    box18.pack()
    global v19
    v19=Tkinter.IntVar()
    box19 = Tkinter.Checkbutton(frame3, text="Channel 14", variable=v19)
    box19.pack()
    button = Tkinter.Button(frame3, text="Submit", command= alpha)
    button.pack()
    button = Tkinter.Button(frame3, text="Skip and next", command= protocol).pack()

def protocol():
    root4=Tkinter.Toplevel()
    root4.title("TRAINING")
    labe3=Tkinter.Label(root4, text="TRAINING APPLICATION",bg='light blue', font=("bold", 10)).pack()
    global var_chk1
    var_chk1=Tkinter.IntVar()
    Tkinter.Radiobutton(root4, text="ADHD", variable=var_chk1, value=1, width=20).pack()
    Tkinter.Radiobutton(root4, text="Stress", variable=var_chk1, value=2,width=20).pack()
    Tkinter.Radiobutton(root4, text="Anxiety", variable=var_chk1, value=3,width=20).pack()
    Tkinter.Radiobutton(root4, text="Peak performance", variable=var_chk1, value=4,width=20).pack()
    Tkinter.Button(root4, text="Next", command=selectprotocol).pack()
def selectprotocol():
    print var_chk1.get()
    if var_chk1.get()==4:
            root5=Tkinter.Toplevel()
            labe3=Tkinter.Label(root5, text="SELECT PROTOCOL",bg='light green', font=("bold",20)).pack()
            labe4=Tkinter.Label(root5, text="Improvement of Attention",bg='light blue', font=("bold", 10)).pack()
            global var_chk2
            var_chk2=Tkinter.IntVar()
            Tkinter.Radiobutton(root5, text="Increase beta", variable=var_chk2, value=1, width=20).pack()
            Tkinter.Radiobutton(root5, text="Reduce theta", variable=var_chk2, value=2,width=20).pack()
            labe5=Tkinter.Label(root5, text="Improvement of Relaxation",bg='light blue', font=("bold", 10)).pack()
            Tkinter.Radiobutton(root5, text="Increase Apha", variable=var_chk2, value=3, width=20).pack()
            Tkinter.Radiobutton(root5, text="Increase theta", variable=var_chk2, value=4,width=20).pack()
            labe6=Tkinter.Label(root5, text="Assistance with meditation",bg='light blue', font=("bold", 10)).pack()
            Tkinter.Radiobutton(root5, text="Increase Apha", variable=var_chk2, value=5, width=20).pack()
            Tkinter.Radiobutton(root5, text="Increase theta", variable=var_chk2, value=6,width=20).pack()
            Tkinter.Button(root5, text="Submit", command=startprotocol).pack()
            
        
def startprotocol():
    if var_chk2.get()==1:
        print "hi"
        import Data_collection4
        from Data_collection4 import CollectData
    

   
root = Tk()

root.geometry("1024x800")
menu = Menu(root)
root.config(menu=menu)


subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)

subMenu.add_command(label="New", command=nothing1)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=ed)

viewMenu = Menu(menu)
menu.add_cascade(label="Testing", menu=viewMenu)
viewMenu.add_command(label="Add", command=baseline)

canvas = Canvas(root, width=1024 , height=768)
canvas.pack(fill="both")

rect1 = canvas.create_rectangle(0,0,1024,768, fill="pink")
img = ImageTk.PhotoImage(Image.open("abd.jpg"))
canvas.create_image(0, 0, anchor=Tkinter.NW, image=img)
canvas.image = img


root.mainloop()
