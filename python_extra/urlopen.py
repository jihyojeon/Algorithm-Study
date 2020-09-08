from urllib.request import urlopen

url = 'http://www.image-net.org/index'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)