


# https://www.youtube.com/watch?v=A0gaXfM1UN0
#                  \/ inherited from another class
class SeaOfBTCapp(tk.Tk):
    # def = method, __init__ = initialize, (self) = first parameter of any method
    def __init__(self, *args, **kwargs): # *args = as many arguments as you want. kwargs = dictionaries

        tk.Tk.__init__(self, *args, **kwargs) # initializing
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # equals an empty dictionary

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")  # nsew is North, South, East, West

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)  # pady, padx means padding on the top and bottom


app = SeaOfBTCapp()
app.mainloop()

