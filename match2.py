# This script searches BitBucket for all projects containing the word "Google"
# and stores those descriptions in a file. 

import codecs, json, re, requests
from datetime import datetime

print('Program begins at '+str(datetime.now()))

url = 'https://api.bitbucket.org/2.0/repositories/'

google = re.compile(".*Google.*", re.IGNORECASE)

f = codecs.open('descriptions_google.txt', 'w', 'utf-8')

#for i in range(0, 100): 
while True: 
  r = requests.get(url)
  t = r.text
  jsonDict = json.loads(t)
  for myIterator in jsonDict['values']:
     for key, value in myIterator.iteritems(): 
       if key == 'description': 
         res = google.match(unicode(value))
         if res != None: f.write(unicode(value)) 
  if 'next' not in jsonDict: break
  else: url = jsonDict['next']

f.close()

print('Program completes at '+str(datetime.now()))

