# -*- coding: utf-8 -*-
import os,sys
import configparser
sys.path.append("..")
from Log.LogController import LogController

result=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
confPath=result+r"\File\Config\\"
class ReadConfig:
    def __init__(self,configName):
        self.conf = configparser.ConfigParser()
        self.conf.read(confPath + configName, encoding='utf-8-sig')
        self.class_name = "ReadConfig"
        self.ls = LogController.getLogger(self.class_name)

    def getReadSqlSever(self, name):
        try:
            value = self.conf.get("SQLSEVER", name)
            return value
        except Exception as e:
            self.ls.log_print("error", str(e), "getReadSqlSever")
            return False

    def getReadMySql(self, name):
        try:
            value = self.conf.get("MYSQL", name)
            return value
        except Exception as e:
            self.ls.log_print("error", str(e), "getReadMySql")
            return False


if __name__=='__main__':
    test=ReadConfig('Config.ini')
    print(test.getReadMySql('ip'))
