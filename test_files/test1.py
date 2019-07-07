import os
import sys
import json


filepath = '/Users/rbahian/Desktop/repos/personal/Log_Management/logs_management/test_files/log2.txt'  

def split_line(log_file):
    with open(log_file, "r") as logs:
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
			print_json(jsonObject)
			print("-----------")

def print_json(jsonObject):
	jsonString = json.dumps(jsonObject)
	print(jsonString)


split_line(filepath)
