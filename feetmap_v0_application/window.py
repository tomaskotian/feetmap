from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class SetupWindow():
    window = Tk()

    width= window.winfo_screenwidth()   #1280
    height= window.winfo_screenheight() #720

    # width= 800
    # height= 450

    #setting tkinter window size
    window.geometry("%dx%d" % (width, height))
    window.title("Feetmap")


    foot_frame_width = int(width*0.8)
    foot_frame_height = int(height*0.9)
    foot_frame  = Frame(window, width=foot_frame_width, height=foot_frame_height)
    foot_frame.pack(anchor=SE)

    canvas= Canvas(foot_frame, width= foot_frame_width, height= foot_frame_height)
    canvas.pack()

    image = Image.open("images/feet.png")
    resized_image = image.resize((int(foot_frame_width*0.8),int(foot_frame_height*0.8)),Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(foot_frame_width*0.15),0,anchor=NW,image=new_image)

    text_size =30
    clear ="#FFFFFF"

    lbar = ttk.Progressbar(foot_frame,orient='vertical',mode='determinate',length=int(foot_frame_height*0.8 ))
    lbar.place(x=int(foot_frame_width*0.1),y=0)
    
    rbar = ttk.Progressbar(foot_frame,orient='vertical',mode='determinate',length=int(foot_frame_height*0.8 ))
    rbar.place(x=int(foot_frame_width*0.925),y=0)

    v1 = StringVar()
    v1.set("0")
    b1 = Label(foot_frame, textvariable=v1)
    b1.config(font =("Courier", text_size)) 
    b1.place(x=int(foot_frame_width*0.08),y=int(foot_frame_height*0.38))

    
    v2 = StringVar()
    v2.set("0")
    b2 = Label(foot_frame, textvariable=v2)
    b2.config(font =("Courier", text_size)) 
    b2.place(x=int(foot_frame_width*0.91),y=int(foot_frame_height*0.38))



    vl1 = StringVar()
    vl1.set("0")
    l1 = Label(foot_frame, textvariable=vl1)
    l1.config(font =("Courier", text_size)) 
    l1.place(x=int(foot_frame_width*0.22),y=int(foot_frame_height*0.1))

    vl2 = StringVar()
    vl2.set("0")
    l2 = Label(foot_frame, textvariable=vl2)
    l2.config(font =("Courier", text_size)) 
    l2.place(x=int(foot_frame_width*0.35),y=int(foot_frame_height*0.1))

    vl3 = StringVar()
    vl3.set("0")
    l3 = Label(foot_frame, textvariable=vl3)
    l3.config(font =("Courier", text_size)) 
    l3.place(x=int(foot_frame_width*0.26),y=int(foot_frame_height*0.37))

    vl4 = StringVar()
    vl4.set("0")
    l4 = Label(foot_frame, textvariable=vl4)
    l4.config(font =("Courier", text_size)) 
    l4.place(x=int(foot_frame_width*0.27),y=int(foot_frame_height*0.62))

    vl5 = StringVar()
    vl5.set("0")
    l5 = Label(foot_frame,textvariable=vl5)
    l5.config(font =("Courier", text_size)) 
    l5.place(x=int(foot_frame_width*0.38),y=int(foot_frame_height*0.62))

    vr1 = StringVar()
    vr1.set("0")
    r1 = Label(foot_frame, textvariable=vr1)
    r1.config(font =("Courier", text_size)) 
    r1.place(x=int(foot_frame_width*0.63),y=int(foot_frame_height*0.1))

    vr2 = StringVar()
    vr2.set("0")
    r2 = Label(foot_frame, textvariable=vr2)
    r2.config(font =("Courier", text_size)) 
    r2.place(x=int(foot_frame_width*0.76),y=int(foot_frame_height*0.1))

    vr3 = StringVar()
    vr3.set("0")
    r3 = Label(foot_frame, textvariable=vr3)
    r3.config(font =("Courier", text_size)) 
    r3.place(x=int(foot_frame_width*0.74),y=int(foot_frame_height*0.37))

    vr4 = StringVar()
    vr4.set("0")
    r4 = Label(foot_frame, textvariable=vr4)
    r4.config(font =("Courier", text_size)) 
    r4.place(x=int(foot_frame_width*0.62),y=int(foot_frame_height*0.62))

    vr5 = StringVar()
    vr5.set("0")
    r5 = Label(foot_frame,textvariable=vr5)
    r5.config(font =("Courier", text_size)) 
    r5.place(x=int(foot_frame_width*0.73),y=int(foot_frame_height*0.62))

    def UpdateValues(self,data):
        self.rbar["value"] = data[11]
        self.lbar["value"] = data[10]

        self.v1.set(self.AddPercent(data[10]))
        self.v2.set(self.AddPercent(data[11]))

        self.vl1.set(self.AddPercent(data[0]))
        self.vl2.set(self.AddPercent(data[1]))
        self.vl3.set(self.AddPercent(data[2]))
        self.vl4.set(self.AddPercent(data[3]))
        self.vl5.set(self.AddPercent(data[4]))
        self.vr1.set(self.AddPercent(data[5]))
        self.vr2.set(self.AddPercent(data[6]))
        self.vr3.set(self.AddPercent(data[7]))
        self.vr4.set(self.AddPercent(data[8]))
        self.vr5.set(self.AddPercent(data[9]))

    def AddPercent(self,val):
        return str(val) + "%"