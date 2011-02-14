# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(open('test.html').read())
tips = soup.findAll('td', attrs={'class': 'erjbiaoti'})

for tip in tips:
    print tip.contents[0].contents[0]
    for k, v in tip.contents[0].attrs:
        if k == 'href':
            print v
            break
