from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Databas import DBC
from Listinfo import INFO


DB = DBC()

root = Tk()
root.title("Employees Informations")
root.configure(background="lightblue")
root.geometry('700x300')
root.maxsize(700,300)
root.minsize(700,300)

#Style
style=ttk.Style()
style.theme_use('alt')
style.configure('TLabel',background='lightblue')
style.configure('TButton',background='#FDF5E6')

#Logo
ttk.Label(root,font=('Calibri',20,'bold'),text="CodeForIraq").grid(row=0,column=3,columnspan=2,padx=10)
can1 = Canvas(root,width =160, height =160,bg ='lightblue')
can1.grid(row =1,column=3,rowspan=2,columnspan=2)
photo = PhotoImage(file ='logo.gif')
PHOTO = photo.subsample(10,10)
item = can1.create_image(80,80,image=PHOTO)


#Full Name
ttk.Label(root,font=('Calibri',18,'bold'),text="Full Name :").grid(row=1,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root,width=20,font=('Calibri',18,'bold'))
EntryFullName.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

#Employ status
ttk.Label(root,font=('Calibri',18,'bold'),text="Employ Status :").grid(row=2,column=0,padx=10,pady=10)
EntryStatus=ttk.Entry(root,width=20,font=('Calibri',18,'bold'))
EntryStatus.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

#Buttons
BuSave = ttk.Button(root,text="Save Info")
BuSave.grid(row=4,column=1)

BuViewList = ttk.Button(root,text="View List")
BuViewList.grid(row=4,column=2)


BuExit = ttk.Button(root,text="Exit",command=root.quit)
BuExit.grid(row=4,column=3)

def BuSaveData():
    if EntryFullName.get()=='' or EntryStatus.get()=='':
        messagebox.showinfo(title='No data',message="Please fill all fields!")
    else:
        msg=DB.Add(EntryFullName.get(),EntryStatus.get())
        messagebox.showinfo(title="Add info",message=msg)
        EntryFullName.delete(0,'end')
        EntryStatus.delete(0,'end')

def BuList():
    Listdata=INFO()


BuSave.config(command=BuSaveData)
BuViewList.config(command=BuList)


root.mainloop()