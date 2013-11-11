from django.shortcuts import render_to_response
from django.template import RequestContext
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import feedparser
import urllib2


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

    for entry in feed['entries']:
        dictionary = {}
        dictionary['title'] = entry['title']
        dictionary['link'] = entry['links'][0]['href']
        date_unformated = entry['published']
        dictionary['date'] = datetime.strptime(date_unformated,
                                               "%a, %d %b %Y %H:%M:%S -%f").strftime("%d %b %Y")

        raw_html = entry['summary']

        soup = BeautifulSoup(raw_html)
        
        # highlights
        comments = soup.findAll('div', attrs={'class': 'annInner'})
        dictionary['highlights'] = []
        for comment in comments:
            dictionary['highlights'].append(comment.__str__())

        # tags and user
        paragraphs = soup('p')[-3:]
        if paragraphs[0].ul:
            dictionary['comments'] = paragraphs[0].ul.__str__()
        dictionary['tags_info'] = paragraphs[1].a.__str__()
        dictionary['users_info'] = paragraphs[2].a.__str__()

        # assert False
        # dictionary['raw'] = raw_html

        dictionaries.append(dictionary)

    return dictionaries

