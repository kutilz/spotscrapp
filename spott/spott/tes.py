import os
import telebot
import mysql.connector
from mysql.connector import errorcode
token="6231566055:AAGeO-mmoLBcqBk7sYnFhamrH8cGPjY4lTE"

mydb=mysql.connector.connect(
    host="sql12.freemysqlhosting.net",
    user="sql12603049",
    passwd="qUdAy2skRe",
    database="sql12603049"
)

# ya=True
# while ya:
#     q=input("2\n\n\n")
#     if q=="aa":
#         ya=False
#     os.system("scrapy crawl spotscrap")
# print("selesai")