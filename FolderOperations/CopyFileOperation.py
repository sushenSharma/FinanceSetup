
import shutil,os
import  glob
import shutil
from FolderOperations import  Delete_Existing_Files

class CopyFile:
  def Operation_To_Copy_File_From_One_Folder_To_Another_Folder(self,file_Download_Folder,destination_path):
    #delete_files_object = Delete_Existing_Files.DeleteExistingFiles()
    #delete_files_object.delete_Operation(destination_path)
    list_of_files = glob.glob(file_Download_Folder) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    shutil.copy(latest_file,destination_path)

  def Operation_To_RenameFile(self,destination_path):
    list_of_files = glob.glob(destination_path)  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file