import  urllib2
import json
url="any url to go in :p"
if __name__ == "__main__":
    req=urllib2.Request("Url")
    opener=urllib2.build_opener()
    f=opener.open(req)
    json=json.load(f)