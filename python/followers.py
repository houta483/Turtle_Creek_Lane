import pyautogui, re, math
from random import randint
import pandas as pd
import tkinter as tk

def makeAllDataAvaliable(numberOfFollowers):
  pyautogui.click(670, 460, button='left')
  pyautogui.sleep(randint(1, 2))

  pyautogui.click(750, 650, button='left')
  pyautogui.sleep(randint(1, 2))

  pyautogui.scroll(-5)

  for x in range(math.ceil(int(numberOfFollowers-30)/10)):
    pyautogui.sleep(randint(1, 2))
    pyautogui.click(705, 820, button='left')
    pyautogui.scroll(-5)

def copyAndPasteFollowers():
  pyautogui.click(705, 820, button='left')
  pyautogui.sleep(.5)
  pyautogui.hotkey('command', 'tab')
  pyautogui.sleep(1)
  pyautogui.hotkey('command', 'a')
  pyautogui.sleep(1)
  pyautogui.hotkey('command', 'c')
  pyautogui.sleep(.5)
  pyautogui.hotkey('command', 'tab')
  pyautogui.sleep(.5)
  pyautogui.hotkey('command', ';')
  pyautogui.sleep(.5)

def setFollowersVariableAndSaveToExcel():
  root = tk.Tk()
  root.withdraw()

  followers = f"{root.clipboard_get()}"
  followers = f"{followers}"
  followers = followers.split()

  df = pd.DataFrame({"IG Handle": ["---"], 'Date Started Following': ['-'], 'First Name': ['-'],
                    'Last Name': ['-'], 'Home State': ['-'], 'Home City': ['-'], 'Aprx Household Income': ['-'],
                    'Date of Last Story View': ['-'], 'Date of Last Story Engagement': ['-'], '# of Story Engagements': ['-'],
                    '# of Story Swipe Ups': ['-'], 'Date of Last Post Engagement': ['-'], '# of Post Engagements': ['-'],
                    '# Post Likes': ['-'], '# of Post Comments': ['-'], 'Response to Story Question Stickers': ['->']})

  for index, follower in enumerate(followers):
    df1 = pd.DataFrame({"IG Handle": [followers[index]]})
    df = df.append(df1, ignore_index=True)

  datatoexcel = pd.ExcelWriter("../database/turtlecreeklane/InstagramFollowerData.xlsx", engine="xlsxwriter")
  df.to_excel(datatoexcel, sheet_name="sheet1")
  datatoexcel.save()

# copyAndPasteFollowers()
# setFollowersVariableAndSaveToExcel()
