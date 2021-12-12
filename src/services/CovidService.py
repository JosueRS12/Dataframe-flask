from ..controller.Controller import Controller

class CovidService:

    def __init__(self):
        myController = Controller()
        self.myDf = myController.getDataframe()

    def showDataFrame(self):
        # self.myDf.style.set_table_styles([self.dicStyles['headers']])
        return self.myDf

    def byColumn(self, column):
        if(column!=None):
            dfQuery = self.myDf.loc[:,f'{column}']
            return dfQuery.to_frame(name=None)
        return None

    def byValueTerritory(self, value):
        if(value!=None):
            dfQuery = self.myDf.query(f"nom_territorio=='{value}'") 
            return dfQuery
        return None

    def byColumnValue(self, column,  value):
        if(column!=None and value!=None):
            dfQuery = self.myDf.query(f"{column}=='{value}'") 
            return dfQuery
        return None


    def byCountVaccines(self, count):
        if(count!=None):
            dfQuery = self.myDf[self.myDf['cantidad']>int(count)]
            return dfQuery
        return None

    def maxByTypeVac(self, typeVac):
        if(typeVac!=None):
            dfQuery = self.myDf.query(f"laboratorio_vacuna=='{typeVac}'")[['nom_territorio', 'cantidad']].max() 
            return dfQuery.to_frame(name=None)
        return None
    
    
