'''
Note:
    -download mysql software and install in your pc
    -download mysql connector and install your pc
    -create set user id and password mysql
    -create database
'''

#Code:
import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123456',
    database='mydb_2022'
    )
if conn.is_connected():
    print("successfull connected ...!")
