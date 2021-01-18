from datetime import *

# my pwn modules
from view.mainView import *

#post = db.posts

dataTest = {
    "fullnames" : "erick manuel grandez mendoza",
    "desctiption" : "im a normal guy",
    "inscriptionDate" : datetime.now()
}

viewMain = mainView()

def app():
    #post_id = post.insert_one(dataTest).inserted_id
    #print(post_id)

    # all the configurations for the views
    viewMain.renderAll(window)

    # initialize the GUI 
    window.mainloop()
app()
