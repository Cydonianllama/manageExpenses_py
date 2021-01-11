class expenses:
	#expenses atts
	idExpenses
	reviewDate
	expenseItems#an array
	#expenses items atts
	idProduct
	idService
	price
	quantity
	paymentMethod
	measurementSytem
	description
	dateExpense
	aproxDateExpenseRangeFirst
	aproxDateExpenseRangeLast
	TypeNecesity
    def __init__(self,idExpenses,reviewDate,expenseItems):
    	self.idExpenses = idExpenses
    	self.reviewDate = reviewDate
    	self.expenseItems = expenseItems
    def addItem(self,idProduct,idService,price,quantity,paymentMethod,measurementSytem,description,dateExpense,aproxDateExpenseRangeLast,aproxDateExpenseRangeFirst,TypeNecesity):
