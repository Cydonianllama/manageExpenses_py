from tkinter import Label,Entry,Button,StringVar
from functools import partial

# my own modules
from controller.expenses import *


#pcik up the data for the entries form
def getData(nameproduct_var,quantity_var,cost_var,dateBuy_var,description_var):
    data = {
        "nameproduct": nameproduct_var.get(),
        "quantity": quantity_var.get(),
        "cost": cost_var.get(),
        "datebuy": dateBuy_var.get(),
        "description": description_var.get()
    }
    print(data)

# action the button create product

def actionCreateProduct(nameproduct_var, quantity_var, cost_var, dateBuy_var, description_var):
    getData(nameproduct_var, quantity_var, cost_var, dateBuy_var, description_var)
    #createProduct(data)

#main class for the dasboard expenses
class dashboardExpenses:
    #x is a tk() class
    def renderProductForm(self,x):
        #variable for pickup the data
        nameproduct_var = StringVar()
        quantity_var = StringVar()
        cost_var = StringVar()
        dateBuy_var = StringVar()
        description_var = StringVar()
        Label(x, text = "Product Form").grid(pady = 5 , row = 0 , column = 0)
        #configurations grid
        x.columnconfigure(1, weight=1)
        x.columnconfigure(2, weight=1)
        x.columnconfigure(3, weight=1)
        x.columnconfigure(4, weight=1)
        x.columnconfigure(5, weight=1)
        x.rowconfigure(7, weight=1)
        # the labels of the form
        Label(x, text="name Product").grid(pady=5, row=1, column=0)
        Label(x, text="quantity").grid(pady=5, row=2, column=0)
        Label(x, text="cost").grid(pady=5,row = 3 , column=0)
        Label(x, text="datebuy").grid(pady=5,row=4,column=0)
        Label(x, text="description").grid(pady = 5 ,row = 5, column = 0)
        #the entries of the form
        nameproduct     = Entry(x, width=40 , textvariable = nameproduct_var).grid(padx=5, row=1, column=1)
        quantity        = Entry(x, width=40 , textvariable = quantity_var).grid(padx=5, row=2, column=1)
        cost            = Entry(x, width=40 , textvariable = cost_var).grid(padx=5, row=3, column=1)
        dateBuy         = Entry(x, width=40 , textvariable = dateBuy_var).grid(padx=5, row=4, column=1)
        description     = Entry(x, width=40 , textvariable = description_var).grid(padx=5, row=5, column=1)
        #for give the necesary parameters for the action in command button
        actionBtn = partial(actionCreateProduct, nameproduct_var,
                            quantity_var, cost_var, dateBuy_var, description_var)
        #btn action
        Button(x, text="Create", width=50, command=actionBtn).grid(padx=10, pady=10, row=7, column=0, columnspan=2)
    def renderServiceForm(self,x):
        x.columnconfigure()
