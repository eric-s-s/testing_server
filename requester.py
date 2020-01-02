import requests
from requests_toolbelt import MultipartEncoder

filename = "/home/eric.shaw/dr_workspace/datarobot-ai-scala/aiapi/src/it/resources/credit-train-small_20-99-entries.csv"


# with open(filename, 'rb') as data:
#     encoder = MultipartEncoder(fields={'file': (filename, data)})
#
#     headers = {}
#     headers.update({'Content-Type': encoder.content_type, 'Content-Length': '0'})
#
#
#     response = requests.post(
#         "http://localhost:5000/test",
#         headers=headers,
#         data=encoder
#     )

files = {'file': open(filename, 'r')}
requests.post("http://localhost:5000/test", files=files)
