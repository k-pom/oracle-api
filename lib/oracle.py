from urllib import urlopen, urlencode
import re

BASE_URL = "http://imperialassembly.com/oracle/"

def get_image(name):
    card_id, hash_id = dosearch(name)
    return urlopen(BASE_URL + docard(card_id, hash_id)).read()

def dosearch(name):
    encodeddata = urlencode({'search_13': name})
    data = urlopen(BASE_URL + "dosearch", encodeddata).read()
    regex = re.compile("{cardid: \"([0-9]*)\", hashid: \"([a-z0-9]*)\"")
    r = regex.search(data)

    # If we didn't get a single card back, return the most recent copy
    if r is None:
        regex = re.compile("#cardid=([0-9]*),#hashid=([a-z0-9]*),")
        return regex.findall(data)[-1]
    return r.groups()

def docard(card_id, hash_id):

    encodeddata = urlencode({'cardid': card_id, 'hashid': hash_id})
    data = urlopen(BASE_URL + "docard", encodeddata).read()

    regex = re.compile("\"(showimage?[^\"]*)\">")
    return regex.findall(data)[0]

