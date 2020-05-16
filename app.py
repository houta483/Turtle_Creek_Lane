import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from python.connections import createDatabaseAndPopulateWithFollowersDateAndTime
from python.main import prepareToRun
from PIL import Image

# Flask is  Running on http://127.0.0.1:5000/ 

app = Flask(__name__)
CORS(app)

@app.route("/submit/", methods=["POST"])
def submit():
  ## this method runs when submits.
  if request.method == "POST":
    if 'file' in request.files:
      json_file = request.files['file']
      ## we can just provicde a path with the body request.
      path = request.args.get('path', 'none')
      print(path)
      saved_name = os.path.join(path, json_file.filename)
      json_file.save(saved_name)
      createDatabaseAndPopulateWithFollowersDateAndTime(saved_name, path)
    else:
      print("file not present")
  print("sucess")
  return jsonify(status='200')

@app.route('/stickers/', methods=["POST"])
def stickers():
  if (request.method == "POST" and request.files.getlist('file')):
    uploads = request.files.getlist('file')

    # where we want to save the output
    path = request.args.get('path', 'none')
    print(path)

    for pic in uploads:
      # Save the pictures to the uncropped images cache
      filename = pic.filename.split(".")[0] + '.jpg'
      saved_name = os.path.join("./uncroppedImages/", filename)
      pic.save(saved_name)

      # save to correct format 
      image = Image.open(saved_name)
      rgb_im = image.convert('RGB')
      rgb_im.save(saved_name)

    prepareToRun(path)
  else:
    print('file not present')
    
  print('success')
  return jsonify(status='200')

