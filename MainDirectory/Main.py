from UI_Operations_Folder import UI_Operations
from Xpath_Folder import  Xpath_Repo,URL_Repo,Folder_Repo
from FolderOperations import  CopyFileOperation,Delete_Existing_Files,Unzip_operation
from business_Logic import Logic_to_Identify_Buying_Selling_By_BigPlayer,NSE_Api_Operations


Xp = Xpath_Repo.Xpath()
Url = URL_Repo.url()
UI = UI_Operations.UI_Operation();  #Create Object for UI_Operation Class
Fd  = Folder_Repo.FolderPath()
lg = Logic_to_Identify_Buying_Selling_By_BigPlayer.Logic_Library()
nse = NSE_Api_Operations.NseOperations()

copy_Object = CopyFileOperation.CopyFile()
delete_Object = Delete_Existing_Files.DeleteExistingFiles()


stock_name = nse.GetTheListOfStockSymbols()
for i in range(len(stock_name)):
    UI.Navigate_To_Url(Url.URL_To_Fetch_Data_For_Equity)
    UI.Click_On_Input_Field(Xp.Xpath_For_Symbol_Input)
    UI.Type_Text_in_Input_Field(Xp.Xpath_For_Symbol_Input,stock_name[i])
    UI.Click_On_DropDown_Operation_And_Select_Value(Xp.Xpath_For_DropDown_Selector,Xp.Xpath_For_Selecting_1Month)
    UI.Click_On_Input_Field(Xp.Xpath_For_GetData_Button)
    UI.Click_On_Input_Field(Xp.Xpath_For_DataLink_Download)
    copy_Object.Operation_To_Copy_File_From_One_Folder_To_Another_Folder(Fd.file_Download_Folder,Fd.Folder_For_CSV_File)
    lg.Logic_toIndentify_Selling_Buying_byBigPlayer()
    delete_Object.delete_Operation(Fd.Folder_For_CSV_File)





