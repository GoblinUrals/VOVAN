
import re

def domain_name(url):
    w = (re.findall(r'www\.?(\w+)|\//(\w+)|\//(\w+-\w+)', url))
    return (w)

s = ["http://google.co.jp",
     "www.xakep.ru",
      "https://youtube.com",
     "https://fan-numer.com",
      "http://google.com"]

for url in s:
    print(domain_name(url))


# [('', 'google', '')]
# [('xakep', '', '')]
# [('', 'youtube', '')]
# [('', 'fan', '')]
# [('', 'google', '')]


















