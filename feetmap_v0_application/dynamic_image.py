from tkinter import *
from PIL import Image, ImageTk

window = Tk()

#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.title("test")

bg = ImageTk.PhotoImage(file="images/feet.png")
my_canvas = Canvas(window,width=width,height=height)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image=bg,anchor=NW)

# def resizer(e):
#     global bg1, resized_bg, new_bg
#     bg1 = Image.open("images/feet.png")
#     resized_bg = bg1.resize((e.width,e.height),Image.ANTIALIAS)
#     new_bg = ImageTk.PhotoImage(resized_bg)
#     my_canvas.create_image(0,0,image=new_bg,anchor=NE)



# window.bind("<Configure>",resizer)
window.resizable(False,False)
window.mainloop()