class user:
	#user atts
	idUser
	fullname
	dateBirthdate
	username
	password
	#user log atts
	idLogUser
	idUser
	dateLog
	descriptionLog
	def __init__(self,idUser,fullname,dateBirthdate,username,password):
		self.idUser = idUser
		self.fullname = fullname
		self.dateBirthdate = dateBirthdate
		self.username = username
		self.password = password

	def addLogUser(self,idLogUser,idUser,dateLog,descriptionLog):
		self.idLogUser = idLogUser
		self.idUser = idUser
		self.dateLog = dateLog
		self.descriptionLog = descriptionLog