
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import tkintermapview
import pandas as pd
from csv import writer  
import os        
root = Tk()
root.title= "Krishn E-Grocery"
root.geometry("1366x768")
img = ImageTk.PhotoImage(Image.open("./content/CXm5S7.png"))
imggc = ImageTk.PhotoImage(Image.open("./content/gc.png"))
my_Canvas = Canvas(root, width=1366, height = 768)
my_Canvas.pack(fill="both", expand=True)
my_Canvas.create_image(0, 0, image=img, anchor="nw")

item_list={
        "h1":["Gloves", 50, 0 , 0],
        "h2":["Masks", 100, 0 , 0],
        "h3":["toothpaste", 40, 0 , 0],
        "h4":["Soap", 50, 0 , 0],
        "h5":["Detergent", 200, 0 , 0],
        "h6":["Shampoo", 120, 0 , 0],
        "f1":["Pasta", 80, 0 , 0],
        "f2":["Kurkure", 20, 0 , 0],
        "f3":["Lays", 20, 0 , 0],
        "f4":["Nuts", 50, 0 , 0],
        "f5":["Popcorn", 30, 0 , 0],
        "f6":["Maggi", 55, 0 , 0],
        "s1":["Notebook", 90, 0 , 0],
        "s2":["Pen-Packet", 100, 0 , 0],
        "s3":["Pencil-Packet", 30, 0 , 0],
        "s4":["box", 30, 0 , 0],
        "s5":["Marker", 25, 0 , 0],
        "s6":["Highlighter", 20, 0 , 0],

    }


def switch1():
    
    global img
    global e
    global varch1 
    global varch2 
    global varch3 
    global varch4 
    global varch5
    global varch6 
    global varcf1 
    global varcf2 
    global varcf3 
    global varcf4 
    global varcf5 
    global varcf6 
    global varcs1 
    global varcs2 
    global varcs3 
    global varcs4 
    global varcs5 
    global varcs6 
    global varsch1 
    global varsch2 
    global varsch3 
    global varsch4 
    global varsch5 
    global varsch6 
    global varscf1 
    global varscf2 
    global varscf3 
    global varscf4
    global varscf5 
    global varscf6 
    global varscs1 
    global varscs2
    global varscs3
    global varscs4 
    global varscs5 
    global varscs6 
    
    global name


    

    name = e.get()
    my_Canvas.delete('all')
    my_Canvas.create_image(0, 0, image=img, anchor="nw")
    my_Canvas.create_text(682, 71, text="Hi, "+ name, font="Arial 50 bold" )
    my_Canvas.create_text(682, 142, text="Please add items to your shopping cart", font="Arial 30" )
    my_Canvas.create_text(227, 199, text="Home", font="	Calibri 40 bold", fill="white" )
    my_Canvas.create_text(696, 199, text="Food", font="	Calibri 40 bold", fill="white" )
    my_Canvas.create_text(1151, 199, text="Stationary", font="	Calibri 40 bold", fill="white" )
    
    my_Canvas.create_text(71, 266, text="Gloves", font="Arial 28 bold", fill="#fcffa4")
    varch1 = IntVar()
    
    c = Checkbutton(root, text="", variable=varch1)
    c_window = my_Canvas.create_window(227, 255, anchor="nw", window=c)
    varsch1 = IntVar()
    sc = Scale( root, variable = varsch1,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(270, 252, anchor="nw", window=sc)
    
    my_Canvas.create_text(71, 319, text="Masks", font="Arial 28 bold", fill="#fcffa4")
    varch2 = IntVar()
    c = Checkbutton(root, text="", variable=varch2)
    c_window = my_Canvas.create_window(227, 312, anchor="nw", window=c)
    varsch2 = IntVar()
    sc = Scale( root, variable = varsch2,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(270, 305, anchor="nw", window=sc)

    my_Canvas.create_text(110, 376, text="ToothPaste", font="Arial 28 bold", fill="#fcffa4")
    varch3 = IntVar()
    c = Checkbutton(root, text="", variable=varch3)
    c_window = my_Canvas.create_window(227, 369, anchor="nw", window=c)
    varsch3 = IntVar()
    sc = Scale( root, variable = varsch3,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(270, 366, anchor="nw", window=sc)
    
    my_Canvas.create_text(71, 433, text="Soap", font="Arial 28 bold", fill="#fcffa4")
    varch4 = IntVar()
    c = Checkbutton(root, text="", variable=varch4)
    c_window = my_Canvas.create_window(227, 426, anchor="nw", window=c)
    varsch4 = IntVar()
    sc = Scale( root, variable = varsch4,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(270, 419, anchor="nw", window=sc)
   
    my_Canvas.create_text(100, 494, text="Detergent", font="Arial 28 bold", fill="#fcffa4")
    varch5 = IntVar()
    c = Checkbutton(root, text="", variable=varch5)
    c_window = my_Canvas.create_window( 227,483, anchor="nw", window=c)
    varsch5 = IntVar()
    sc = Scale( root, variable = varsch5,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(270, 476, anchor="nw", window=sc)
    
    my_Canvas.create_text(100, 551, text="Shampoo", font="Arial 28 bold", fill="#fcffa4")
    varch6 = IntVar()
    c = Checkbutton(root, text="", variable=varch6)
    c_window = my_Canvas.create_window(227,540, anchor="nw", window=c)
    varsch6 = IntVar()
    sc = Scale( root, variable = varsch6,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(270,533, anchor="nw", window=sc)




    #Food





    my_Canvas.create_text(526, 266.6, text="Pasta", font="Arial 28 bold", fill="#fcffa4")
    varcf1=IntVar()
    c = Checkbutton(root, text="", variable=varcf1)
    c_window = my_Canvas.create_window(682.5, 256, anchor="nw", window=c)
    varscf1 = IntVar()
    sc = Scale( root, variable = varscf1,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(725.25, 252.4, anchor="nw", window=sc)
    
    my_Canvas.create_text(526, 320, text="Kurkure", font="Arial 28 bold", fill="#fcffa4")
    varcf2 = IntVar()
    c = Checkbutton(root, text="", variable=varcf2)
    c_window = my_Canvas.create_window(682.5, 312.85, anchor="nw", window=c)
    varscf2 = IntVar()
    sc = Scale( root, variable = varscf2,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(725.22, 305.75, anchor="nw", window=sc)

    my_Canvas.create_text(526.14, 376.83, text="Lays", font="Arial 28 bold", fill="#fcffa4")
    varcf3 = IntVar()
    c = Checkbutton(root, text="", variable=varcf3)
    c_window = my_Canvas.create_window(682.56, 369.72, anchor="nw", window=c)
    varscf3 = IntVar()
    sc = Scale( root, variable = varscf3,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(725.22, 366.165, anchor="nw", window=sc)
    
    my_Canvas.create_text(526.14, 433.71, text="Nuts", font="Arial 28 bold", fill="#fcffa4")
    varcf4 = IntVar()
    c = Checkbutton(root, text="", variable=varcf4)
    c_window = my_Canvas.create_window(682.56, 426.6, anchor="nw", window=c)
    varscf4 = IntVar()
    sc = Scale( root, variable = varscf4,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(725.22, 419.49, anchor="nw", window=sc)
    
    my_Canvas.create_text(526.14, 494.145, text="Popcorn", font="Arial 28 bold", fill="#fcffa4")
    varcf5 = IntVar()
    c = Checkbutton(root, text="", variable=varcf5)
    c_window = my_Canvas.create_window(682.56, 483.48, anchor="nw", window=c)
    varscf5 = IntVar()
    sc = Scale( root, variable = varscf5,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(725.22, 476.37, anchor="nw", window=sc)
    
    my_Canvas.create_text(526.14, 551, text="Maggi", font="Arial 28 bold", fill="#fcffa4")
    varcf6 = IntVar()
    c = Checkbutton(root, text="", variable=varcf6)
    c_window = my_Canvas.create_window(682.56, 540.36, anchor="nw", window=c)
    varscf6 = IntVar()
    sc = Scale( root, variable = varscf6,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(725.22, 533.25, anchor="nw", window=sc)
    
    
    





    #Stationary

    my_Canvas.create_text(1024, 267, text="Notebook", font="Arial 28 bold", fill="#fcffa4")
    varcs1 = IntVar()
    c = Checkbutton(root, text="", variable=varcs1)
    c_window = my_Canvas.create_window(1159, 256, anchor="nw", window=c)
    varscs1 = IntVar()
    sc = Scale( root, variable = varscs1,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(1223, 252, anchor="nw", window=sc)
    
    my_Canvas.create_text(1024, 320, text="Pen-Pack", font="Arial 28 bold", fill="#fcffa4")
    varcs2 = IntVar()
    c = Checkbutton(root, text="", variable=varcs2)
    c_window = my_Canvas.create_window(1159, 313, anchor="nw", window=c)
    varscs2 = IntVar()
    sc = Scale( root, variable = varscs2,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(1223, 306, anchor="nw", window=sc)

    my_Canvas.create_text(1024, 377, text="Pencil-Pack", font="Arial 28 bold", fill="#fcffa4")
    varcs3 = IntVar()
    c = Checkbutton(root, text="", variable=varcs3)
    c_window = my_Canvas.create_window(1159, 370,anchor="nw", window=c)
    varscs3 = IntVar()
    sc = Scale( root, variable = varscs3,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(1223, 366, anchor="nw", window=sc)
    
    my_Canvas.create_text(1024, 434, text="Box", font="Arial 28 bold", fill="#fcffa4")
    varcs4 = IntVar()
    c = Checkbutton(root, text="", variable=varcs4)
    c_window = my_Canvas.create_window(1159, 427, anchor="nw", window=c)
    varscs4 = IntVar()
    sc = Scale( root, variable = varscs4,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(1223, 419, anchor="nw", window=sc)
    
    my_Canvas.create_text(1024, 494, text="Marker", font="Arial 28 bold", fill="#fcffa4")
    varcs5 = IntVar()
    c = Checkbutton(root, text="", variable=varcs5)
    c_window = my_Canvas.create_window(1159, 483, anchor="nw", window=c)
    varscs5 = IntVar()
    sc = Scale( root, variable = varscs5,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(1223, 476, anchor="nw", window=sc)
    
    my_Canvas.create_text(1024, 551, text="Highlighter", font="Arial 28 bold", fill="#fcffa4")
    varcs6 = IntVar()
    c = Checkbutton(root, text="", variable=varcs6)
    c_window = my_Canvas.create_window(1159, 540, anchor="nw", window=c)
    varscs6 = IntVar()
    sc = Scale( root, variable = varscs6,  from_ = 1, to = 20,  orient = HORIZONTAL)
    sc_window = my_Canvas.create_window(1223, 533, anchor="nw", window=sc)
    



    pr2 = Button(root, text="Proceed", font="Arial 20 bold", command=p2)
    pr2_window = my_Canvas.create_window(640,640, anchor="nw", window = pr2)

    w2 = Toplevel()
    w2.title("Product Information")
    w2.geometry("250x500")


def switch3():

    ln1=[]
    for i in range(0,3):
        if(i == 0):
            ln1.append(name)
        if(i==1):
            ln1.append(count)
        if(i==2):
            ln1.append(sum)

    print(ln1)
    with open('./storage/data.csv', 'a', newline='') as f_object: 
        writer_object = writer(f_object)
        writer_object.writerow(ln1)  
        f_object.close()
    my_Canvas.delete('all')
    my_Canvas.create_image(0, 0, image=img, anchor="nw")
    my_Canvas.create_text(683,355.5, text="HURRAY! YOUR ORDER HAS BEEN PLACED", font="Calibri 40 bold", fill="white")
    pr33 = Button(root, text="Close this window", font="Arial 20 bold", command=root.destroy)
    pr33_window = my_Canvas.create_window(533.25,640, anchor="nw", window = pr33)

    

def p2():
    item_list["h1"][2]=varch1.get()
    item_list["h1"][3]=varsch1.get()
    item_list["h2"][2]=varch2.get()
    item_list["h2"][3]=varsch2.get()
    item_list["h3"][2]=varch3.get()
    item_list["h3"][3]=varsch3.get()
    item_list["h4"][2]=varch4.get()
    item_list["h4"][3]=varsch4.get()
    item_list["h5"][2]=varch5.get()
    item_list["h5"][3]=varsch5.get()
    item_list["h6"][2]=varch6.get()
    item_list["h6"][3]=varsch6.get()


    item_list["f1"][2]=varcf1.get()
    item_list["f1"][3]=varscf1.get()
    item_list["f2"][2]=varcf2.get()
    item_list["f2"][3]=varscf2.get()
    item_list["f3"][2]=varcf3.get()
    item_list["f3"][3]=varscf3.get()
    item_list["f4"][2]=varcf4.get()
    item_list["f4"][3]=varscf4.get()
    item_list["f5"][2]=varcf5.get()
    item_list["f5"][3]=varscf5.get()
    item_list["f6"][2]=varcf6.get()
    item_list["f6"][3]=varscf6.get()


    item_list["s1"][2]=varcs1.get()
    item_list["s1"][3]=varscs1.get()
    item_list["s2"][2]=varcs2.get()
    item_list["s2"][3]=varscs2.get()
    item_list["s3"][2]=varcs3.get()
    item_list["s3"][3]=varscs3.get()
    item_list["s4"][2]=varcs4.get()
    item_list["s4"][3]=varscs4.get()
    item_list["s5"][2]=varcs5.get()
    item_list["s5"][3]=varscs5.get()
    item_list["s6"][2]=varcs6.get()
    item_list["s6"][3]=varscs6.get()
    my_Canvas.delete('all')
    my_Canvas.create_image(0, 0, image=img, anchor="nw")
    my_Canvas.create_line(683,0,683,768, fill="yellow", width=5)
    bnm = Button(root, text="Proceed", font="Arial 20 bold", command=switch3)
    bnm_window = my_Canvas.create_window(995, 711, anchor="nw" , window = bnm )

    bill()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(script_directory, "offline_tiles_nyc.db")
    my_Canvas.create_text(995, 107, text="Delivery Info", font="Arial 40 bold", fill="yellow")
    my_Canvas.create_text(995, 178, text ="Customer : "+ name, font="Arial 30 bold", fill="white")
    global map_widget
    map_widget = tkintermapview.TkinterMapView(root, width=569, height=427, corner_radius=0)
    map_widget.set_position(26.899377700349195, 75.73601841291928)
    map_widget.set_zoom(18)
    mw_window = my_Canvas.create_window(1031,462, anchor=tk.CENTER, window = map_widget)
    map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)
    

    

def add_marker_event(coords):
    global new_marker
    print("Add marker:", coords)
    global cdds
    cdds=coords
    new_marker = map_widget.set_marker(coords[0], coords[1], text="Delivery Location")

def bill():
    global sum
    global count
    count = 0
    sum = 0
    my_Canvas.create_text(284, 107, text="Your final bill", font="Arial 40 bold", fill="yellow")
    j = 0
    for i in item_list.values():
        if(i[2]==1):
            count = count + i[3]
            j= j + 35.55
            sum = sum + i[1]*i[3]
            my_Canvas.create_text(312.84, 142.2+j, text=str(i[0])+"        Quantity : "+str(i[3]) + "          Net Amt=> " + str(i[1]*i[3]), font="Calibri 20", fill="white")
    my_Canvas.create_text(284.4, 142.2 + j+71, text="Total = Rs." + str(sum), font="Calibri 30")

my_Canvas.create_text(974, 142, text="Welcome to our Grocery Store!", font="Arial 40 bold" )
e = Entry(root, justify=CENTER, font="Arial 30")
e.insert(0, "Enter your Name")
e_window = my_Canvas.create_window(750, 284, anchor="nw", window=e)
b1 = Button(root, text="Proceed" ,font="Arial 15 bold", command = switch1)
l1 = Label(root, image=imggc)
l1_window = my_Canvas.create_window(0, 384, anchor="w", window=l1)
b1_window = my_Canvas.create_window(925, 355.5, anchor="nw", window=b1)
my_Canvas.create_text(974, 640, text="Ph.No. : +91 900010000", font="Calibri 30 bold")
my_Canvas.create_text(974, 675, text="Email : admin@krishnstore.com", font="Calibri 30 bold")
root.attributes('-fullscreen', True)





mainloop()

