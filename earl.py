import urllib2
import json
import sys

help_text = '''Usage
-----
python earl.py <function> <url>
-----
fucntions: make_short, make_long
url: The url to operate on.
'''
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
        sys.exit()
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
        sys.exit()

    data = (response.read()).split(',')[2]
    long_url = data.split()[1]
    return long_url

if len(sys.argv) == 1:
    print help_text
    sys.exit()
elif len(sys.argv) == 3:
    args = list(sys.argv)
    args.remove(args[0])
    func = args[0]
    url = args[1]
    if func == 'make_long':
        result = make_long(url)
        print result
    elif func == 'make_short':
        result = make_short(url)
        print result
    else:
        print help_text
else:
    print help_text
