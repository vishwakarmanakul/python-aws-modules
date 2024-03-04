import  requests
import json
url= 'http://127.0.0.1:8000/student/1'
r= requests.get(url)
print(r)
json_data= r.json()
print(json_data)
