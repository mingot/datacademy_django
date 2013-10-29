from django.shortcuts import render_to_response
from django.template import RequestContext
from HTMLParser import HTMLParser
import feedparser
import urllib2


class SummaryParser(HTMLParser):
    entries = []

    def handle_starttag(self, tag, attrs):
        pass
    
    def handle_endtag(self, tag):
        pass
    
    def handle_data(self, data):
        self.entries.append(data)


def news_list(request):
    news_dictionaries = construct_rss_dictionary()
    return render_to_response('news/news_list.html',
                              {'news': news_dictionaries},
                              context_instance=RequestContext(request))


def construct_rss_dictionary():
    response = urllib2.urlopen('https://groups.diigo.com/group/datacademy/rss')
    raw_data = response.read()
    feed = feedparser.parse(raw_data)
    dictionaries = []
    parser = SummaryParser()

    for entry in feed['entries']:
        dictionary = {}
        dictionary['title'] = entry['title']
        dictionary['link'] = entry['links'][0]['href']

        raw_html = entry['summary']
        parser.entries = []
        parser.feed(raw_html)
        dictionary['info'] = parser.entries
        dictionary['raw'] = raw_html

        dictionaries.append(dictionary)

    return dictionaries

