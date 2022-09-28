from http.client import HTTPConnection
connection = HTTPConnection("www.globo.com ", port=80, timeout=10)
connection.request("HEAD", "/")

response = connection.getresponse()
print(response.getheaders())
