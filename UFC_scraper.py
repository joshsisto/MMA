from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import re
import os


def get_fighter_list(url):
    """
    Scrape fighter href links from UFC
    :param url:
    :return:
    """
    r = get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    fighter_list = []
    for table_row in soup.select("table.fighter-listing tr"):
        cell_link = table_row.findAll('a')
        for link in cell_link:
            fighter_list.append(link.get('href'))
    fighter_links = []
    for fighter in fighter_list:
        fighter_links.append(f"http://www.ufc.com{fighter}")
    print(fighter_links)
    return fighter_links

# get_fighter_list(r"http://www.ufc.com/fighter/Weight_Class/filterFighters?offset=0&max=20&sort=lastName&order=asc&weightClass=&fighterFilter=Current")


def scrape_all_fighters():
    """
    #Open ufc_links.txt and go through all pages containing fighters and scrape fighter links using get_fighter_list()
    ppend fighter links to fighter_links.txt (You should now have all active ufc fighters)
    :return:
    """
    full_list = []
    with open("ufc_links.txt") as f:
        content = f.readlines()
        # print(content)
        for link in content:
            full_list.append(get_fighter_list(link))
            ff = open("fighter_links.txt", "a+")
            ff.write(str(get_fighter_list(link)))
            ff.close()
            # print(link.strip("\n"))
            print(full_list)
            time.sleep(5)




test_link = r"http://www.ufc.com/fighter/Rafael-Dos-Anjos"

def extract_name(url):
    """
    Grab the end of fighter link to extract name using regex
    :param url:
    :return:
    """
    m = re.search("([^/]+)$", url).group(0)
    print(m.upper().replace("-", " "))

extract_name(test_link)


def get_fighter_stats(url):
    r = get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    fighter_stats = []
    # for table_row in soup.select("div.fighter-info tr"):
    #     fighter_info = table_row.findAll('td')
    #     for data in fighter_info:
    #         f_data = (str(data).strip('\n\t'))
    #         fighter_stats.append(f_data)
            # print(f_data)
    # print(fighter_stats)

    table_data = soup.select('table.fights-table')
    print(table_data)
    # for table_row in soup.select("table.fights-table td"):
    #     fighter_info_exp = table_row.find(id='fighter-from')
    #     print(fighter_info_exp)
        # for data in fighter_info_exp:
        #     f_data = (str(data).strip('\n\t'))
        #     fighter_stats.append(data)
    # print(fighter_stats)

# get_fighter_stats(test_link)





#https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251
#https://github.com/mozilla/geckodriver/releases
#C:\Windows\System32
url = r"http://www.ufc.com/fighter/Colby-Covington"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

#After opening the url above, Selenium clicks the expand button
# python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
# python_button.click() #click fhsu link


