from Log.LogController import LogController


import os, sys, time, json



class SetUp(object):
    def __init__(self):
        self.class_name = "SetUp"
        self.logger = LogController.getLogger(self.class_name)

    def __str__(self):
        return self.class_name


    def setup(self):
        
