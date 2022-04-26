import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox as mb

from sympy import false


class DB:                         
    def __init__(self):           
        self.connection = sqlite3.connect("mybooks.db")  
        self.cursor = self.connection.cursor()   
        self.cursor.execute(             
            "CREATE TABLE IF NOT EXISTS library (name text, author text, isbn integer, year integer)")
        self.connection.commit()  
    def __del__(self):          
        self.connection.close()   

    def view(self):
        self.cursor.execute("SELECT * FROM library ")
        rows = self.cursor.fetchall()
        return rows

        
    def insert(self, name, author , isbn, year ): 
        self.cursor.execute("INSERT INTO library VALUES (?,?,?,?)", ( name, author , isbn, year,)) 
        self.connection.commit()
        self.view()
        
    def delete(self, isbn):                   
        self.cursor.execute("DELETE FROM library WHERE isbn=?", [isbn])
        self.connection.commit()
        self.view()



data = DB()



def delete_command():  

    #mb.showwarning("Warning", "Delete button working ONLY with ISBN")

    data.delete(isbn.get())

    isbn.delete(0, END)
    

def view_():
    for row in data.view():
        print(row)

def add_to_database():
    data.insert(name_e.get(),author.get(),isbn.get(),year.get())
    name_e.delete(0, END)
    author.delete(0, END)
    isbn.delete(0, END)
    year.delete(0, END)


root=tk.Tk()
root.geometry("500x300")

name=Canvas(root,width=300,height=100)
name.place(x=0,y=0)
name.create_text(30,50,text="Name: ")
root.title("Library Project")
Author=Canvas(root,width=300,height=100)
Author.place(x=0,y=100)
Author.create_text(30,10,text="Author: ")

ISBN=Canvas(root,width=300,height=100)
ISBN.place(x=0,y=150)
ISBN.create_text(25,10,text="ISBN: ")

Year=Canvas(root,width=300,height=100)
Year.place(x=0,y=200)
Year.create_text(25,10,text="Year: ")

name_e= Entry(root, width=30)
name_e.place(x=80,y=40)

author= Entry(root, width=30)
author.place(x=80,y=100)

year= Entry(root, width= 30)
year.place(x=80, y=200)

isbn= Entry(root, width= 30)
isbn.place(x=80, y=150)

add= tk.Button(text="Add to database", command= add_to_database)
add.place(x=350,y=40)

add = tk.Button(text="See DataBase", command= view_)
add.place(x=350,y=80)

delete = tk.Button(text="Delete elements", command=delete_command)
delete.place(x=350,y=120)

root.mainloop()