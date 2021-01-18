# [guide]: x in the methods are the window component from tkinter 

#my own modules...
from utils.tkinter import window
from view.products import *
from view.location import *
#from utils.connection import db

#instances a global vaiables
viewProduct = productsViews()
viewLocation = locationView()


from tkinter import ttk
import tkinter as tk
from tkinter import *

class mainView:

	def __init__(self):
		print("main view created")
	def createSwicthToPanel(self,x):
		n= 	ttk.Notebook(x)
		Frame1= viewProduct.getViewProduct(n)
		Frame2= ttk.Frame(n)
		Frame3= viewLocation.getFrameLocation(n)

		# add content of the notebook
		n.add(Frame1, text= 'productos')
		n.add(Frame2, text= 'servicios')
		n.add(Frame3, text= 'locations')

		# positioning
		n.pack(side= tk.TOP, fill= tk.BOTH , expand= False)

	# method that contain all the logic of this class
	def renderAll(self,x):
		self.createSwicthToPanel(x)