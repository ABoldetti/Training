from customtkinter import *

class Root (CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x800")
        self.title("Mainpage")
        mainpage = Mainpage( self )

class Mainpage ( Root ):
    def __init__( self , master ):
        super().__init__()
        

root = Root()
root.mainloop()