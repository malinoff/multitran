import argparse
import urllib

from twisted.internet import reactor
from twisted.internet import defer

from multitran_api import MultitranAPI

@defer.inlineCallbacks
def translate(word, lang):
    result = yield api.translate(word, lang)
    print result
    reactor.stop()


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('lang')
    args = parser.parse_args()

    api = MultitranAPI()
    word = urllib.quote(args.word)
    lang = api.langs[args.lang][1]
    translate(word, lang)
    reactor.run()
