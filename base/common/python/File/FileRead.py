
import os
from XlsxTool import XlsxTool


class FileRead(object):
    def __int__(self):
        self.class_name = "FileRead"


    def __str__(self):
        return self.class_name

    def open(self, filename):
        if not isinstance(filename, str):
            return False
        file_context = None
        if str(filename).endswith("xlsx"):
            xt = XlsxTool(filename)
            return xt
        if str(filename).endswith("json"):
            pass

if __name__ == "__main__":
    fr = FileRead()
    xlsx = fr.open("Template.xlsx")
    for x in xlsx.readSheetbyName(xlsx.getSheetNames()[0]).rows:
        print (x)
    
    



    