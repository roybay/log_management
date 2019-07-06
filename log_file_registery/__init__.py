import markdown
import os
import sys

from bson.objectid import ObjectId
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from werkzeug import secure_filename

UPLOAD_FOLDER = '/opt/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'log'])


# Create the instance of flask 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MONGO_URI"] = "mongodb://mongo:27017/logdb"
mongo = PyMongo(app)

# Rest API Documentation
@app.route("/apidocs")
def index():
    print('README file', file=sys.stderr)
    """Present API Documentation"""
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

      # Read the content of the API Doc
      content = markdown_file.read()

      # Convert to HTML
      return markdown.markdown(content)

# Log File Uploader
@app.route("/uploader")
def uploader():
    print('UPLOADER file', file=sys.stderr)
    """Present API Documentation"""
    with open(os.path.dirname(app.root_path) + '/upload.html', 'r') as markdown_file:

      # Read the content of the API Doc
      content = markdown_file.read()

      # Convert to HTML
      return markdown.markdown(content)


# Add Log via JSON object
@app.route('/logs', methods=['POST'])
def add_logs():
  logdb = mongo.db.logdb
  
  date = request.json['date']
  service_name = request.json['service_name']
  instance_id = request.json['instance_id']
  log_trace = request.json['log_trace']

  log_id = logdb.insert({'date': date, 'service_name': service_name, 'instance_id': instance_id, 'log_trace': log_trace})
  #new_log = logdb.find({ "_id": "5d20f7e24c1a75a0195f52b6" })
  new_log = logdb.find_one({'_id': ObjectId(log_id)})
  output = {'_id' : str(new_log['_id']), 'date' : new_log['date'], 'service_name' : new_log['service_name'], 'instance_id' : new_log['instance_id'], 'log_trace' : new_log['log_trace']}
  #output = { 'service_name' : new_log['service_name'], 'instance_id' : new_log['instance_id'], 'log_trace' : new_log['log_trace']}

  return jsonify(output)
  #return str(log_id)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
    
if __name__ == '__main__':
   app.run(debug = True)








