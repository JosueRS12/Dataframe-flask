from ..connection.Connection import results
import pandas as pd


class Controller():

    def __init__(self):
        self.df = pd.DataFrame.from_records(results)
        self.myDf = None

    def getDataframe(self):
        self.cleanDataframe()
        self.toIntDataframe('cantidad')
        return self.myDf

    def cleanDataframe(self):
        self.myDf = self.df.dropna(0, how="any")
        
    def toIntDataframe(self, column):
        self.myDf[column] = self.df[column].astype('int64')
