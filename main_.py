from utils.tkinter import window
from view.tableExpenses import *

#instances a global vaiables
Dexpenses = dashboardExpenses()

def app():
    Dexpenses.renderProductForm(window)
    window.mainloop()

app()