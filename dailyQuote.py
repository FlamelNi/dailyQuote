

import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://www.eduro.com/')
# r.status
# r.data

source = str(r.data)

a = source.find("article")
b = source.find("</p>", a)
a = source.find("<p>", a) + 3

quote = source[a:b]


quote = quote.replace("&#8217;", "'")

a = source.find("author", b)
a = source.find("&#8211;", a) + 8
b = source.find("&nbsp;", a)

author = source[a:b]

print(quote + " -" + author)






