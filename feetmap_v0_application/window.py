from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class SetupWindow():
    def __init__(self):
        self.window = Tk()

        self.width= self.window.winfo_screenwidth()   #1280
        self.height= self.window.winfo_screenheight() #720

        # width= 800
        # height= 450

        self.ingnore_update = False
        self.mode = 0

        self.menu_width = int(self.width*0.2)
        self.menu_height = int(self.height*0.9)
        self.menu = Frame(self.window, width=self.menu_width, height=self.menu_height,bg="#abb3b0")
        self.menu.pack(fill=BOTH,anchor=NW,side=LEFT)

        self.window.geometry("%dx%d" % (self.width, self.height))
        self.window.title("Feetmap")

        px = 20
        py = 20
        self.but0 = Button(self.menu, text ="mode0", command = self.Mode0,bg="#06b025")
        self.but0.pack(anchor=W,padx=px,pady=py)
        
        self.but1 = Button(self.menu, text ="mode1", command = self.Mode1,bg="#ffffff")
        self.but1.pack(anchor=W,padx=px,pady=py)
        
        self.but2 = Button(self.menu, text ="mode2", command = self.Mode2,bg="#ffffff")
        self.but2.pack(anchor=W,padx=px,pady=py)
        
        self.but3 = Button(self.menu, text ="mode3", command = self.Mode3,bg="#ffffff")
        self.but3.pack(anchor=W,padx=px,pady=py)

        self.Set_up0()
        


    #setting tkinter window size


    def Mode0(self):
        self.but0.config(bg="#06b025")
        self.but1.config(bg="#ffffff")
        self.but2.config(bg="#ffffff")
        self.but3.config(bg="#ffffff")
        self.ingnore_update = True
        self.mode = 0
        self.foot_frame.destroy()
        self.Set_up0()
        self.ingnore_update = False
    
    def Mode1(self):
        self.but0.config(bg="#ffffff")
        self.but1.config(bg="#06b025")
        self.but2.config(bg="#ffffff")
        self.but3.config(bg="#ffffff")
        self.ingnore_update = True
        self.mode = 1
        self.foot_frame.destroy()
        self.Set_up1()
        self.ingnore_update = False
    
    def Mode2(self):
        self.but0.config(bg="#ffffff")
        self.but1.config(bg="#ffffff")
        self.but2.config(bg="#06b025")
        self.but3.config(bg="#ffffff")
        self.ingnore_update = True
        self.mode = 2
        self.foot_frame.destroy()
        self.Set_up2()
        self.ingnore_update = False
        
    def Mode3(self):
        self.but0.config(bg="#ffffff")
        self.but1.config(bg="#ffffff")
        self.but2.config(bg="#ffffff")
        self.but3.config(bg="#06b025")
        self.ingnore_update = True
        self.mode = 3
        self.foot_frame.destroy()
        self.Set_up3()
        self.ingnore_update = False

    def View(self):
        print("profile view")

    def Set_up0(self):
        self.foot_frame_width = int(self.width*0.8)
        self.foot_frame_height = int(self.height*0.9)
        self.foot_frame  = Frame(self.window, width=self.foot_frame_width, height=self.foot_frame_height)
        self.foot_frame.pack(anchor=SE)

        self.canvas= Canvas(self.foot_frame, width= self.foot_frame_width, height= self.foot_frame_height)
        self.canvas.pack()

        self.image = Image.open("images/mode0.png")
        self.resized_image = self.image.resize((int(self.foot_frame_width*0.8),int(self.foot_frame_height*0.8)),Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(int(self.foot_frame_width*0.15),0,anchor=NW,image=self.new_image)

        text_size =30
        clear ="#FFFFFF"

        self.lbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.lbar.place(x=int(self.foot_frame_width*0.1),y=0)
        
        self.rbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.rbar.place(x=int(self.foot_frame_width*0.925),y=0)

        self.v1 = StringVar()
        self.v1.set("0")
        self.b1 = Label(self.foot_frame, textvariable=self.v1)
        self.b1.config(font =("Courier", text_size)) 
        self.b1.place(x=int(self.foot_frame_width*0.08),y=int(self.foot_frame_height*0.38))

        self.v2 = StringVar()
        self.v2.set("0")
        self.b2 = Label(self.foot_frame, textvariable=self.v2)
        self.b2.config(font =("Courier", text_size)) 
        self.b2.place(x=int(self.foot_frame_width*0.91),y=int(self.foot_frame_height*0.38))

        self.vl1 = StringVar()
        self.vl1.set("0")
        self.l1 = Label(self.foot_frame, textvariable=self.vl1)
        self.l1.config(font =("Courier", text_size)) 
        self.l1.place(x=int(self.foot_frame_width*0.22),y=int(self.foot_frame_height*0.1))

        self.vl2 = StringVar()
        self.vl2.set("0")
        self.l2 = Label(self.foot_frame, textvariable=self.vl2)
        self.l2.config(font =("Courier", text_size)) 
        self.l2.place(x=int(self.foot_frame_width*0.35),y=int(self.foot_frame_height*0.1))

        self.vl3 = StringVar()
        self.vl3.set("0")
        self.l3 = Label(self.foot_frame, textvariable=self.vl3)
        self.l3.config(font =("Courier", text_size)) 
        self.l3.place(x=int(self.foot_frame_width*0.26),y=int(self.foot_frame_height*0.37))

        self.vl4 = StringVar()
        self.vl4.set("0")
        self.l4 = Label(self.foot_frame, textvariable=self.vl4)
        self.l4.config(font =("Courier", text_size)) 
        self.l4.place(x=int(self.foot_frame_width*0.27),y=int(self.foot_frame_height*0.62))

        self.vl5 = StringVar()
        self.vl5.set("0")
        self.l5 = Label(self.foot_frame,textvariable=self.vl5)
        self.l5.config(font =("Courier", text_size)) 
        self.l5.place(x=int(self.foot_frame_width*0.38),y=int(self.foot_frame_height*0.62))

        self.vr1 = StringVar()
        self.vr1.set("0")
        self.r1 = Label(self.foot_frame, textvariable=self.vr1)
        self.r1.config(font =("Courier", text_size)) 
        self.r1.place(x=int(self.foot_frame_width*0.63),y=int(self.foot_frame_height*0.1))

        self.vr2 = StringVar()
        self.vr2.set("0")
        self.r2 = Label(self.foot_frame, textvariable=self.vr2)
        self.r2.config(font =("Courier", text_size)) 
        self.r2.place(x=int(self.foot_frame_width*0.76),y=int(self.foot_frame_height*0.1))

        self.vr3 = StringVar()
        self.vr3.set("0")
        self.r3 = Label(self.foot_frame, textvariable=self.vr3)
        self.r3.config(font =("Courier", text_size)) 
        self.r3.place(x=int(self.foot_frame_width*0.74),y=int(self.foot_frame_height*0.37))

        self.vr4 = StringVar()
        self.vr4.set("0")
        self.r4 = Label(self.foot_frame, textvariable=self.vr4)
        self.r4.config(font =("Courier", text_size)) 
        self.r4.place(x=int(self.foot_frame_width*0.62),y=int(self.foot_frame_height*0.62))

        self.vr5 = StringVar()
        self.vr5.set("0")
        self.r5 = Label(self.foot_frame,textvariable=self.vr5)
        self.r5.config(font =("Courier", text_size)) 
        self.r5.place(x=int(self.foot_frame_width*0.73),y=int(self.foot_frame_height*0.62))

    def Set_up1(self):
        self.foot_frame_width = int(self.width*0.8)
        self.foot_frame_height = int(self.height*0.9)
        self.foot_frame  = Frame(self.window, width=self.foot_frame_width, height=self.foot_frame_height)
        self.foot_frame.pack(anchor=SE)

        self.canvas= Canvas(self.foot_frame, width= self.foot_frame_width, height= self.foot_frame_height)
        self.canvas.pack()

        self.image = Image.open("images/mode1.png")
        self.resized_image = self.image.resize((int(self.foot_frame_width*0.8),int(self.foot_frame_height*0.8)),Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(int(self.foot_frame_width*0.15),0,anchor=NW,image=self.new_image)

        text_size =30
        clear ="#FFFFFF"

        self.lbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.lbar.place(x=int(self.foot_frame_width*0.1),y=0)
        
        self.rbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.rbar.place(x=int(self.foot_frame_width*0.925),y=0)

        self.v1 = StringVar()
        self.v1.set("0")
        self.b1 = Label(self.foot_frame, textvariable=self.v1)
        self.b1.config(font =("Courier", text_size)) 
        self.b1.place(x=int(self.foot_frame_width*0.08),y=int(self.foot_frame_height*0.38))

        self.v2 = StringVar()
        self.v2.set("0")
        self.b2 = Label(self.foot_frame, textvariable=self.v2)
        self.b2.config(font =("Courier", text_size)) 
        self.b2.place(x=int(self.foot_frame_width*0.91),y=int(self.foot_frame_height*0.38))

        self.vl1 = StringVar()
        self.vl1.set("0")
        self.l1 = Label(self.foot_frame, textvariable=self.vl1)
        self.l1.config(font =("Courier", text_size)) 
        self.l1.place(x=int(self.foot_frame_width*0.3),y=int(self.foot_frame_height*0.1))

        self.vl3 = StringVar()
        self.vl3.set("0")
        self.l3 = Label(self.foot_frame, textvariable=self.vl3)
        self.l3.config(font =("Courier", text_size)) 
        self.l3.place(x=int(self.foot_frame_width*0.26),y=int(self.foot_frame_height*0.37))

        self.vl4 = StringVar()
        self.vl4.set("0")
        self.l4 = Label(self.foot_frame, textvariable=self.vl4)
        self.l4.config(font =("Courier", text_size)) 
        self.l4.place(x=int(self.foot_frame_width*0.3),y=int(self.foot_frame_height*0.62))

        self.vr1 = StringVar()
        self.vr1.set("0")
        self.r1 = Label(self.foot_frame, textvariable=self.vr1)
        self.r1.config(font =("Courier", text_size)) 
        self.r1.place(x=int(self.foot_frame_width*0.7),y=int(self.foot_frame_height*0.1))

        self.vr3 = StringVar()
        self.vr3.set("0")
        self.r3 = Label(self.foot_frame, textvariable=self.vr3)
        self.r3.config(font =("Courier", text_size)) 
        self.r3.place(x=int(self.foot_frame_width*0.74),y=int(self.foot_frame_height*0.37))

        self.vr4 = StringVar()
        self.vr4.set("0")
        self.r4 = Label(self.foot_frame, textvariable=self.vr4)
        self.r4.config(font =("Courier", text_size)) 
        self.r4.place(x=int(self.foot_frame_width*0.7),y=int(self.foot_frame_height*0.62))

    def Set_up2(self):
        self.foot_frame_width = int(self.width*0.8)
        self.foot_frame_height = int(self.height*0.9)
        self.foot_frame  = Frame(self.window, width=self.foot_frame_width, height=self.foot_frame_height)
        self.foot_frame.pack(anchor=SE)

        self.canvas= Canvas(self.foot_frame, width= self.foot_frame_width, height= self.foot_frame_height)
        self.canvas.pack()

        self.image = Image.open("images/mode2.png")
        self.resized_image = self.image.resize((int(self.foot_frame_width*0.8),int(self.foot_frame_height*0.8)),Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(int(self.foot_frame_width*0.15),0,anchor=NW,image=self.new_image)

        text_size =30
        clear ="#FFFFFF"

        self.lbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.lbar.place(x=int(self.foot_frame_width*0.1),y=0)
        
        self.rbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.rbar.place(x=int(self.foot_frame_width*0.925),y=0)

        self.v1 = StringVar()
        self.v1.set("0")
        self.b1 = Label(self.foot_frame, textvariable=self.v1)
        self.b1.config(font =("Courier", text_size)) 
        self.b1.place(x=int(self.foot_frame_width*0.08),y=int(self.foot_frame_height*0.38))

        self.v2 = StringVar()
        self.v2.set("0")
        self.b2 = Label(self.foot_frame, textvariable=self.v2)
        self.b2.config(font =("Courier", text_size)) 
        self.b2.place(x=int(self.foot_frame_width*0.91),y=int(self.foot_frame_height*0.38))

        self.vl1 = StringVar()
        self.vl1.set("0")
        self.l1 = Label(self.foot_frame, textvariable=self.vl1)
        self.l1.config(font =("Courier", text_size)) 
        self.l1.place(x=int(self.foot_frame_width*0.3),y=int(self.foot_frame_height*0.1))

        self.vl4 = StringVar()
        self.vl4.set("0")
        self.l4 = Label(self.foot_frame, textvariable=self.vl4)
        self.l4.config(font =("Courier", text_size)) 
        self.l4.place(x=int(self.foot_frame_width*0.3),y=int(self.foot_frame_height*0.62))

        self.vr1 = StringVar()
        self.vr1.set("0")
        self.r1 = Label(self.foot_frame, textvariable=self.vr1)
        self.r1.config(font =("Courier", text_size)) 
        self.r1.place(x=int(self.foot_frame_width*0.7),y=int(self.foot_frame_height*0.1))

        self.vr4 = StringVar()
        self.vr4.set("0")
        self.r4 = Label(self.foot_frame, textvariable=self.vr4)
        self.r4.config(font =("Courier", text_size)) 
        self.r4.place(x=int(self.foot_frame_width*0.7),y=int(self.foot_frame_height*0.62))

    def Set_up3(self):
        self.foot_frame_width = int(self.width*0.8)
        self.foot_frame_height = int(self.height*0.9)
        self.foot_frame  = Frame(self.window, width=self.foot_frame_width, height=self.foot_frame_height)
        self.foot_frame.pack(anchor=SE)

        self.canvas= Canvas(self.foot_frame, width= self.foot_frame_width, height= self.foot_frame_height)
        self.canvas.pack()

        self.image = Image.open("images/mode3.png")
        self.resized_image = self.image.resize((int(self.foot_frame_width*0.8),int(self.foot_frame_height*0.8)),Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(int(self.foot_frame_width*0.15),0,anchor=NW,image=self.new_image)

        text_size =30
        clear ="#FFFFFF"

        self.lbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.lbar.place(x=int(self.foot_frame_width*0.1),y=0)
        
        self.rbar = ttk.Progressbar(self.foot_frame,orient='vertical',mode='determinate',length=int(self.foot_frame_height*0.8 ))
        self.rbar.place(x=int(self.foot_frame_width*0.925),y=0)

        self.v1 = StringVar()
        self.v1.set("0")
        self.b1 = Label(self.foot_frame, textvariable=self.v1)
        self.b1.config(font =("Courier", text_size)) 
        self.b1.place(x=int(self.foot_frame_width*0.08),y=int(self.foot_frame_height*0.38))

        self.v2 = StringVar()
        self.v2.set("0")
        self.b2 = Label(self.foot_frame, textvariable=self.v2)
        self.b2.config(font =("Courier", text_size)) 
        self.b2.place(x=int(self.foot_frame_width*0.91),y=int(self.foot_frame_height*0.38))

        self.vl1 = StringVar()
        self.vl1.set("0")
        self.l1 = Label(self.foot_frame, textvariable=self.vl1)
        self.l1.config(font =("Courier", text_size)) 
        self.l1.place(x=int(self.foot_frame_width*0.3),y=int(self.foot_frame_height*0.1))

        self.vl4 = StringVar()
        self.vl4.set("0")
        self.l4 = Label(self.foot_frame, textvariable=self.vl4)
        self.l4.config(font =("Courier", text_size)) 
        self.l4.place(x=int(self.foot_frame_width*0.3),y=int(self.foot_frame_height*0.62))

        self.vr1 = StringVar()
        self.vr1.set("0")
        self.r1 = Label(self.foot_frame, textvariable=self.vr1)
        self.r1.config(font =("Courier", text_size)) 
        self.r1.place(x=int(self.foot_frame_width*0.7),y=int(self.foot_frame_height*0.1))

        self.vr4 = StringVar()
        self.vr4.set("0")
        self.r4 = Label(self.foot_frame, textvariable=self.vr4)
        self.r4.config(font =("Courier", text_size)) 
        self.r4.place(x=int(self.foot_frame_width*0.7),y=int(self.foot_frame_height*0.62))



    def UpdateValues(self,data):
        if not(self.ingnore_update):
            if self.mode == 0:
                self.lbar["value"] = data[10]
                self.rbar["value"] = data[11]

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
            elif self.mode == 1:
                data = self.DataMode1(data)
                self.lbar["value"] = data[10]
                self.rbar["value"] = data[11]
                

                self.v1.set(self.AddPercent(data[10]))
                self.v2.set(self.AddPercent(data[11]))

                self.vl1.set(self.AddPercent(data[0]))
                self.vl3.set(self.AddPercent(data[2]))
                self.vl4.set(self.AddPercent(data[3]))
                self.vr1.set(self.AddPercent(data[5]))
                self.vr3.set(self.AddPercent(data[7]))
                self.vr4.set(self.AddPercent(data[8]))
            elif self.mode == 2:
                data = self.DataMode2(data)
                self.lbar["value"] = data[10]
                self.rbar["value"] = data[11]
                

                self.v1.set(self.AddPercent(data[10]))
                self.v2.set(self.AddPercent(data[11]))

                self.vl1.set(self.AddPercent(data[0]))
                self.vl4.set(self.AddPercent(data[2]))
                self.vr1.set(self.AddPercent(data[5]))
                self.vr4.set(self.AddPercent(data[8]))
            elif self.mode == 3:
                data = self.DataMode3(data)
                self.lbar["value"] = data[10]
                self.rbar["value"] = data[11]
                

                self.v1.set(self.AddPercent(data[10]))
                self.v2.set(self.AddPercent(data[11]))

                self.vl1.set(self.AddPercent(data[0]))
                self.vl4.set(self.AddPercent(data[3]))
                self.vr1.set(self.AddPercent(data[5]))
                self.vr4.set(self.AddPercent(data[8]))


    def AddPercent(self,val):
        return str(val) + "%"
    
    def DataMode1(self,data):
        data[0] = data[0]+data[1]
        data[2] = data[2]
        data[3] = data[3]+data[4]
        data[5] = data[5]+data[6]
        data[7] = data[7]
        data[8] = data[8]+data[9]
        return data
    
    def DataMode2(self,data):
        data[0] = data[0]+data[1]+data[2]
        data[3] = data[3]+data[4]
        data[5] = data[5]+data[6]+data[7]
        data[8] = data[8]+data[9]
        return data
    
    def DataMode3(self,data):
        data[0] = data[0]+data[1]
        data[3] = data[3]+data[4]+data[2]
        data[5] = data[5]+data[6]
        data[8] = data[8]+data[9]+data[7]
        return data