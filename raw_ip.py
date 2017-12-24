import time
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://ip.42.pl/raw')
localtime = time.asctime( time.localtime(time.time()) )
print (r.data.decode('utf-8'),localtime)
