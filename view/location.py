#GUI modules
from tkinter import Label,Entry,Button,StringVar,LabelFrame,Frame
from tkinter import scrolledtext as st
import tkinter as tk

class locationView:
	def renderMaintein(self,x):
		#global variables

		#components of reference
		container 				= Frame(x)
		headNameLocation 		= Label(container,text= "location", width= 16)
		headDescriptionLocation = Label(container,text= "desctiption", width= 32)

		#containers
		containerActionsBottom = Frame(container)
		
		#actions maintein
		btnEdit  = Button(containerActionsBottom,text= "Edit", width= 10)
		btnDelete= Button(containerActionsBottom,text= "Delete", width= 10)
		
		#positioning part
		headNameLocation.grid(column= 0, row= 0)
		headDescriptionLocation.grid(column= 1, row= 0)
		#containerActionsBottom.grid(column = 3 , row = 12,columnspan= 2)
		btnEdit.grid(column = 0 , row = 0)
		btnDelete.grid(column = 1 , row = 0)
		containerActionsBottom.grid(column = 0,columnspan = 2,row= 8)
		container.pack(fill= tk.BOTH, side= tk.TOP, expand= True)

	def renderForm(self,x):
		#variables
		nameLocation_= StringVar()

		#components of reference
		textField			= LabelFrame(x,text= "maintein location")
		labelNamaLocation 	= Label(textField, text= "Name Location", width= 16)
		labelDescription 	= Label(textField, text= "description", width= 16)

		#interaction Components
		nameLocation 		= Entry(textField ,width= 20, textvariable= nameLocation_)
		description 		= st.ScrolledText(textField,width= 20,height= 5)
		btnAdd 				= Button(textField,text= "add", width= 16)

		#positioning Part
		labelNamaLocation.grid(column= 0,row= 0)
		labelDescription.grid(column= 0,row= 1)
		nameLocation.grid(column= 1, row=0,sticky= tk.W)
		description.grid(column= 1, row = 1,sticky= tk.W)
		btnAdd.grid(column = 0,columnspan = 2,row=3)
		textField.pack(fill =tk.BOTH, side = tk.TOP , expand= True)

	# this method contain all the logic of the views for render 
	def getFrameLocation(self,x):
		FrameLocation = Frame(x)
		self.renderForm(FrameLocation)
		self.renderMaintein(FrameLocation)
		return FrameLocation