# Log Management Service 
---
## Usage 

All response will be restfull:

```JSON
{
	"date": "2018-07-02T17:54:15.294Z",
	"service_name": "api-gateway",
	"instance_id": "ffd3082fe09d",
	"log_trace": "<log message>"
}
```
---
---
### List All endpoints

**Definition**

GET /report

**Response**

- `200 OK` on success

```JSON
{
	"total_error": "19",
	"details":[
	{
		"api-gateway": "17",
		"instances": [
			{
				"ffd3082fe09d": "11"
			},{
				"ffd3082fe09da": "6"
			}
		]
	},{
		"some-other": "2",
		"instances": [
			{
				"ffd3082fe09d": "2"
			}
		]
	}
	]
}
```

or 

```JSON
[]
```
---

**Definition**

GET /logs

**Response**

- `200 OK` on success

```JSON
[{
    "_id": "5d20fca8e2699aecef3a489f",
    "date": "2018-07-02T17:54:15.294Z",
    "instance_id": "ffd3082fe09d",
    "log_trace": "Sample Log Message",
    "service_name": "api-gateway"
}]
```
---

**Definition**

POST /logs

**Parameters**

- `date` String
- `service_name` String
- `instance_id` String
- `log_trace` String

```JSON
{
	"date": "2018-07-02T17:54:15.294Z",
	"service_name": "api-gateway",
	"instance_id": "ffd3082fe09d",
	"log_trace": "Sample Log Message"
}
```

**Response**

- `201 Created` on success

```JSON
{
    "_id": "5d20fca8e2699aecef3a489f",
    "date": "2018-07-02T17:54:15.294Z",
    "instance_id": "ffd3082fe09d",
    "log_trace": "Sample Log Message",
    "service_name": "api-gateway"
}
```
---

**Definition**

GET / uploader

**Response**

- `200 OK` on success

```HTML
<!doctype html>
<title>Upload New Log File</title>
<h1>Upload New Log File</h1>
<body>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
</body>
```
---

**Definition**

POST / uploader

**Response**

- `302 Found` on success
- Redirects to `/uploads/<FILE_NAME>`

---

**Definition**

GET /uploads/<FILE_NAME>

**Response**

- `201 Created` on success

```JSON
{
    "_id": "5d20fca8e2699aecef3a489f",
    "date": "2018-07-02T17:54:15.294Z",
    "instance_id": "ffd3082fe09d",
    "log_trace": "Sample Log Message",
    "service_name": "api-gateway"
}
```

