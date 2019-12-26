import logging
from business_Logic import NSE_Api_Operations
import pandas as pd
from FolderOperations import  CopyFileOperation
from  Xpath_Folder import Folder_Repo


def Average(lst):
    return sum(lst) / len(lst)

class Logic_Library:
    def Logic_toIndentify_Selling_Buying_byBigPlayer(self):
        Fd = Folder_Repo.FolderPath()
        Cp = CopyFileOperation.CopyFile()

        logging.basicConfig(filename="LogFile.log",filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO)
        Nse = NSE_Api_Operations.NseOperations()
        List_Of_Stocks = Nse.GetTheListOfStockSymbols()
        name = Cp.Operation_To_RenameFile(Fd.Folder_For_CSV_File)
        dataFrame = pd.read_csv(name)
        filter_dataFrame = dataFrame[dataFrame['Series'] == 'EQ']
        filter_dataFrame.rename(columns={'% Dly Qt to Traded Qty':'Percentage_delivery_qty'},inplace=True)
        #print(filter_dataFrame.columns)
        nt_tq = dataFrame["Total Traded Quantity"]/dataFrame["No. of Trades"]
        filter_dataFrame['NT/TQ']=nt_tq
        #print(filter_dataFrame.columns)
        Actual_dataFrame = filter_dataFrame[["Average Price","Total Traded Quantity","Turnover","No. of Trades","Deliverable Qty","Percentage_delivery_qty","NT/TQ"]]
        print(Actual_dataFrame.head())
        Reverse_Data_Frame = Actual_dataFrame.iloc[::-1]


        Average_Price_List = Reverse_Data_Frame["Average Price"].tolist()
        TotalTradedQuantity_List = Reverse_Data_Frame["Total Traded Quantity"].tolist()
        TurnOver_List = Reverse_Data_Frame["Turnover"].tolist()
        NumberOfTrades_List = Reverse_Data_Frame["No. of Trades"].tolist()
        DeliverableQuantity_List = Reverse_Data_Frame["Deliverable Qty"].tolist()
        Percentage_Delivery_Qty_List = Reverse_Data_Frame["Percentage_delivery_qty"].tolist()
        TQ_NT_List = Reverse_Data_Frame["NT/TQ"].tolist()


        Average_Price_3Day_Average = Average(Average_Price_List[:3])
        Average_Price_5Day_Average = Average(Average_Price_List[:5])
        Average_Price_8Day_Average = Average(Average_Price_List[:8])
        Average_Price_13Day_Average = Average(Average_Price_List[:13])

        TotalTradedQuantity_3Day_Average = Average(TotalTradedQuantity_List[:3])
        TotalTradedQuantity_5Day_Average = Average(TotalTradedQuantity_List[:5])
        TotalTradedQuantity_8Day_Average = Average(TotalTradedQuantity_List[:8])
        TotalTradedQuantity_13Day_Average = Average(TotalTradedQuantity_List[:13])


        TurnOver_3Day_Average = Average(TurnOver_List[:3])
        TurnOver_5Day_Average = Average(TurnOver_List[:5])
        TurnOver_8Day_Average = Average(TurnOver_List[:8])
        TurnOver_13Day_Average = Average(TurnOver_List[:13])

        NumberOfTrades_3Day_Average = Average(NumberOfTrades_List[:3])
        NumberOfTrades_5Day_Average = Average(NumberOfTrades_List[:5])
        NumberOfTrades_8Day_Average = Average(NumberOfTrades_List[:8])
        NumberOfTrades_13Day_Average = Average(NumberOfTrades_List[:13])


        DeliverableQuantity_3Day_Average = Average(DeliverableQuantity_List[:3])
        DeliverableQuantity_5Day_Average = Average(DeliverableQuantity_List[:5])
        DeliverableQuantity_8Day_Average = Average(DeliverableQuantity_List[:8])
        DeliverableQuantity_13Day_Average = Average(DeliverableQuantity_List[:13])


        Percentage_Delivery_Qty_3Day_Average = Average(Percentage_Delivery_Qty_List[:3])
        Percentage_Delivery_Qty_5Day_Average = Average(Percentage_Delivery_Qty_List[:5])
        Percentage_Delivery_Qty_8Day_Average = Average(Percentage_Delivery_Qty_List[:8])
        Percentage_Delivery_Qty_13Day_Average = Average(Percentage_Delivery_Qty_List[:13])


        TQ_NT_3Day_Average = Average(TQ_NT_List[:3])
        TQ_NT_5Day_Average = Average(TQ_NT_List[:5])
        TQ_NT_8Day_Average = Average(TQ_NT_List[:8])
        TQ_NT_13Day_Average = Average(TQ_NT_List[:13])


        print("Average_Price_3Day_Average :",Average_Price_3Day_Average )
        print("Average_Price_5Day_Average :",Average_Price_5Day_Average )
        print("Average_Price_8Day_Average :",Average_Price_8Day_Average )
        print("Average_Price_13Day_Average :",Average_Price_13Day_Average )


        print("TotalTradedQuantity_3Day_Average :",TotalTradedQuantity_3Day_Average)
        print("TotalTradedQuantity_5Day_Average :",TotalTradedQuantity_5Day_Average)
        print("TotalTradedQuantity_8Day_Average :",TotalTradedQuantity_8Day_Average)
        print("TotalTradedQuantity_13Day_Average :",TotalTradedQuantity_13Day_Average)

        print("TurnOver_3Day_Average:",TurnOver_3Day_Average)
        print("TurnOver_5Day_Average:",TurnOver_5Day_Average)
        print("TurnOver_8Day_Average:",TurnOver_8Day_Average)
        print("TurnOver_13Day_Average:",TurnOver_13Day_Average)

        print("NumberOfTrades_3Day_Average",NumberOfTrades_3Day_Average)
        print("NumberOfTrades_5Day_Average",NumberOfTrades_5Day_Average)
        print("NumberOfTrades_8Day_Average",NumberOfTrades_8Day_Average)
        print("NumberOfTrades_13Day_Average",NumberOfTrades_13Day_Average)


        print("DeliverableQuantity_3Day_Average",DeliverableQuantity_3Day_Average)
        print("DeliverableQuantity_5Day_Average",DeliverableQuantity_5Day_Average)
        print("DeliverableQuantity_8Day_Average",DeliverableQuantity_8Day_Average)
        print("DeliverableQuantity_13Day_Average",DeliverableQuantity_13Day_Average)

        print("Percentage_Delivery_Qty_3Day_Average",Percentage_Delivery_Qty_3Day_Average)
        print("Percentage_Delivery_Qty_5Day_Average",Percentage_Delivery_Qty_5Day_Average)
        print("Percentage_Delivery_Qty_8Day_Average",Percentage_Delivery_Qty_8Day_Average)
        print("Percentage_Delivery_Qty_13Day_Average",Percentage_Delivery_Qty_13Day_Average)

        print("TQ_NT_3Day_Average",TQ_NT_3Day_Average)
        print("TQ_NT_5Day_Average",TQ_NT_5Day_Average)
        print("TQ_NT_8Day_Average",TQ_NT_8Day_Average)
        print("TQ_NT_13Day_Average",TQ_NT_13Day_Average)


        if TQ_NT_3Day_Average > TQ_NT_5Day_Average > TQ_NT_8Day_Average > TQ_NT_13Day_Average:
            logging.info('Big Players are Active in  Stock :')

        if Average_Price_3Day_Average > Average_Price_5Day_Average > Average_Price_8Day_Average > Average_Price_13Day_Average:
            if TotalTradedQuantity_3Day_Average > TotalTradedQuantity_5Day_Average > TotalTradedQuantity_8Day_Average > TotalTradedQuantity_13Day_Average:
                if TurnOver_3Day_Average > TurnOver_5Day_Average> TurnOver_8Day_Average> TurnOver_13Day_Average:
                    if NumberOfTrades_3Day_Average > NumberOfTrades_5Day_Average > NumberOfTrades_8Day_Average > NumberOfTrades_13Day_Average:
                        if DeliverableQuantity_3Day_Average > DeliverableQuantity_5Day_Average > DeliverableQuantity_8Day_Average > DeliverableQuantity_13Day_Average:
                             logging.info('Delivery Based Buying in  Stock :')
                             if TQ_NT_3Day_Average > TQ_NT_5Day_Average > TQ_NT_8Day_Average > TQ_NT_13Day_Average:
                                 logging.info('Big Players are Active in  Stock :')


        if Average_Price_3Day_Average < Average_Price_5Day_Average < Average_Price_8Day_Average < Average_Price_13Day_Average:
            if TotalTradedQuantity_3Day_Average < TotalTradedQuantity_5Day_Average < TotalTradedQuantity_8Day_Average < TotalTradedQuantity_13Day_Average:
                if TurnOver_3Day_Average < TurnOver_5Day_Average< TurnOver_8Day_Average< TurnOver_13Day_Average:
                    if NumberOfTrades_3Day_Average < NumberOfTrades_5Day_Average < NumberOfTrades_8Day_Average < NumberOfTrades_13Day_Average:
                        if DeliverableQuantity_3Day_Average < DeliverableQuantity_5Day_Average < DeliverableQuantity_8Day_Average < DeliverableQuantity_13Day_Average:
                             logging.info('Delivery Based Selling in  Stock :')
                             if TQ_NT_3Day_Average > TQ_NT_5Day_Average > TQ_NT_8Day_Average > TQ_NT_13Day_Average:
                                 logging.info('Big Players are Active in  Stock :')




