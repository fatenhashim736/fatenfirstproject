from tkinter import *
from tkinter import ttk
from Databas import DBC

dbconnect=DBC()

class INFO:
    def __init__(self):
        self._root=Tk()
        self._dbconnect=DBC()
        tv=ttk.Treeview(self._root)
        tv.pack()
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Status'))
        tv.heading('#Name',text='Name')
        tv.heading('#Status',text='Status')
        cursor=self._dbconnect.ListInfo()

        for row in cursor:
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Status',row['Status'])

        self._root.mainloop()