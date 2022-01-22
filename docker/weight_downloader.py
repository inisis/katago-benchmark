import re
import sys
import os.path
import requests
from bs4 import BeautifulSoup


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


url = 'https://katagotraining.org/networks/kata1/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

response = requests.get(url, headers = headers)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all('a', href=re.compile(r"bin\.gz"))
print("all links")

new = 0
for link in links:
    print(link['href'])
    url = link['href']
    filename = url.split('/')[-1]

    if not os.path.exists(filename):
        new += 1
        print('download:',filename)
        download(url, filename)
    else:
        print(filename,'exist')

print('total:', len(links))
print('new: ', new)
print('Done')    
