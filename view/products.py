#GUI modules
from tkinter import Label,Entry,Button,StringVar,LabelFrame,Frame
from tkinter import scrolledtext as st
import tkinter as tk
from tkinter import ttk
#for partial function
from functools import partial

# my own modules
from controller.expenses import *
from view.partials.averagePrice import renderAveragesPricesForm as apView

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

class productsViews:
    def renderProductForm(self,x):
        #global variables
        _nameProduct = StringVar()

        # we can use justify=tk.LEFT -> instead sticky but in difernect circuntances
        labelFrameProduct = LabelFrame(x, text= "PRODUCT", pady= 15 )
        labelName       = Label(labelFrameProduct, text="name Product" , width = 16)
        labelCategory   = Label(labelFrameProduct, text="category"     , width = 16)
        labelDescription= Label(labelFrameProduct, text="description"  , width = 16)
        
        #the entries of the form
        nameproduct = Entry(labelFrameProduct, width=32 , textvariable = _nameProduct)
        
        category    = ttk.Combobox(labelFrameProduct, state= "readonly",width= 32)
        category['values']= ("seleccionar","basicos","gusto","inesperado","probar", "otros")
        category.current(0) #set the selected item
        
        description = st.ScrolledText(labelFrameProduct,width=32,height=5)
        
        #for give the necesary parameters for the action in command button
        actionBtn   = partial(actionCreateProduct,_nameProduct,description,category)
        
        #btn action
        btnCreate = Button(labelFrameProduct, text= "Create", width= 16, command= actionBtn)
        #positioning
        labelName.grid(pady=5, row= 1, column= 0 ,sticky= tk.W)
        labelCategory.grid(pady=5, row= 2, column= 0 ,sticky= tk.W)
        labelDescription.grid(pady=5, row= 3, column= 0 ,sticky= tk.W)
        nameproduct.grid(padx=5, row=1, column=1 ,sticky=tk.W)
        category.grid(padx= 5, row= 2, column= 1 ,sticky= tk.W)
        description.grid(padx= 5, row= 3,column= 1 ,sticky= tk.W)
        btnCreate.grid(pady= 30,row= 6, column= 0 ,columnspan= 2)
        labelFrameProduct.pack(fill = tk.BOTH , side = tk.TOP , expand = False, padx=15) 

    def tableMaintein(self,x):
        frameMaintein = Frame(x)
        labelFrameAP = LabelFrame(frameMaintein,text= "KeepProducts")
        btnEdit=    Button(labelFrameAP,text= "editar", width=16)
        btnDelete=  Button(labelFrameAP,text= "eliminar", width=16)

        # positioning
        btnEdit.grid(column= 0, row= 0)
        btnDelete.grid(column= 1, row= 0)
        labelFrameAP.pack()
        frameMaintein.pack(fill= tk.BOTH, side= tk.RIGHT, padx= 15, expand= True) 

    def getViewProduct(self,x):
        frameProduct = ttk.Frame(x)
        # partial of average price view (render Method)
        apView(frameProduct)
        # intern views of product UI
        self.tableMaintein(frameProduct)
        self.renderProductForm(frameProduct)
        return frameProduct