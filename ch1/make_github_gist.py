import json
import requests

BASE_URL = 'http://api.github.com'
LINK_URL = 'http://gist.github.com'
username = 'simodalla'
api_token = '5d682dd1f173ca763261ad0a1eebc098428ff4a9'
# header = {'X-Github-Username': '%s' % username,
#           'Content-Type': 'application/json',
#           'Authorization': 'token %s' % api_token}
# url = '/gists'
# data = {
#     'description': 'demo gist for api',
#     'public': True,
#     'files': {
#         'file1.txt': {
#             'content': 'bla bla bla'
#         }
#     }
# }
# r = requests.post('{}{}'.format(BASE_URL, url),
#                   headers=header,
#                   data=json.dumps(data))
# print(r)
# # print(r.json()['url'])
# print(r.json())
header = {'X-Github-Username': '%s' % username,
          'Content-Type': 'application/json',
          'Authorization': 'token %s' % api_token,
          }
url = "/gists"
data = {
    "description": "the description for this gist",
    "public": True,
    "files": {
        "file1.txt": {
            "content": "String file contents"
        }
    }
}
r = requests.post('%s%s' % (BASE_URL, url),
                  headers=header,
                  data=json.dumps(data))
print r.json()['url']
