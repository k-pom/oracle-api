from lib import oracle

def get_image_by_name(name):
    if not in_cf(name):
        save_card(name)

    return url_from_cf(name)

def in_cf(name):
    """ Determine if the card is in cloud files """

    return False

def url_from_cf(name):
    """ return the cdn url for the card """

    return False

def save_card(name):
    """ retrieve the image from oracle and push it to cloud files """

    img_url = oracle.get_image(name)
    save_to_cf(name, img_url)

def save_to_cf(name, url):
    """ Given a name and file, save it to cloud files """
    print url
    return False