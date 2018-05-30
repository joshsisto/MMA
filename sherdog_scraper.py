from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from sherdog_links import *


#https://realpython.com/python-web-scraping-practical-introduction/
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


# simple_get(catch_link)

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
    Scrape fighter data
    """

    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        html_tr = html.find_all('tr')
        # html_td = html.find_all('td')
        # for fighter in html.find_all('div', class_ = 'odd')
        # print(html_tr)
        # print(html_td)
        print(len(html_tr))
        # print(type(html_td))
    else:

        # Raise an exception if we failed to get any data from the url
        raise Exception('Error retrieving contents at {}'.format(url))

    print(html_tr[3])
    print(type(html_tr[3]))

#get_fighters(heavy_link)

def get_fighter_list(url):
    url_to_scrape = url
    r = get(url_to_scrape)
    # print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)
    fighter_list = []
    for table_row in soup.select("table.fightfinder_result tr"):
        cells = table_row.findAll('td')
        cell_link = table_row.findAll('a')

        if len(cells) > 0:
            cell_one = cells[1].text.strip()
            fighter = [cell_one, cell_link]
            fighter_list.append(fighter)

            print("Added {0}, {1}, to the list".format(cell_one, cell_link))


get_fighter_list(l_heavy_link)

