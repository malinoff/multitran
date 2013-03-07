import argparse
import urllib

from twisted.internet import reactor
from twisted.web.client import getPage

from multitran_api import MultitranAPI

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('lang')
    args = parser.parse_args()

    api = MultitranAPI()
    word = urllib.quote(args.word)
    lang = api.langs[args.lang][1]
    page = 'http://www.multitran.ru/c/m.exe?CL=1&s=%s&l1=%d'%(word, lang)

    def cb(page):
        print api.parse_page(page)
        reactor.stop()

    getPage(page).addCallbacks(callback=cb,
                               errback=lambda x: reactor.stop())
    reactor.run()
