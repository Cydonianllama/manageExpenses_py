#GUI modules
from tkinter import Label,Entry,Button,StringVar,LabelFrame,Frame
from tkinter import scrolledtext as st
import tkinter as tk
from tkinter import ttk
#for partial function
from functools import partial

# my own modules
from controller.expenses import *


#pcik up the data for the entries form
def getData(_nameProduct,description,_category):
    data = {
        "nameproduct": _nameProduct.get(),
        "description": description.get("1.0",tk.END),
        "category": _category.get(),
    }
    print(data)

# action the button create product

def actionCreateProduct(_nameProduct,description,_category):
    getData(_nameProduct,description,_category)
    #createProduct(data)

#main class for the dasboard expenses
class dashboardExpenses:
    #x is a tk() class
    def navBar(self):
        print('still in development')
    def renderProductForm(self,x):
        #######averagePrices#an array
        #######category
        ########average prices att
        #######idAveragePrice
        #######idLocation#an array
        #######price
        ########location att
        #######idLocation
        #######namelocation
        #######description
        #variable for pickup the data
        labelFrameProduct = LabelFrame(x, text= "PRODUCT", pady= 15 )
        labelFrameProduct.pack(fill = tk.BOTH , side = tk.LEFT , expand = False, padx=15) 
        _nameProduct = StringVar()
        # the labels of the form
        # we can use justify=tk.LEFT -> instead sticky but in difernect circuntances
        Label(labelFrameProduct, text="name Product" , width = 16).grid(pady=5, row= 1, column= 0 ,sticky= tk.W)
        Label(labelFrameProduct, text="category"     , width = 16).grid(pady=5, row= 2, column= 0 ,sticky= tk.W)
        Label(labelFrameProduct, text="description"  , width = 16).grid(pady=5, row= 3, column= 0 ,sticky= tk.W)

        #the entries of the form
        nameproduct = Entry(labelFrameProduct, width=32 , textvariable = _nameProduct).grid(padx=5, row=1, column=1 ,sticky=tk.W)
        category    = ttk.Combobox(labelFrameProduct, state= "readonly",width= 32)
        category['values']= ("seleccionar","basicos","gusto","inesperado","probar", "otros")
        category.current(0) #set the selected item
        category.grid(padx= 5, row= 2, column= 1 ,sticky= tk.W)
        description = st.ScrolledText(labelFrameProduct,width=32,height=5)
        description.grid(padx= 5, row= 3,column= 1 ,sticky= tk.W)
        #for give the necesary parameters for the action in command button
        actionBtn   = partial(actionCreateProduct,_nameProduct,description,category)
        #btn action
        Button(labelFrameProduct, text= "Create", width= 16, command= actionBtn).grid(pady= 30,row= 6, column= 0 ,columnspan= 2)
    def renderAveragesPricesForm(self,x):
        labelFrameAP = LabelFrame(x,text ="Average Prices" , pady= 15 )
        labelFrameAP.pack(fill = tk.BOTH , side = tk.LEFT , expand = False, padx=15)
        Label(labelFrameAP,text= "location", width= 8, justify = "right" , anchor= "n").grid(pady= 5,row= 0,column = 2,sticky= tk.N)
        Label(labelFrameAP,text= "price"   , width= 8, justify = "right" , anchor= "n").grid(pady= 5,row= 1,column = 2,sticky= tk.N)
        locationName = Entry(labelFrameAP, width= 30 )
        locationName.grid(pady = 5 ,row= 0 ,column= 3 )
        price        = Entry(labelFrameAP,width= 30)
        price.grid(pady= 5 , row= 1, column= 3 )
    def renderAll(self,x):
        containerUP = Frame(x)
        #containerUP.config(width = 0,height =0)
        containerUP.pack(fill = tk.Y , side = tk.LEFT  , expand = False)
        self.renderProductForm(x)
        self.renderAveragesPricesForm(x)

