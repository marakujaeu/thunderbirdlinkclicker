import mailbox
from urlextract import URLExtract
import requests

mbox = mailbox.mbox('INBOX')
urlslist=[]
extractor = URLExtract()


for msg in mbox:
        body = msg.get_payload()
        body = str(body)
        urls = extractor.find_urls(body)
        for url in urls:
            if "http" not in url:
                url = 'http://' + url
            urlslist.append(url)
            r = requests.get(url)

print("Clicked links:")
print(urlslist)