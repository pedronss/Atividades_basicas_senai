import tkinter as tk
import tkinter.font as tkfont
janela2= tk.Tk()
janela2.geometry ("250x210")
fontsz= tkfont.Font(size=15)
bv= tk.Label (janela2,  foreground="Green", text="Bem vindo!", font=fontsz)
bv.place(x=65,y=80)
janela2.mainloop()
