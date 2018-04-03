import tkinter
import sqlite3


def connect():
    con = sqlite3.connect("mg.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbmg(id INTEGER PRIMARY KEY ,school TEXT , dat INTEGER,month INTEGER,year INTEGER,day TEXT,session TEXT,present INTEGER,total INTEGER) ")
    con.commit()
    con.close()

def insert(school,dat,month,year,day,session,present,total):
    con = sqlite3.connect("mg.db")
    cur = con.cursor()
    cur.execute("INSERT INTO tbmg VALUES(NULL,?,?,?,?,?,?,?,?)",(school,dat,month,year,day,session,present,total))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("mg.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tbmg")
    rows = cur.fetchall()
    con.close()
    return rows


def search(school="",dat="",month="",year="",day="",session="",present="",total=""):

    con = sqlite3.connect("mg.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tbmg WHERE school = ? OR dat = ? OR month = ? OR year = ? OR day = ? OR session = ? OR present = ? OR total = ? ",(school,dat,month,year,day,session,present,total))
    rows = cur.fetchall()
    con.close()
    return rows

def update(id,school,dat,month,year,day,session,present,total):
    con = sqlite3.connect("mg.db")
    cur = con.cursor()
    cur.execute("UPDATE tbmg SET school = ? ,dat = ?,month = ?,year= ?,day = ?,session = ?,present = ?,total = ? WHERE id = ?",(school,dat,month,year,day,session,present,total,id))
    con.commit()
    con.close()


def delete(id):
    con = sqlite3.connect("mg.db")
    cur = con.cursor()
    cur.execute("DELETE FROM tbmg WHERE id=?",(id,))
    con.commit()
    con.close()


