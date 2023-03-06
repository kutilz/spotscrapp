import os
import telebot
token="6231566055:AAGeO-mmoLBcqBk7sYnFhamrH8cGPjY4lTE"
ya=True
while ya:
    q=input("2\n\n\n")
    if q=="aa":
        ya=False
    os.system("scrapy crawl spotscrap")
print("selesai")