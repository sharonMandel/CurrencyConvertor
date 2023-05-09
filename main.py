'''
EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United
Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON -
Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong
Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi
|TRY - Turkey Lira |HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States
Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic
Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand
'''
from forex_python.converter import CurrencyRates

from currencyConvertor import *

class Main():
    def __init__(self):
         self.file_type = ".txt"

    def startProgram(self):
         currencyConvertor = CurrencyConvertor()

         fileName = ""
         while True:
            if not fileName:
                fileName = input("Please enter the name of txt file e.g. nameOfFile.txt: ")
            else:
                fileName = input("Invalid input file. Please enter the name of txt file e.g. nameOfFile.txt: ")

            if currencyConvertor.validateInputFile(fileName):
                currencyConvertor.ReadAndWriteToList(fileName)
                currencyList = currencyConvertor.checkConvertDataToList()
                print(currencyList)

                break

if __name__ == "__main__":
    start_program = Main()
    start_program.startProgram()


