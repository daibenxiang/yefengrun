import os,time,datetime,json,sys
import urllib.request as urllib2
import urllib.parse
import urllib.error as urlerror

sys.path.append("..")

from ExceptionController.Exception import *
from LogController.LogShow import LogShow
from CheckController.CheckIP import CheckIP
from tools.JsonTool import JsonTool
open_debug = True

class HttpController(object):
    def __init__(self, ip):
        self.class_name = "HttpController"
        self.ip = ip
        self.url_http_pre = 'http://' 
        self.url_https_pre = 'https://'
        self.headers = {}
        self.headers["Accept"] = "application/json"
        self.jsontool = JsonTool()
        self.logtool = LogShow(self.class_name)

    def checkNetwork(self):
        return CheckIP.checkIP(self.ip)

    def get(self, url, data=None):
        self.checkNetwork()
        request = None
        response = None
        result = None
        data = bytes(data, encoding='utf8')  if data is not None else None
        try:
            if open_debug:
                self.logtool.log_print("debug", '[url] ' + url, "get")
            request = urllib2.Request(url, headers=self.headers, data = data if data is not None else None)
            response = urllib2.urlopen(request)
            result =response.read()
            if open_debug:
                self.logtool.log_print("debug", 'get = ' + str(result), "get")
            return result.strip()
        except urlerror.HTTPError as ee:
            self.logtool.log_print ("error", str(ee), "get")
        except urllib2.URLError as e:
            #return e.code
            self.logtool.log_print ("error", str(e), "get")
        except Exception as e:
            self.logtool.log_print("error", str(e), "get")

    def post(self, url, data=None): 
        self.checkNetwork()
        try:
            if open_debug:
                self.logtool.log_print("debug", '[url] ' + url, "post")
            request = None
            response = None
            result = None
            #data = data.encode('utf-8')
            data = bytes(data, encoding='utf8')  if data is not None else None
            request = urllib2.Request(url, headers=self.headers, data=data)
            response = urllib2.urlopen(request)
            result =response.read()
            if open_debug:
                self.logtool.log_print("debug", 'post = ' + str(result), "post")
            return result
        except urllib2.URLError as e:
            #return e.code
            self.logtool.log_print ("error", str(e), "post")
        except Exception as ee:
            self.logtool.log_print ("error", str(ee), "post")
            raise NoneTypeException

    def put(self, url, data=None):
        self.checkNetwork()
        try:  
            if open_debug:
                self.logtool.log_print("debug", '[url] ' + url, "put")
            request = None
            response = None
            result = None
            data = bytes(data, encoding='utf8')  if data is not None else None
            request = urllib2.Request(url, headers=self.headers, data=data)
            request.get_method = lambda: 'PUT'
            response = urllib2.urlopen(request, timeout=10)
            result = response.read()
            if open_debug:
                self.logtool.log_print("debug", 'put = ' + str(result), "put")
            return result
        except urllib2.URLError as e:
            self.logtool.log_print ("error", str(e), "put")
        except Exception as ee:            
            self.logtool.log_print ("error", str(ee), "put")
            raise NoneTypeException
        
    def delete(self, url, data=None):
        self.checkNetwork()
        data = bytes(data, encoding='utf8')  if data is not None else None
        try:
            if open_debug:
                self.logtool.log_print("debug", '[url] ' + url, "delete")
            request, response, result = None, None, None
            request = urllib2.Request(url, headers=self.headers, data=data)
            request.get_method = lambda:'DELETE'   
            response = urllib2.urlopen(request, timeout=10)
            result = response.read()
            data = data.encode() if data is not None else None
            if open_debug:
                self.logtool.log_print("debug", "delete = " + str(result), "delete")
            return result
        except urllib2.URLError as e:
            self.logtool.log_print("error", str(e), "delete")
        except Exception as ee:
            self.logtool.log_print("error", str(ee), "delete")
            raise NoneTypeException

    def anaPostresult(self, result):
        return self.jsontool.anaPostresult(result)

    def serialize(self, class_name, jsoninfo):
        return self.jsontool.serialize(class_name, jsoninfo)

    def deserialize(self, cla):
        return self.jsontool.deserialize(cla)

    def getJsonfromClass(self, cla):        
        return self.jsontool.getJsonfromClass(cla)

if __name__ == "__main__":
    hc = HttpController("192.168.41.208")
    hc.post("https://api-server-corpus1.zhan.com/toefl/filtrate-paper?debug=1")