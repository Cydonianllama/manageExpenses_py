class services:
    def __init__(self,nameservice,description,cost,dateservice,typenecesity):
        self.nameservice = nameservice
        self.description = description
        self.cost = cost
        self.dateService = dateservice
        self.typenecesity = typenecesity
    def getCost(self):
        return self.nameservice