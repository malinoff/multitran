import urllib
from lxml import etree

from twisted.web.client import getPage
from twisted.internet.defer import Deferred, inlineCallbacks, returnValue

class MultitranAPI(object):


    langs = {'en': ('English', 1),
             'de': ('German', 3),
             'fr': ('French', 4),
             'es': ('Spain', 5),
             'it': ('Italian', 23),
             'nl': ('Dutch', 24),
             'lv': ('Latvian', 27),
             'et': ('Estonian', 26),
             'ja': ('Japanese', 28),
             'af': ('African', 31),
             'eo': ('Esperanto', 34),
             'xal': ('Kalmyk', 35)
             }

    def get_languages(self):
        return dict(map(lambda x: (x[0], x[1][0]), self.langs.items()))

    @inlineCallbacks
    def translate(self, word, lang):
        page = 'http://www.multitran.ru/c/m.exe?CL=1&s=%s&l1=%d'%(word, lang)
        page = yield getPage(page)
        translation = ''
        html = etree.HTML(page)
        trs = html.xpath('//form[@id="translation"]/../table[2]/tr')
        for tr in trs:
            tds = tr.xpath('td')
            for td in tds:
                for elem in td.xpath('descendant::text()'):
                    translation += '%s' % elem.rstrip('\r\n')
            translation += '\n'
        returnValue(translation)
