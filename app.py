import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from python.connections import createDatabaseAndPopulateWithFollowersDateAndTime
from python.main import prepareToRun
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route("/submit/", methods=["POST"])
def submit():
  if request.method == "POST":
    if 'file' in request.files:
      json_file = request.files['file']
      saved_name = os.path.join(
          "/Users/Tanner/code/products/turtlecreeklane/", json_file.filename)
      json_file.save(saved_name)
      createDatabaseAndPopulateWithFollowersDateAndTime(saved_name)
    else:
      print("file not present")
  print("sucess")
  return jsonify(status='200')

@app.route('/stickers/', methods=["POST"])
def stickers():
  if (request.method == "POST" and request.files.getlist('file')):
    uploads = request.files.getlist('file')
    print(request.files)

    for pic in uploads:
      filename = pic.filename.split(".")[0] + '.jpg'
      saved_name = os.path.join("/Users/Tanner/code/products/turtlecreeklane/uncroppedImages/", filename)
      pic.save(saved_name)

      image = Image.open(saved_name)
      rgb_im = image.convert('RGB')
      rgb_im.save(saved_name)

    prepareToRun()
  else:
    print('file not present')
    
  print('success')
  return jsonify(status='200')

  # hello

