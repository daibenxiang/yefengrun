#encoding='UTF-8'
import os, sys, time

from Log.LogShow import LogShow

class LogController(object):

    def __init__(self):
        self.class_name = "LogController"

    def __str__(self):
        return self.class_name

    @classmethod
    def getLogger(self, logclass):
        return LogShow(logclass)


if __name__ == "__main__":
    ls = LogController.getLogger("test")
    ls.log_print("warn", "teststestest")
    os.system("pause")
