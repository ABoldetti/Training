import customtkinter as ctk


class App( ctk.CTk ):
    def __init__( self ):
        super().__init__()
        self.geometry("700x400+50+200")
        self.title ("Prova")
        self.configure( fg_color = "darkgrey")
        self.resizable( width=True , height=True)

        self.button = ctk.CTkButton( self , command=self.button )
        self.button.grid  ( row = 0 , column = 0 , padx = 20 , pady= 40)
        pass
    
    def button( self ):
        print( "Prova" )

app = App()
app.mainloop()