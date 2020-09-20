from tkinter import *
from PIL import ImageTk, Image
import sys, os
import face_dataset as fd
import face_recognition as fr
from spreadsheets import * 
from spreadsheetsFR import *
from spreadsheetsSD import *
import webbrowser
import tkinter as tk

#our variables
ourgray = '#1a1c21'
font1 = "Bahnschrift"
c1 = '#991414'

# functions for other selfs
def wtitle(head, temp):
    space1 = tk.Label(temp, text="\n",bg = ourgray, font=("Helvetica", 8)).pack()
    heading = tk.Label(temp, text=head,bg = ourgray, fg='red', font=(font1, 16,"bold")).pack()
    space2 = tk.Label(temp, text="\n",bg = ourgray, font=("Helvetica", 8)).pack()

# social distancing
def sd():
    os.system('python social_distance_detector.py')

def sdstat():
    os.system('python showstatsd.py')


class RakshakApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class socialdistancing(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        wtitle("SOCIAL DISTANCING TRACKER", self)
        self.configure(bg=ourgray)
        btn1 = tk.Button(self, text="See the live stream", font=(font1,14),padx=20, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=sd).pack(pady=5)
        btn2 = tk.Button(self, text="See Statistics", font=(font1,14),padx=44, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=sdstat).pack(pady=5)
        tk.Button(self, text="Back",font=(font1,12),padx=20, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(StartPage)).pack(pady=50)
        


# facemask
def fm():
    os.system('python face_mask_detector.py')

class facemask(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        wtitle("FACE MASK DETECTOR", self)
        self.configure(bg=ourgray)
        btn1 = tk.Button(self, text="See the live stream",font=(font1,14),padx=20, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=fm).pack(pady=5)
        tk.Button(self, text="Back", font=(font1,12),padx=30, pady=10,bg=c1,fg='white',relief=RAISED,bd=6,command=lambda: master.switch_frame(StartPage)).pack(pady=50)
        


# Roaming COVID patients
class roamingCOVID(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        def namearr():
            arrname,arrstatus = showNameStatus()
            arrname[0] = ''
            arrstatus[0] = ''
            return arrname, arrstatus, len(arrname)
        
        def checknames():
            webbrowser.open('https://docs.google.com/spreadsheets/d/1aLH0dQFW3mN5vSxJdhjdQuAMTKojCDn-7mk6CNH3W68/edit?usp=sharing')
        
        wtitle("TRACKING COVID PATIENTS", self)
        self.configure(bg=ourgray)
        names,status, l=namearr()
        btn1 = tk.Button(self, text="See the live stream", font=(font1,14),padx=20, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command= lambda: fr.livestream(names,status,l)).pack(pady=5)
        btn2 = tk.Button(self, text="Check the names",font=(font1,14),padx=28, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=checknames).pack(pady=5)
        tk.Button(self, text="Back",font=(font1,12),padx=20, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(StartPage)).pack(pady=50)
        


# Add/delete COVID patients

class newpatient(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        wtitle("COVID PATIENTS DATABASE\n\nPlease select your choice...", self)
        self.configure(bg=ourgray)
        btn1 = tk.Button(self,text="Add a new patient", font=(font1,14),padx=50, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(addpatient)).pack(pady=5)
        btn2 = tk.Button(self, text="Delete an existing patient",font=(font1,14), padx=17, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(deletepatient)).pack(pady=5)
        tk.Button(self, text="Back",font=(font1,12),padx=10, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(StartPage)).pack()

#Add a new patient

class addpatient(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        def entername():
            count = idNumber()
            addPatient(count,e2.get(),radio.get())
            os.system('python face_training.py')
            idnum = "Your ID number is: {}".format(count)
            space3 = tk.Label(self, text=idnum, font=("Helvetica", 12),bg=ourgray, fg='green').pack(pady=5)


            
        def createset():
            fd.facedataset(idNumber())
            b1=e2.get()
            if(b1!=''):
                space2 = tk.Label(self, text="Image captured,'Submit' to save", font=("Helvetica", 10),bg=ourgray, fg='green').pack(pady=5)
                btn3.config(state=tk.NORMAL)
            else:
                warnlbl = tk.Label(self, text="Name is empty! Go back and try again!", font=("Helvetica", 10),bg=ourgray, fg='red').pack(pady=5)
            
        wtitle("ADD A NEW PATIENT'S DATABASE", self)
        self.configure(bg=ourgray)
        namelbl = tk.Label(self, text="Enter the patient's full name:", font=("Helvetica", 12),bg=ourgray,fg='white').pack(pady=5)
        e2 = tk.Entry(self, width=50)
        e2.pack()
        statuslbl = tk.Label(self, text="Choose patient status", font=("Helvetica", 12),bg=ourgray,fg='white').pack()
        radio = StringVar(self, "Positive")
        R1 = tk.Radiobutton(self, text="Positive patient",font=("Helvetica", 12) ,value = "Positive", variable = radio)
        R2 = tk.Radiobutton(self, text="At risk", font=("Helvetica", 12),value = "At risk",variable = radio)
        R1.pack()
        R2.pack()
        btn1 = tk.Button(self, text="Capture Image",font=(font1,10),padx=20, pady=5,bg=c1,fg='white',relief=RAISED,bd=6, command=createset)
        btn1.pack(side=LEFT)
        btn3 = tk.Button(self, text="SUBMIT", font=(font1,10),padx=40, pady=5,bg=c1,fg='white',relief=RAISED,bd=6,state=DISABLED, command=entername)
        btn3.pack(side=RIGHT)
        space1 = tk.Label(self, text="\n \n \n \n",bg = ourgray, font=("Helvetica", 8)).pack(pady=20)
        tk.Button(self, text="Back",font=(font1,12),padx=10, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(newpatient)).pack()


#Delete an existing patient

class deletepatient(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def dlt():
            flag=0
            n=e1.get()
            if(n!=''):
                try:
                    for i in range(80):
                        path="dataset/User."+str(n)+"."+str(i+1)+".jpg"
                        os.remove(path)
                except:
                    flag =1
                    infolbl = tk.Label(self, text="No patient found with entered ID!", font=("Helvetica", 10),bg=ourgray, fg='red').pack(pady=5)

                if(flag==0):
                    infolbl = tk.Label(self, text="Database deleted Succesfully!", font=("Helvetica", 10),bg=ourgray, fg='green').pack(pady=5)
                but1.configure(state=DISABLED)
                
            else:
                warnlbl = tk.Label(self, text="Invalid ID! Go back and try again!", font=("Helvetica", 10),bg=ourgray, fg='red').pack(pady=5)

        wtitle("DELETE AN EXISTING PATIENT'S DATABASE", self)
        self.configure(bg=ourgray)
        namelbl = tk.Label(self, text="Enter the patient's id:", font=("Helvetica", 12),bg=ourgray,fg='white').pack(pady=5)
        e1 = tk.Entry(self, width=50)
        e1.pack()
        but1=tk.Button(self, text="Delete dataset",font=(font1,13),padx=30, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=dlt)
        but1.pack(pady =40)
        tk.Button(self, text="Back",font=(font1,12),padx=20, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(newpatient)).pack(pady =3)
        

# main menu
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=ourgray)
        welLbl1 = tk.Label(self, text="\n", font=("Helvetica", 8),bg=ourgray)
        welLbl2 = tk.Label(self, text="WELCOME TO", fg='red', font=("Bahnschrift", 22, "bold"),bg=ourgray)
        welLbl3 = tk.Label(self, text="COVID RAKSHAK", fg='red', font=("Bahnschrift", 22,"bold" ),bg=ourgray)
        welLbl4 = tk.Label(self, text="\n", font=("Helvetica", 8),bg=ourgray)
        welLbl1.pack()
        welLbl2.pack()
        welLbl3.pack()
        welLbl4.pack()
        btn1 = tk.Button(self,text="Social Distancing Tracker", font=(font1,14),padx=50, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(socialdistancing)).pack(pady=5)
        btn2 = tk.Button(self, text="Face Mask Detector",font=(font1,14), padx=73, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(facemask)).pack(pady=5)
        btn3 = tk.Button(self,text="See if COVID patients are out",font=(font1,14), padx=33, pady=10, bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(roamingCOVID)).pack(pady=5)
        btn4 = tk.Button(self, text="Add/Delete COVID patients",font=(font1,14), padx=43, pady=10,bg=c1,fg='white',relief=RAISED,bd=6, command=lambda: master.switch_frame(newpatient)).pack(pady=5)



if __name__ == "__main__":
    app = RakshakApp()
    app.configure(bg=ourgray)
    app.resizable(width=False,height=False)
    app.title("COVID Rakshak")
    app.geometry("500x500+10+20")
    app.iconbitmap('trainer/logo2.ico')
    app.mainloop()
