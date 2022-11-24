
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from matplotlib.pyplot import bar
from pyparsing import line
import tkintermapview
import pandas as pd
import matplotlib.pyplot as plt
from csv import writer
       
root1 = Tk()
root1.title= "Krishn E-Grocery"
root1.geometry("1366x768")
img = ImageTk.PhotoImage(Image.open("./content/CXm5S7.png"))
imggc = ImageTk.PhotoImage(Image.open("./content/gc.png"))
my_Canvas = Canvas(root1, width=1366, height = 768)
my_Canvas.pack(fill="both", expand=True)
my_Canvas.create_image(0, 0, image=img, anchor="nw")
df1 = pd.read_csv("./storage/data.csv", sep=",")[["Name","NumberOfItems"]]
df2 = pd.read_csv("./storage/data.csv", sep=",")[["Name","TotalSales"]]
def plot():
    global e
    global e1
    un = "jphs123"
    ps = "54321"
    if(un == e.get() and ps == e1.get()):
        my_Canvas.delete('all')
        my_Canvas.create_image(0, 0, image=img, anchor="nw")

        df1.plot(kind="line")
        df2.plot(kind="bar")
        plt.show()
    else:
        tk.messagebox.showinfo("Error", "Enter correct username or password")
        mainn()

  

def mainn():
    global e
    global e1
    my_Canvas.create_text(974, 142.2, text="Data Visualiser", font="Arial 40 bold" )
    e = Entry(root1, justify=CENTER, font="Arial 20")
    e.insert(0, "Enter username")
    e_window = my_Canvas.create_window(831.87, 284.4, anchor="nw", window=e)
    e1 = Entry(root1, justify=CENTER, font="Arial 20")
    e1.insert(0, "password")
    e1_window = my_Canvas.create_window(831.87, 355.5, anchor="nw", window=e1)
    b1 = Button(root1, text="Proceed" ,font="Arial 10 bold", command = plot)
    l1 = Label(root1, image=imggc)
    l1_window = my_Canvas.create_window(0, 384, anchor="w", window=l1)
    b1_window = my_Canvas.create_window(935,426.6, anchor="nw", window=b1)
    my_Canvas.create_text(782.1, 639.9, text="Ph.No. : +91 900010000", font="Calibri 20 bold")
    my_Canvas.create_text(782.1, 675.45, text="Email : admin@krishnstore.com", font="Calibri 20 bold")
    root1.attributes('-fullscreen', True)




mainn()
mainloop()

