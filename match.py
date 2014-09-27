# This script searches the public project descriptions on BitBucket for a 
# selected set of 10 keywords. The frequency of each keyword is printed to 
# stdout. 

import json, re, requests

jsonDict = {}
url = 'https://api.bitbucket.org/2.0/repositories/'

android = re.compile(".*Android.*", re.IGNORECASE)
arduino = re.compile(".*Arduino.*", re.IGNORECASE)
facebook = re.compile(".*Facebook.*", re.IGNORECASE)
google = re.compile(".*Google.*", re.IGNORECASE)
iphone = re.compile(".*IPhone.*", re.IGNORECASE)
linkedin = re.compile(".*LinkedIn.*", re.IGNORECASE)
pinterest = re.compile(".*Pinterest.*", re.IGNORECASE)
raspPi = re.compile(".*Raspberry.*", re.IGNORECASE)
translate = re.compile(".*translat.*", re.IGNORECASE)
twitter = re.compile(".*Twitter.*", re.IGNORECASE)

tracker = {
  "android": 0,
  "arduino": 0,
  "facebook": 0,
  "google": 0,
  "iphone": 0,
  "linkedin": 0,
  "pinterest": 0,
  "raspPi": 0,
  "translate": 0,
  "twitter": 0
}

#for i in range(0, 100):
while True: 
  r = requests.get(url)
  t = r.text
  jsonDict = json.loads(t)
  for myIterator in jsonDict['values']:
     for key, value in myIterator.iteritems(): 
       if key == 'description': 
         res = android.match(unicode(value))
         if res != None: tracker['android'] = tracker['android'] + 1
         res = arduino.match(unicode(value))
         if res != None: tracker['arduino'] = tracker['arduino'] + 1
         res = facebook.match(unicode(value))
         if res != None: tracker['facebook'] = tracker['facebook'] + 1
         res = google.match(unicode(value))
         if res != None: tracker['google'] = tracker['google'] + 1
         res = iphone.match(unicode(value))
         if res != None: tracker['iphone'] = tracker['iphone'] + 1
         res = linkedin.match(unicode(value))
         if res != None: tracker['linkedin'] = tracker['linkedin'] + 1
         res = pinterest.match(unicode(value))
         if res != None: tracker['pinterest'] = tracker['pinterest'] + 1
         res = raspPi.match(unicode(value))
         if res != None: tracker['raspPi'] = tracker['raspPi'] + 1
         res = translate.match(unicode(value))
         if res != None: tracker['translate'] = tracker['translate'] + 1
         res = twitter.match(unicode(value))
         if res != None: tracker['twitter'] = tracker['twitter'] + 1
  if 'next' not in jsonDict: break
  else: url = jsonDict['next']

for key, value in tracker.iteritems(): 
  print(key+': '+str(value))
