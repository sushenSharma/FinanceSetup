from Xpath_Folder import  Folder_Repo

from FolderOperations import CopyFileOperation
import os
import zipfile

class unzip:
    def unzip_operation_for_NumberOfTrades(self):
        #Object Declaration for URL Paths ,Xpaths
        folder_object = Folder_Repo.FolderPath()
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(folder_object.Folder_For_NumberOfTrades_zip):
            for file in f:
                if '.zip' in file:
                    files.append(os.path.join(r, file))

        for file_path in files:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                 zip_ref.extractall(folder_object.Folder_For_NumberOfTrades_CSV)



# Price_Trade_volume_files = []
# for r, d, f in os.walk(folder_object.Folder_For_Price_and_TradedVolume_zip):
#     for file in f:
#         if '.zip' in file:
#             Price_Trade_volume_files.append(os.path.join(r, file))
#
#
# for file_path in Price_Trade_volume_files:
#     with zipfile.ZipFile(file_path, 'r') as zip_ref:
#       zip_ref.extractall(folder_object.Folder_For_Price_and_TradedVolume_zip)