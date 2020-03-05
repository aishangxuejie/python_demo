#post请求提交用户信息到服务器
import urllib.request
import urllib.parse
import json

url='http://192.168.100.21:9001/his/dwd/gsbxLkb7/aduitGsbxLkb7.html'

header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
# values = {
#     'from': 'zh',
#     'to': 'en',
#     'query': '',
#     'transtype': 'translang',
#     'simple_means_flag': '3'
# }
values = {'base64':'5Y2V5L2N56uv5a6h5om55rWL6K+VMSzpmYjotoUxLOmZiOi2hSwxMzAyMDE0ODQ0OTI1LDE1NzQ3NTE1NjIyNzY='}
data = urllib.parse.urlencode(values).encode('utf-8')
request = urllib.request.Request(url, data, header_dict)
html = urllib.request.urlopen(request).read().decode('utf-8')
js = json.dumps(html)
print(html)
print(js)