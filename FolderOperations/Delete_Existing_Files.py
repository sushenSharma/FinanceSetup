import shutil
import os, re, os.path

class DeleteExistingFiles:
    def delete_Operation(self,mypath):
        for root, dirs, files in os.walk(mypath):
            for file in files:
                print(file)
                os.remove(os.path.join(root, file))