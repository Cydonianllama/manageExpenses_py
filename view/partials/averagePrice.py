from tkinter import Label,Entry,Button,StringVar,LabelFrame,Frame
from tkinter import scrolledtext as st
import tkinter as tk

def renderAveragesPricesForm(x):
    #global variables

    #components of reference
    labelFrameAP    = LabelFrame(x, text= "Average Prices", pady= 15)
    labelLocation   = Label(labelFrameAP,text= "location", width= 8, justify = "right", anchor= "n")
    labelPrice      = Label(labelFrameAP,text= "price"   , width= 8, justify = "right", anchor= "n")

    #componentes of interaction
    locationName = Entry(labelFrameAP, width= 30 )
    price        = Entry(labelFrameAP, width= 30)
    btnAdd       = Button(labelFrameAP,text = "agregar" , width = 16)
    
    #positioning
    labelLocation.grid(pady= 5,row= 0,column = 2,sticky= tk.N)
    labelPrice.grid(pady= 5,row= 1,column = 2,sticky= tk.N)
    locationName.grid(pady= 5 ,row= 0,column= 3)
    price.grid(pady= 5 , row= 1, column= 3 )
    btnAdd.grid(pady= 6,  row= 2, column= 2 , columnspan= 2)
    labelFrameAP.pack(fill= tk.BOTH, side= tk.BOTTOM, expand= False, padx= 15)