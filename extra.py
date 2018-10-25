
import tkinter as tk
from tkinter import *


window = tk.Tk()  # create instance
window.title("Retail GUI")  # title for gui
window.configure(background="black")

potato_photo = PhotoImage("potatoImage.jpg")
Label(window, image=potato_photo, bg="white").grid(row=0, column=0, sticky=E)

window.mainloop()  # loop that runs forever till closed


