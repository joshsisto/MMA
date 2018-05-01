from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from sherdog_links import *

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


simple_get(welter_link)

def get_all_html(url):
    """
    Get all HTML data
    """

    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        return print(html)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

# get_all_html(welter_link)

def get_fighters(url):
    """
    Get all HTML data
    """

    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        html_tr = html.find_all('tr')
        html_td = html.find_all('td')
        # for fighter in html.find_all('div', class_ = 'odd')
        # print(html_tr)
        # print(html_td)
        print(len(html_tr))
        # print(type(html_td))
    else:

        # Raise an exception if we failed to get any data from the url
        raise Exception('Error retrieving contents at {}'.format(url))


    # for line in html_tr:
    #     print(line)

    for num in range(len(html_tr)):
        for line in html_tr[num]:
            print(line)


get_fighters(heavy_link)





