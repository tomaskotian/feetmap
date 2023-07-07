from tkinter import *
from PIL import Image, ImageTk

window = Tk()

width= window.winfo_screenwidth()   #1280
height= window.winfo_screenheight() #720

# width= 800
# height= 450

window.geometry("%dx%d" % (width, height))
window.title("test")

foot_frame_width = int(width*0.8)
foot_frame_height = int(height*0.9)
foot_frame  = Frame(window, width=foot_frame_width, height=foot_frame_height)
foot_frame.pack(anchor=SE)

canvas= Canvas(foot_frame, width= foot_frame_width, height= foot_frame_height)
canvas.pack()

image = Image.open("images/feet.png")
resized_image = image.resize((foot_frame_width,foot_frame_height),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0,anchor=NW,image=new_image)

window.resizable(False,False)
window.mainloop()