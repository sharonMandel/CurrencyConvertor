import pandas as pd
import os
from forex_python.converter import CurrencyRates

class CurrencyConvertor():
    def __init__(self):
        self.TurnFrom = None
        self.TurnTo = None
        self.pathFile = os.path.abspath(os.getcwd())
        self.dataFileList = []

        self.inputFileType = ".txt"

    def validateInputFile(self, fileName):
        global FullPathFile
        FullPathFile = self.pathFile + '/'+ fileName
        if os.path.isfile(FullPathFile):
            if self.inputFileType in fileName:
                return True

        return False

    def ReadAndWriteToList(self, fileName):
        dataFile = pd.read_csv(FullPathFile, header=None)
        self.dataFileList =  dataFile[0][:]
        if len( self.dataFileList ) > 2:
            self.TurnFrom =  str(self.dataFileList [0])
            self.TurnTo =  str(self.dataFileList[1])
            return dataFile[0][:]
        else:
            print('This file no conatins coins to transfer')

    def checkConvertDataToList(self):
        coinsList = []
        currentRatesData = CurrencyRates()
        dict_from,dict_to = currentRatesData.get_rates(self.TurnFrom),currentRatesData.get_rates(self.TurnTo)

        if  self.TurnTo not in dict_from.keys():
            if self.TurnFrom in dict_to.keys():
                amount_to_convert = dict_to.get(self.TurnFrom)
        else:
            amount_to_convert = dict_from.get(self.TurnTo)

        for moneyToConvert in  self.dataFileList[2:]:
            moneyToConvert = float(moneyToConvert)*float(amount_to_convert)
            coinsList.append(moneyToConvert)
        return coinsList
