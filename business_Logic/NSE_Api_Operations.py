#This File is to Implement and Customise the Abstract Functions Provided by NSE_Tools API

from nsetools import  Nse

class NseOperations:
    def GetTheListOfStockSymbols(self): # Method To Get the List of Stock Symbols ,which will return list of Stock Symbols
        nse = Nse()
        all_stock_codes = nse.get_stock_codes()
        Keys_Stock_symbols = []
        for key in all_stock_codes.keys():
            Keys_Stock_symbols.append(key)
        Stock_Symbol = Keys_Stock_symbols[1:]
        return  Stock_Symbol
