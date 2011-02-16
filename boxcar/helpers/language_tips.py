# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from BeautifulSoup import BeautifulSoup, Tag, NavigableString

def get_title_and_link():
    soup = BeautifulSoup(open('/Users/tualatrix/.virtualenvs/ttime/src/boxcar/boxcar/helpers/trans_collect.html').read())
    tips = soup.findAll('a', attrs={'target': '_blank'})

    for tip in reversed(tips):
        if type(tip.contents[0]) != NavigableString:
            continue
        title = tip.contents[0]
        for k, v in tip.attrs:
            if k == 'href':
                link = v
                break
        yield title, link

def get_content_from_url(url):
    soup = BeautifulSoup(open('/Users/tualatrix/.virtualenvs/ttime/src/boxcar/boxcar/helpers/content_12022973.html').read())
    div = soup.findAll('div', attrs={'class': 'sanjineiwen'})[0]
    return div.renderContents()
