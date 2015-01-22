from lib import oracle
import cloudfiles
from urllib import urlopen
import os


cf = cloudfiles.get_connection(os.environ.get('CF_USER'), os.environ.get('CF_KEY'))
files = cf.get_container("l5r-cards")

def get_image_by_name(name):
    filename =  name + ".jpg"
    if not (filename in files.list_objects()):
        save_card(name, filename)

    return files[filename].public_uri()


def save_card(name, filename):
    """ retrieve the image from oracle and push it to cloud files """

    image_data = oracle.get_image(name)
    image = files.create_object(filename)
    image.write(image_data)
