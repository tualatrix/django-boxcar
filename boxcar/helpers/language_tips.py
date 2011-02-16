# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib

from BeautifulSoup import BeautifulSoup, Tag, NavigableString

def get_title_and_link():
    url = 'http://www.chinadaily.com.cn/language_tips/trans/trans_collect.html'
    soup = BeautifulSoup(urllib.urlopen(url).read())
    tips = soup.findAll('a', attrs={'target': '_blank'})

    for tip in reversed(tips):
        if type(tip.contents[0]) != NavigableString:
            continue
        title = tip.contents[0]
        for k, v in tip.attrs:
            if k == 'href':
                link = v
                if not line.startswith('http://'):
                    link = os.path.join(os.path.dirname(url), link)
                break
        yield title, link

def get_content_from_url(url):
    soup = BeautifulSoup(urllib.urlopen(url).read())
    div = soup.findAll('div', attrs={'class': 'sanjineiwen'})[0]
    return div.renderContents()
