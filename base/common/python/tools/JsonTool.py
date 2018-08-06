import os,sys,time,datetime,json
import urllib.request as requests
sys.path.append("../")

from LogController.LogShow import LogShow
from ExceptionController.Exception import *

open_debug = True

class JsonTool(object):
    def __init__(self):
        self.class_name = "JsonTool"
        self.json_res = {}
        self.logtool = LogShow(self.class_name)

    def __str__(self):
        return self.class_name
    
    def getJson(self):
        return self.json_res

    def anaPostresult(self, result):
        if isinstance(result, requests.Request):
            if result.status_code == 200:
                return True
            else:
                return False

    def serialize(self, class_name, jsoninfo):
        if jsoninfo is None:
            return None
        try:
            if type(jsoninfo) != type({}):
                if open_debug:
                    self.logtool.log_print ("debug", str(class_name) + " -- " + str(jsoninfo), "serialize")
                json_result = json.loads(jsoninfo)
                if open_debug:
                    self.logtool.log_print ("debug", str(class_name) + " -- " + str(json_result), "serialize")
                return self.createClass(class_name, json_result)
            if type(jsoninfo) == type({}):
                return self.createClass(class_name, jsoninfo)
            # if type(jsoninfo) == type([]):
            #     return self.createClass(class_name, jsoninfo)
        except TypeError as e:
            print("[error][JsonTool-serialize] " + str(class_name) + " -- " + str(e))
            raise NoneTypeException
            #return self.createClass(class_name, jsoninfo)
        except ValueError as ee:
            return self.createClass(class_name, jsoninfo)

    def deserialize(self, cla):
        if cla is None:
            return None
        try:
            jsoninfo = self.getJsonfromClass(cla)
        except:
            jsoninfo = cla
        if jsoninfo is None:
            return None
        else:
            try:
                jsoninfo = json.dumps(jsoninfo)
            except:
                pass
        return jsoninfo
    
    def createClass(self, class_name, json_result):
        pass

    def getJsonfromClass(self, cla):        
        return cla.getJson()