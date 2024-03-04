api='https://jsonplaceholder.typicode.com/posts'
from collections import Counter
import random
import requests
import json
res = requests.get(api)
response = json.loads(res.text)
# print(response)
for item in random.sample(response,10):
    print(item)