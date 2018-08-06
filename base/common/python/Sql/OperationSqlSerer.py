# -*- coding: utf-8 -*-
import pymssql
import os,sys
sys.path.append("..")
from File.ReadConfig import ReadConfig
dbx=ReadConfig('Config.ini')
ip=dbx.getReadSqlSever('ip')
user=dbx.getReadSqlSever('username')
password=dbx.getReadSqlSever('password')
database=dbx.getReadSqlSever('database')
print(ip)
coon=pymssql.connect(ip, user, password,database)
cursor = coon.cursor()
test='''SELECT TOP (1000) [CityId]
      ,[AreaCityId]
      ,[Sort]
  FROM [Zhan_Clue_Center].[dbo].[Zhan_Allot_City_Map]'''
cursor.execute(test)
row = cursor.fetchall()
print(row)
coon.close()
