# Log Management Service 

This repo is build for demo purposes.

## Assumption:
Environment has many services and each service has many instances. 
Log files manually added to the log management services for this demo.
Authorization and authentication are ignored on this demo. 
DB design and optimization are ignored on this demo. 
All servers use non-ssl ports



## How to run the repo

1.	Clone repo to local computer
1.	docker-compose build
1. 	docker-compose up

Go to http://localhost:3030

Initial deployment has no data. Thus, report will return.

```JSON 
{
  "details": [], 
  "total_error": 0
}
```
Necessary API documentation can be found in:

http://localhost:3030/apidocs

## Arch Design

![Log Management Service Design](https://github.com/roybay/logs_management/blob/master/Log_Mng_Svc_Design.png)

## Improvments

1. 	All servers are running single instance for this demo and need to be configured to provide high availality and scaliblity. 
1. 	All servers from top to buttom need to have SSL communication 
1. 	Error handling is not properly done. 
1. 	Dockerfile need to be redone with proper security 
1. 	Logs manually added to the system either uploading a log file, POST call with JSON for many insert or single insert. However, it need to be done automatically which requires to learn more about the env. It can be done with many ways. 
1. 	Tecnical Specification Documents 
1. 	Arch design documentation 
1.	Functional requirements
1. 	Test cases
1.	Auto test scripts need to be added.



