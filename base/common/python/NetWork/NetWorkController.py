import os, sys, time

from NetWork.FtpTool import FtpTool
from NetWork.SshTool import SshTool
from NetWork.SftpTool import SftpTool

class NetWorkController(object):
    def __init__(self):
        self.class_name = "NetWorkController"


    def __str__(self):
        return self.class_name

    def getProtocol(self, protocol, *args):
        if protocol == "ftp":
            return FtpTool(*args)
        if protocol == "ssh":
            return SshTool(*args)
        if protocol == "sftp":
            return SftpTool(*args)


if __name__ == "__main__":
    nwc = NetWorkController()
    nwc = NetWorkController.getProtocol("ftp", "", "", )