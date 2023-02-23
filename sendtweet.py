from credentials  import *
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep

import datetime



scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('pythonsheets-331905-e09db471bfa6.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)



sheet = client.open('pythonTest')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

def tweet_sender():
  column = sheet_instance.col_values(4)
  y = [2,4,56,3,32,43,32]
  # y = open("data2.txt","r",encoding='utf8')
  # y1= y.readlines()
  for x in column :
    try:
     # api.update_status(x)
      print(x)
      sleep(100)
      print("Just tweeted")
      
    except:
      print("ln")
      sleep(10)

# i = 1
# while i < 3:
#  # tweet_sender()
#   print(i)
#   i += 1
# else:
#   print(i)
#   print("i is no longer less than 6")


x1 = datetime.datetime.now()
y1 = datetime.datetime(2021, 11, 25, 20 , 0 ,0)

# date2 = datetime(2017, 5, 16, 8, 21, 10)

# # Difference between two dates
diff = y1-x1

while y1 > x1 :
  print(diff)
  sleep(60)
  
else:
  print("Okay Curre ", x1)
