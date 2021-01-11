class products:
	#product-atributes
	idProduct
	nameProduct
	description
	averagePrices#an array
	category
	#average prices att
	idAveragePrice
	idLocation#an array
	price
	#location att
	idLocation
	namelocation
	description
    def __init__(self,idProduct,nameProduct,description,averagePrices,category):
    	self.idProduct = idProduct
    	self.nameProduct = nameProduct
    	self.description = description
    	self.averagePrices = averagePrices
    	self.category = category
    def addLocation(self,idLocation,namelocation,description):
    	self.idLocation = idLocation
    	self.namelocation = namelocation
    	self.description = description
    	print('still in development')
    def addAveragePrice(self,idAveragePrice,idLocation,price):
    	self.idAveragePrice = idAveragePrice
    	self.idLocation = idLocation
    	self.price = price
