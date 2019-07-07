import markdown
import os
import sys
import logging


from bson.objectid import ObjectId
from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory
from flask import render_template
from flask_pymongo import PyMongo
from werkzeug import secure_filename

UPLOAD_FOLDER = '/opt/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'log'])

# Create the instance of flask 
app = Flask(__name__)
# Upload File Config
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# DB Connection 
app.config["MONGO_URI"] = "mongodb://mongo:27017/logdb"
mongo = PyMongo(app)

# Rest API Documentation
@app.route("/apidocs")
def index():
    print('RestAPI Documentation', file=sys.stderr)
    """Present API Documentation"""
    with open(os.path.dirname(app.root_path) + '/APIDocs.md', 'r') as markdown_file:

      # Read the content of the API Doc
      content = markdown_file.read()

      # Convert to HTML
      return markdown.markdown(content)

# Get Logs via JSON object
@app.route('/logs', methods=['GET'])
def get_logs():
  logdb = mongo.db.logdb
  
  all_log = list(logdb.find())
  return jsonify(all_log)
  
# Add Log via JSON object
@app.route('/log', methods=['POST'])
def set_log():
  logdb = mongo.db.logdb
  
  date = request.json['date']
  service_name = request.json['service_name']
  instance_id = request.json['instance_id']
  log_trace = request.json['log_trace']

  log_id = logdb.insert({'_id': str(ObjectId()),'date': date, 'service_name': service_name, 'instance_id': instance_id, 'log_trace': log_trace})
  new_log = logdb.find_one({'_id': log_id})
  output = {'_id' : new_log['_id'], 'date' : new_log['date'], 'service_name' : new_log['service_name'], 'instance_id' : new_log['instance_id'], 'log_trace' : new_log['log_trace']}
  
  return jsonify(output)
  
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('uploader.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/log_files', methods=['GET', 'POST'])
def insert_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return insert_file_data(file.filename)
    return render_template('uploader.html')

def insert_file_data(logfile):
    filename = UPLOAD_FOLDER + '/' + logfile
    jsonList=[]
    with open(filename, "r") as logs:
      for line in logs:
        tmp = line.split(" ", 1)
        date = tmp[0]
        tmp = tmp[1].split("[", 1)
        tmp = tmp[1].split(" ", 1)
        service_name = tmp[0]
        tmp = tmp[1].split("]", 1)
        instance_id = tmp[0]
        tmp = tmp[1].split(": ", 1)
        log_trace = tmp[1]
        jsonObject = { 'date': date, 'service_name': service_name, 'instance_id': instance_id, 'log_trace': log_trace }
        jsonList.append(jsonObject)
    return jsonify({'data': jsonList})


