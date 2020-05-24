import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWORD"),
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Sticker_Responses")
mycursor.execute("USE Sticker_Responses")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS responses (IG_Handle VARCHAR(255), Date_Started_Following DATE, First_Name VARCHAR(255), Last_Name VARCHAR(255), Home_State VARCHAR(255), Home_City VARCHAR(255), Aprx_Household_Income VARCHAR(255),  Number_of_Story_Engagements INT, Date_of_Last_Story_View DATE, Date_of_Last_Story_Engagement DATE, Number_of_Story_Swipe_Ups INT, Date_of_Last_Post_Engagement DATE, Number_of_Post_Engagements INT, Number_Post_Likes INT, Number_of_Post_Comments INT, Response_to_Story_Question_Stickers VARCHAR(5000))"
    )


def insertValue(name, response):
  print('HERE')
  sql = "INSERT INTO responses (IG_Handle, Response_to_Story_Question_Stickers) VALUES(%s, %s)"
  val = [
    name, response
  ]

  print(val)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "was inserted.")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
