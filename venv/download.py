import urllib2
req = urllib2.Request('http://www.python.org/')
#下载19000到20000字节的片段
req.headers['Range'] = 'bytes=%s-%s' % (0, 1024)
f = urllib2.urlopen(req)
pagerange = f.headers.get('Content-Range')
print (pagerange)
bytes (19000-19189/19190)
print (repr(f.read()))
