import bs4

with open('python.html') as myfile:
    soup = bs4.BeautifulSoup(myfile, "lxml")
    print("BeautifulSoup Object: {}".format(type(soup)))

    # Find elements by tags
    print(soup.find_all('a'))
    print(soup.find_all('strong'))

    # Find elements by id
    print(soup.find('div', {'id': 'inventor'}))
    print(soup.select('#inventor'))

    # Find elements by css selectors
    print(soup.select('.wow'))

    print("*******************")

    print("Facebook URL:", soup.find_all('a')[0]['href'])
    print("Inventor:", soup.find('div', {'id': 'inventor'}).text)
    print("Span content:", soup.select('span')[0].getText())