import os, uuid, io, os, os.path, json, glob, shutil
from PIL import Image
import pandas as pd

from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./python/APIKey.json'

client = vision.ImageAnnotatorClient()

def createDatabase(path):
  df = pd.DataFrame({"IG Handle": ["@"], 'Date Started Following': ['-'], 'First Name': ['-'],
                     'Last Name': ['-'], 'Home State': ['-'], 'Home City': ['-'], 'Aprx Household Income': ['-'],
                     'Date of Last Story View': ['-'], 'Date of Last Story Engagement': ['-'], '# of Story Engagements': ['-'],
                     '# of Story Swipe Ups': ['-'], 'Date of Last Post Engagement': ['-'], '# of Post Engagements': ['-'],
                     '# Post Likes': ['-'], '# of Post Comments': ['-'], 'Response to Story Question Stickers': ['See Following columns']
                     })
  datatoexcel = pd.ExcelWriter(path + "/InstagramStickerResponseData.xlsx", engine="xlsxwriter")
  df.to_excel(datatoexcel, sheet_name="sheet1")
  datatoexcel.save()

def populateDatabase(name, stickerQuestion, response, path):
  df = pd.read_excel(path + '/InstagramStickerResponseData.xlsx', index_col=[0])

  foundIGHandle = df[df['IG Handle'].str.contains(name)]
  IGHandlecount = foundIGHandle.count()[-1]

  df2 = pd.DataFrame({"IG Handle": [f"@{name}"], 'Date Started Following': ['-'], 'First Name': ['-'],
                      'Last Name': ['-'], 'Home State': ['-'], 'Home City': ['-'], 'Aprx Household Income': ['-'],
                      'Date of Last Story View': ['-'], 'Date of Last Story Engagement': ['-'], '# of Story Engagements': ['-'],
                      '# of Story Swipe Ups': ['-'], 'Date of Last Post Engagement': ['-'], '# of Post Engagements': ['-'],
                      '# Post Likes': ['-'], '# of Post Comments': ['-'], 'Response to Story Question Stickers': ['->']})
  df2[stickerQuestion] = response
  df = df.append(df2, ignore_index=True)

  datatoexcel = pd.ExcelWriter(path + "/InstagramStickerResponseData.xlsx", engine="xlsxwriter")
  df.to_excel(datatoexcel, sheet_name="sheet1")
  datatoexcel.save()

def createSubImages(picture):
  im = Image.open(picture)

  leftSide = im.crop((0, 180, im.width / 2, (im.height - (.1 * im.height))))
  leftTop = leftSide.crop((0, 0, leftSide.width, leftSide.height / 4))
  leftUpper = leftSide.crop((0, leftSide.height / 4, leftSide.width, (2 * leftSide.height / 4)))
  leftLower = leftSide.crop((0, (leftSide.height / 2), leftSide.width, (3 * leftSide.height / 4)))
  leftBottom = leftSide.crop((0, (leftSide.height - (.97 * (leftSide.height / 4))), leftSide.width, (leftSide.height)))

  rightSide = im.crop((im.width / 2, 180, im.width, im.height - (.1 * im.height)))
  rightTop = rightSide.crop((0, 0, rightSide.width, rightSide.height / 4))
  rightUpper = rightSide.crop((0, rightSide.height / 4, rightSide.width, (2 * rightSide.height / 4)))
  rightLower = rightSide.crop((0, (rightSide.height / 2), rightSide.width, (3 * rightSide.height / 4)))
  rightBottom = rightSide.crop((0, (rightSide.height - (.97 * (rightSide.height / 4))), rightSide.width, (rightSide.height)))

  leftTop.save(f"./croppedImages/{uuid.uuid1()}.jpg")
  leftUpper.save(f"./croppedImages/{uuid.uuid1()}.jpg")
  leftLower.save(f"./croppedImages/{uuid.uuid1()}.jpg")
  leftBottom.save(f"./croppedImages/{uuid.uuid1()}.jpg")

  rightTop.save(f"./croppedImages/{uuid.uuid1()}.jpg")
  rightUpper.save(f"./croppedImages/{uuid.uuid1()}.jpg")
  rightLower.save(f"./croppedImages/{uuid.uuid1()}.jpg")
  rightBottom.save(f"./croppedImages/{uuid.uuid1()}.jpg")

def populate(path):
  count = 0
  for filepath in glob.iglob('./croppedImages/*'):
    count = count + 1

    lengthOfDir = 0
    for name in os.listdir('./croppedImages'):
      lengthOfDir = lengthOfDir + 1

    print(str(round((count/lengthOfDir*100), 2)) + "%" + " Completed" )

    file_name = os.path.abspath(f"{filepath}")

    with io.open(file_name, 'rb') as image_file:
      content = image_file.read()
      image = types.Image(content=content)
      response = client.document_text_detection(image=image)
      text = response.text_annotations
      username = text[0].description.split('\n')[0]
      textBody = text[0].description.split('\n')[1:]
      newText = str("".join(textBody))
      newTextWithoutReply = newText.split('Reply')[0]

      if (os.path.exists(path + '/InstagramStickerResponseData.xlsx') == False):
        createDatabase(path)

        print('the database exists')
      populateDatabase(username, 'Add Question', newTextWithoutReply, path)

def clearCache(folder):
  if (folder == "cropped"):
    path = './croppedImages'
  elif (folder == "uncropped"):
    path = './uncroppedImages'
    
  for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    try:
      if (os.path.isfile(file_path) or os.path.islink(file_path)):
        os.unlink(file_path)
      elif (os.path.isdir(file_path)):
        shutil.rmtree(file_path)
    except Exception as e:
      print('Failed to delete %s. Reason: %s' % (file_path, e))

def prepareToRun(path):
  print(path)
  for filename in os.listdir('./uncroppedImages'):
    image_file = os.path.join('./uncroppedImages/', filename)
    createSubImages(f"{image_file}")
  
  populate(path)
  clearCache('cropped')
  clearCache('uncropped')

