# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib

from BeautifulSoup import BeautifulSoup, Tag, NavigableString

def get_title_and_link():
    soup = BeautifulSoup(urllib.urlopen('http://www.chinadaily.com.cn/language_tips/trans/trans_collect.html').read())
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
    soup = BeautifulSoup(urllib.urlopen(url).read())
    div = soup.findAll('div', attrs={'class': 'sanjineiwen'})[0]
    return div.renderContents()
