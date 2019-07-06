import markdown
import os
import sys

from bson.objectid import ObjectId
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

UPLOAD_FOLDER = '/opt/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'log'])


# Create the instance of flask 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MONGO_URI"] = "mongodb://mongo:27017/logdb"
mongo = PyMongo(app)

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

@app.route("/uploads/<path:filename>")
def get_upload(filename):
    return mongo.send_file(filename)

@app.route("/uploads/<path:filename>", methods=["POST"])
def save_upload(filename):
    logdb = mongo.db.logdb

    logdb.save_file(filename, request.files["file"])
    return redirect(url_for("get_upload", filename=filename))

@app.route("/<ObjectId:task_id>")
def show_task(task_id):
    task = mongo.db.tasks.find_one_or_404(task_id)
    return render_template("task.html", task=task)



@app.route("/test")
def index():
    print('README file', file=sys.stderr)
    """Present API Documentation"""
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

    	# Read the content of the API Doc
    	content = markdown_file.read()

    	# Convert to HTML
    	return markdown.markdown(content)