import tkinter as tk

class SetupWindow():
    window = tk.Tk()
    #getting screen width and height of display
    width= window.winfo_screenwidth()
    height= window.winfo_screenheight()
    #setting tkinter window size
    window.geometry("%dx%d" % (width, height))
    window.title("Feetmap")