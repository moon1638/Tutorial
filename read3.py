import urllib2,json,base64
accesstoken="YSJ7CVF2SW02XYDQULMV"
institution="10007772"
course="U56119"
page=0
url="https://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
    institution,
    course
    )
request=urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('/n','')
    )
response=urllib2.urlopen(request)
data=json.load(response)
#a = data[6]
#x = a["Details"]
#c = x[1]
#c=x[4]
#d = c["Value"]
#print d
#print json.dumps(data,indent=2)
a=data[5]["Details"]
x=a[0]["Value"]
print x
