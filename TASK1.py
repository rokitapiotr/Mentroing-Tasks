"""
File upload and verification Resource: httpbin: https://httpbin.org/
Task: Create a Postman collection for "/post:, which allows file uploads. Then write a python script to upload any file
to httpbin and verify the response
"""
import requests

url = 'https://httpbin.org/post'

files = {'file': ('text.txt', open('text.txt', 'rb'))}

response = requests.post(url, files=files)

if response.status_code == 200:
    print("The file has been uploaded")
    print(response.text)
else:
    print('The file has not been uploaded')
