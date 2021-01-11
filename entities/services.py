class services:
	#services atts
	idProduct
	nameServices
	description
	averagePrices
	category
	#average prices atts
	idAveragePrice
	idLocation
	price
	#location atts
	idLocation
	namelocation
	description
    def __init__(self,idProduct,nameServices,description,averagePrices,category):
    	self.idProduct = idProduct
    	self.nameServices = nameServices
    	self.description = description
    	self.averagePrices = averagePrices
    	self.category = category
    def addAveragePrice(self,idAveragePrice,idLocation,price):
    	self.idLocation = idLocation
    	self.idAveragePrice = idAveragePrice
    	self.price = price
    def addLocation(self,idLocation,namelocation,description):
    	self.idLocation = idLocation
    	self.namelocation = namelocation
    	self.description = description