import sqlite3

class DBC:
    def __init__(self):
        self._db=sqlite3.connect("Employees.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists Empconnect(ID integer primary key autoincrement,Name text NOT NULL,Status text NoT NULL)")
        self._db.commit()

    def Add(self,Name,Status):
        self._db.execute("insert into Empconnect(Name,Status)values(?,?)",(Name,Status))
        self._db.commit()
        return "Informations Saved"

    def ListInfo(self):
        cursor=self._db.execute("select * from Empconnect")
        return cursor;