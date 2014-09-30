import urllib2
import json
import sys

opener = urllib2.build_opener()


def make_short(url):
    '''
        url: Any long url
    '''
    request = urllib2.Request('https://www.googleapis.com/urlshortener/v1/url',
                              data=json.dumps({"longUrl": url}),
                              headers={'Content-Type': 'application/json'})
    try:
        response = opener.open(request)
    except Exception, e:
        print "Error occurred while making the request."
        print e
    data = (response.read()).split(',')[1]
    short_url = data.split()[1]
    return short_url


def make_long(url):
    '''
        url: Any goo.gl short URL
    '''
    request = urllib2.Request('https://www.googleapis.com/urlshortener\
        /v1/url?shortUrl=%s' % (url))
    try:
        response = opener.open(request)
    except Exception, e:
        print "Error occurred while making the request."
        print e

    data = (response.read()).split(',')[2]
    long_url = data.split()[1]
    return long_url

# TODO
# def analytics(url):
#    pass
