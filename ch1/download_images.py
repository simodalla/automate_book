from bs4 import BeautifulSoup
import re
import urllib2
import os

# Download parameters
image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(movie)

header = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)),
                     "lxml")

images = [a['src'] for a
          in soup.find_all('img', {'src': re.compile('gstatic.com')})][:5]
for img in images:
    print("Image source: {}".format(img))
    raw_img = urllib2.urlopen(img).read()
    cntr = len([i for i in os.listdir('images') if image_type in i]) + 1
    with open('images/{}_{}.jpg'.format(image_type, str(cntr)), 'wb') as f:
        f.write(raw_img)
