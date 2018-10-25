
#For your individual mid semester project: design a retail related application of your own design. Incorporate as many
#  as possible of the new programming features you have discovered this semester.

#Include and use a module of your own functions. Create and use a database, including queries, insert, update, and
#  delete options. Include a menu of options. Design the user interface and make it friendly.

#Upload a single document containing all your code and clear screen shots of your logic working. Include all the menu
#  and logical options.


import tkinter as tk
from tkinter import *

from PIL import Image, ImageTk  # added Pillow in settings
from functools import partial

import sqlite3
from sqlite3 import Error
import sqlDatabaseForRetail

sqlDatabaseForRetail.create_database_and_table()  # should create the database And table I will use

LARGE_FONT = ("Verdana", 18)

NOT_GONNA_HAPPEN = "NOT_GONNA_HAPPEN"

#numberOfPounds = tk.StringVar()


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Retail")  # title of window
        #self.pack(fill=BOTH, expand=1)  # adjust dimensions as needed
        self.grid()

        nameLabel = Label(text="Name: ", background="powder blue")
        nameLabel.grid(column=1, row=5)

        nameVariable = tk.StringVar()
        namer = Entry(textvariable=nameVariable, width=20)
        namer.grid(column=2, row=5, sticky=E)

        potatoLabel = Label(text="This is the Potato selling ", font=LARGE_FONT)
        #potatoLabel.place(x=0, y=0)
        potatoLabel.grid(column=1, row=1)

        potatoLabel2 = Label(text="Retail App", font=("Arial Bold", 20))
        # potatoLabel.place(x=0, y=0)
        potatoLabel2.grid(column=1, row=2)

        priceLabel = Label(text="One pound of potato's for 0.73", font=("Arial Bold", 12))
        priceLabel.grid(column=1, row=3)

        label3 = Label(text="Purchase potatoes by pound:", font=("Arial Bold", 12))
        label3.grid(column=1, row=4)

        numberOfPounds = tk.StringVar()
        potatoPurchase = Entry(textvariable=numberOfPounds, width=20)
        potatoPurchase.grid(column=2, row=4, sticky=E)

        totalLabel = Label(self)
        totalLabel.grid(column=2, row=8)

        #call_result = partial(Window.buyPounds, totalLabel, numberOfPounds)
        buyButton = Button(text="Buy", command=None, background="orange", font=("Arial Bold", 20))
        #quitButton = Button(self, text="Exit", command=self.user_exit, background="orange", font=("Arial Bold", 20))
        #quitButton.place(x=0, y=0)  # places on location with x and y
        buyButton.grid(column=1, row=8)

        quitButton2 = Button( text="Exit", command=self.user_exit, background="white", font=("Arial Bold", 20))  # TODO change button name
        # quitButton.place(x=0, y=0)  # places on location with x and y
        quitButton2.grid(column=1, row=9)

        # below is the file menu stuff that you usually see in any application
        menu = Menu(self.master)  # menu variable, Menu is tk object
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Save", command=self.saveData(Purchister=namer.get(), amount=potatoPurchase.get()))  #

        file.add_command(label="Update", command=self.saveData(Purchister=namer.get(), amount=potatoPurchase.get()))  #

        file.add_command(label="Search and Load", command=self.loadSelectData(Purchisie=namer.get()))  #

        file.add_command(label="Load", command=self.loadAllData)  #

        file.add_command(label="Delete select", command=self.deleteSelectData(Purchisie=namer.get()))  #

        file.add_command(label="Delete All", command=self.deleteAllSelectData)  #

        file.add_command(label="Exit", command=self.user_exit)
        menu.add_cascade(label="File", menu=file)  #add_cascade is a bunch of options like when you click file(top-left)

        edit = Menu(menu)
        edit.add_command(label="Show Image", command=self.showImg)  # activates showImg function
        edit.add_command(label="Show Text", command=self.showTxt)  # activates showTxt function
        menu.add_cascade(label="Edit", menu=edit)  # adds to top of program

    def deleteAllSelectData(self):
        toplevel = Toplevel()
        label1 = Label(toplevel, text=NOT_GONNA_HAPPEN, height=0, width=20, font=("Arial Bold", 20))
        label1.pack()

    def deleteSelectData(self, Purchisie):
        sqlDatabaseForRetail.delete_saved_data(Purchisie)

    def updatePerviousData(self, Purchister, amount):
        sqlDatabaseForRetail.update_search_data(Purchister, amount)

    def loadSelectData(self, Purchisie):
        sqlDatabaseForRetail.get_saved_data(Purchisie)

    def loadAllData(self):
        sqlDatabaseForRetail.select_all()

    def saveData(self, Purchister, amount):
        sqlDatabaseForRetail.save_search_data(Purchister, amount)

    def buyPounds(totalLabel,  potatoPurchase):
        try:
            #numberOfPoundsInt = tk.StringVar(potatoPurchase)
            totalCost = float(potatoPurchase) * 0.73
            totalLabel.configure(text="Total Cost is %f" % totalCost)
        except ValueError as ve:
            print(ve)

    def showImg(self):
        load = Image.open('potatoImage.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        #img.place(x=0, y=0)
        img.grid(column=99, row=59)

    def showTxt(self):

        text = Label(self, text="Hey sexy tater tot")
        #text.pack()
        text.grid(column=1, row=5)

    def user_exit(self):
        exit(0)


root = Tk()
root.geometry("600x600")  # size of window
root.configure(background="powder blue")  # set background color here

app = Window(root)

root.mainloop()

