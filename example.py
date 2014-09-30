import earl
import sys

help_text = '''Usage
-----
python example.py <function> <url>
-----
fucntions: make_short, make_long
url: The url to operate on.
'''

if len(sys.argv) == 1:
    print help_text
    sys.exit()
elif len(sys.argv) == 3:
    args = list(sys.argv)
    args.remove(args[0])
    func = args[0]
    url = args[1]
    if func == 'make_long':
        result = earl.make_long(url)
        print result
    elif func == 'make_short':
        result = earl.make_short(url)
        print result
    else:
        print help_text
else:
    print help_text
