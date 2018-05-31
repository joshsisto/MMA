from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import time
import re

from ufc_links import *


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
    r = get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    fighter_list = []
    for table_row in soup.select("table.fighter-listing tr"):
        cell_link = table_row.findAll('a')
        for link in cell_link:
            fighter = (str(link).split())
            fighter_list.append(fighter[2])

    fighter_links = []
    for fighter in fighter_list:
        fighter = fighter[6:-2]
        fighter_links.append(f"http://www.ufc.com{fighter}")
    # print(fighter_links)
    # print(len(fighter_links))
    return fighter_links

# get_fighter_list(the_ufc_link)

full_list = []
# with open("ufc_links.txt") as f:
#     content = f.readlines()
#     # print(content)
#     for link in content:
#         full_list.append(get_fighter_list(link))
#         ff = open("fighter_links.txt", "a+")
#         ff.write(str(get_fighter_list(link)))
#         ff.close()
#         # print(link.strip("\n"))
#         print(full_list)
#         time.sleep(5)


test_link = r"http://www.ufc.com/fighter/junior-Albini#"

m = re.search("([^/]+)$", test_link).group(0)
print(m.upper().replace("-", " "))

def get_fighter_stats(url):
    r = get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    fighter_stats = []
    for table_row in soup.select("div.fighter-info tr"):
        fighter_info = table_row.findAll('td')
        for data in fighter_info:
            f_data = (str(data).split())
            fighter_stats.append(f_data)
            # print(f_data)
    # print(fighter_stats)

    for table_row in soup.select("table.fights-table tr"):
        fighter_info_exp = table_row.findAll('td')
        for data in fighter_info_exp:
            f_data = (str(data).split())
            fighter_stats.append(f_data)
    print(fighter_stats)


get_fighter_stats(test_link)

