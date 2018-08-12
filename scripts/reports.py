import requests
import itertools
import re

REPORT_URL = 'http://chicagolrb.org/reports?page={}'

for page in itertools.count(0):
    url = REPORT_URL.format(page)
    response = requests.get(url)
    report_urls = re.findall(r'http.*?\.pdf', response.text)
    if not report_urls:
        break
    for report_url in report_urls:
        print(report_url)
