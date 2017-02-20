import urllib

from bs4 import BeautifulSoup
from threading import Thread

# Location of restaurnts
home_url = 'https://www.yelp.com'
find_what = 'Restaurants'
location = 'Bologna'

# Get all restaurants tha match the search criteria
search_url = 'https://www.yelp.com/search?find_desc={}&find_loc={}'.format(
    find_what, location)
# print(search_url)
s_html = urllib.urlopen(search_url).read()
# print(s_html)
soup_s = BeautifulSoup(s_html, "lxml")

# Get URLs of top 10 Restaurants in London
s_urls = soup_s.select('.biz-name')[:10]
# print(s_urls)
url = ['{}{}'.format(home_url, s_urls[u]['href']) for u in range(len(s_urls))]
# print(url)


def scrape(ur):
    """function the will fo actual scraping job"""
    html = urllib.urlopen(ur).read()
    soup = BeautifulSoup(html, 'lxml')

    title = soup.select('.biz-page-title')
    saddress = soup.select('.street-address')
    phone = soup.select('.biz-phone')

    if title:
        print('Title: {}'.format(title[0].getText().strip()))
    if saddress:
        print('Street Address: {}'.format(saddress[0].getText().strip()))
    if phone:
        print('Phone: {}'.format(phone[0].getText().strip()))
    print("-------------------------------------")


if __name__ == '__main__':
    threadlist = []
    i = 0
    while i < len(url):
        t = Thread(target=scrape, args=(url[i],))
        t.start()
        threadlist.append(t)
        i += 1

    [t.join() for t in threadlist]