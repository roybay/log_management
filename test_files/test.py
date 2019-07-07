import os
import sys


filepath = 'log2.txt'  
with open(filepath, "r") as log_file:
	for line in log_file:
		tmp = line.split(" ", 1)
		date = tmp[0]
		tmp = tmp[1].split("[", 1)
		tmp = tmp[1].split(" ", 1)
		service_name = tmp[0]
		tmp = tmp[1].split("]", 1)
		instance_id = tmp[0]
		log_trace = tmp[1]
		print("Line : " + line)
		print("Date : " + date)
		print("service_name : " + service_name)
		print("instance_id : " + instance_id)
		print("log_trace : " + log_trace)
		print("=========")



def index():
    """Present API Documentation"""
    with open(os.path.dirname(app.root_path) + '/APIDocs.md', 'r') as markdown_file:

      	# Read the content of the API Doc
      	content = markdown_file.read()

      	# Convert to HTML
      	return markdown.markdown(content)



