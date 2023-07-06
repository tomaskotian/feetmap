import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SetupWindow():
    window = tk.Tk()
    #getting screen width and height of display
    width= window.winfo_screenwidth()
    height= window.winfo_screenheight()
    #setting tkinter window size
    window.geometry("%dx%d" % (width, height))
    window.title("Feetmap")


    main_frame  =  tk.Frame(window, width=width, height= height, bg="#FFFFFF")
    main_frame.pack(fill="both",expand=True)
    # Specify Grid
    tk.Grid.rowconfigure(main_frame,0,weight=1)
    tk.Grid.rowconfigure(main_frame,1,weight=1)
    tk.Grid.rowconfigure(main_frame,2,weight=1)
    tk.Grid.rowconfigure(main_frame,3,weight=1)

    tk.Grid.columnconfigure(main_frame,0,weight=1)
    tk.Grid.columnconfigure(main_frame,1,weight=1)
    tk.Grid.columnconfigure(main_frame,2,weight=1)
    tk.Grid.columnconfigure(main_frame,3,weight=1)
    tk.Grid.columnconfigure(main_frame,4,weight=1)
    tk.Grid.columnconfigure(main_frame,5,weight=1)
    tk.Grid.columnconfigure(main_frame,6,weight=1)

    text_size =30
    clear ="#FFFFFF"

    lbar = ttk.Progressbar(main_frame,orient='vertical',mode='determinate',length=400)
    lbar.grid(row=0,column=1,rowspan=3)
    
    rbar = ttk.Progressbar(main_frame,orient='vertical',mode='determinate',length=400)
    rbar.grid(row=0,column=4,rowspan=3)

    v1 = tk.StringVar()
    v1.set("0")
    b1 = tk.Label(main_frame, textvariable=v1,bg=clear)
    b1.config(font =("Courier", text_size)) 
    b1.grid(row=0,column=1,rowspan=3)
    
    v2 = tk.StringVar()
    v2.set("0")
    b2 = tk.Label(main_frame, textvariable=v2,bg=clear)
    b2.config(font =("Courier", text_size),bg=clear) 
    b2.grid(row=0,column=4,rowspan=3)


    vl1 = tk.StringVar()
    vl1.set("0")
    l1 = tk.Label(main_frame, textvariable=vl1,bg=clear)
    l1.config(font =("Courier", text_size),bg=clear) 
    l1.grid(row=0,column=2)

    vl2 = tk.StringVar()
    vl2.set("0")
    l2 = tk.Label(main_frame, textvariable=vl2,bg=clear)
    l2.config(font =("Courier", text_size),bg=clear) 
    l2.grid(row=0,column=3)

    vl3 = tk.StringVar()
    vl3.set("0")
    l3 = tk.Label(main_frame, textvariable=vl3,bg=clear)
    l3.config(font =("Courier", text_size),bg=clear) 
    l3.grid(row=1,column=2,columnspan=2)

    vl4 = tk.StringVar()
    vl4.set("0")
    l4 = tk.Label(main_frame, textvariable=vl4,bg=clear)
    l4.config(font =("Courier", text_size),bg=clear) 
    l4.grid(row=2,column=2)

    vl5 = tk.StringVar()
    vl5.set("0")
    l5 = tk.Label(main_frame,textvariable=vl5,bg=clear)
    l5.config(font =("Courier", text_size),bg=clear) 
    l5.grid(row=2,column=3)

    vr1 = tk.StringVar()
    vr1.set("0")
    r1 = tk.Label(main_frame, textvariable=vr1,bg=clear)
    r1.config(font =("Courier", text_size),bg=clear) 
    r1.grid(row=0,column=5)

    vr2 = tk.StringVar()
    vr2.set("0")
    r2 = tk.Label(main_frame, textvariable=vr2,bg=clear)
    r2.config(font =("Courier", text_size),bg=clear) 
    r2.grid(row=0,column=6)

    vr3 = tk.StringVar()
    vr3.set("0")
    r3 = tk.Label(main_frame, textvariable=vr3,bg=clear)
    r3.config(font =("Courier", text_size),bg=clear) 
    r3.grid(row=1,column=5,columnspan=2)

    vr4 = tk.StringVar()
    vr4.set("0")
    r4 = tk.Label(main_frame, textvariable=vr4,bg=clear)
    r4.config(font =("Courier", text_size),bg=clear) 
    r4.grid(row=2,column=5)

    vr5 = tk.StringVar()
    vr5.set("0")
    r5 = tk.Label(main_frame,textvariable=vr5,bg=clear)
    r5.config(font =("Courier", text_size),bg=clear) 
    r5.grid(row=2,column=6)

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