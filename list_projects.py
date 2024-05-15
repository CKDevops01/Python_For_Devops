# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://chaitanyakharche51.atlassian.net/rest/api/3/project"

API_TOKEN="enter api-token"

auth = HTTPBasicAuth("enter valid emailid of jira account", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#output = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
output = json.loads(response.text)
for i in range(len(output)):

  name = output[i]["name"]

  print(name)
