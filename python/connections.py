import json, pyautogui, re, math, os
from random import randint
import pandas as pd
import tkinter as tk
from datetime import datetime
from dateutil.parser import parse

# ALL THE POTENTIAL DATA WE CAN GET FROM CONNECTIONS

# with open('/Users/Tanner/code/products/Instagram/data.json') as f:
#   data = json.load(f)

# rawFollowers = data['followers']
# prettyFollowers = json.dumps(rawFollowers, indent=4)

# rawBlockedUsers = data['blocked_users']
# prettyFollowers = json.dumps(rawBlockedUsers, indent=4)

# rawRestricedUsers = data['restricted_users']
# prettyFollowers = json.dumps(rawRestricedUsers, indent=4)

# rawFollowRequestsSent = data['follow_requests_sent']
# prettyFollowers = json.dumps(rawFollowRequestsSent, indent=4)

# rawFolloring = data['following']
# prettyFollowers = json.dumps(rawFolloring, indent=4)

# rawFollowingHashtags = data['following_hashtags']
# prettyFollowers = json.dumps(rawFollowingHashtags, indent=4)

# rawWhitelistedForSponsorTaggingBy = data['whitelisted_for_sponsor_tagging_by']
# prettyFollowers = json.dumps(rawWhitelistedForSponsorTaggingBy, indent=4)

# rawDismissedSuggestedUSers = data['dismissed_suggested_users']
# prettyFollowers = json.dumps(rawDismissedSuggestedUSers, indent=4)

def createDatabaseAndPopulateWithFollowersDateAndTime(json_file, path):
  with open(json_file) as f:
    data = json.load(f)

  rawFollowers = data['followers']

  df = pd.DataFrame({"IG Handle": ["---"], 'Date Started Following': ['-'], 'Time Started Following': ['-'], 'First Name': ['-'],
                     'Last Name': ['-'], 'Home State': ['-'], 'Home City': ['-'], 'Aprx Household Income': ['-'],
                     'Date of Last Story View': ['-'], 'Date of Last Story Engagement': ['-'], '# of Story Engagements': ['-'],
                     '# of Story Swipe Ups': ['-'], 'Date of Last Post Engagement': ['-'], '# of Post Engagements': ['-'],
                     '# Post Likes': ['-'], '# of Post Comments': ['-'], 'Response to Story Question Stickers': ['->']})

  for index in enumerate(rawFollowers.items()):

    dateTime = str(index[1][1])
    date = dateTime.split("T")[0]
    date = date.split('-')
    date = f"{date[1]}-{date[2]}-{date[0]}"
    finalDate = datetime.strptime(date, '%m-%d-%Y').date()

    time = dateTime.split("T")[1]
    finalTime = time.split("+")[0]

    df1 = pd.DataFrame({
        "IG Handle": [index[1][0]],
        'Date Started Following': [finalDate],
        'Time Started Following': [finalTime]
    })
    df = df.append(df1, ignore_index=True)

    datatoexcel = pd.ExcelWriter(path + "/InstagramFollowerData.xlsx", engine="xlsxwriter")
    df.to_excel(datatoexcel, sheet_name="sheet1")
    datatoexcel.save()


if __name__ =="__main__":
  if (os.path.exists('/Users/Tanner/code/products/turtlecreeklane/database/InstagramFollowerData.xlsx') == False):
    createDatabaseAndPopulateWithFollowersDateAndTime()

