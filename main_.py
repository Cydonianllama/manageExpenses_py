from datetime import *

#my own modules...
from utils.tkinter import window
from view.tableExpenses import *
#from utils.connection import db

#instances a global vaiables
Dexpenses = dashboardExpenses()

#post = db.posts

dataTest = {
    "fullnames" : "erick manuel grandez mendoza",
    "desctiption" : "im a normal guy",
    "inscriptionDate" : datetime.now()
}

def app():
    #post_id = post.insert_one(dataTest).inserted_id
    #print(post_id)
    Dexpenses.renderAll(window)
    window.mainloop()
app()
