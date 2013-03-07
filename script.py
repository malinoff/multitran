import argparse
import urllib

from multitran_api import MultitranAPI

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('lang')
    args = parser.parse_args()

    api = MultitranAPI()
    word = urllib.quote(args.word)
    lang = api.langs[args.lang][1]
    print api.translate(word, lang)
