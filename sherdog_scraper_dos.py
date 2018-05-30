import requests
from bs4 import BeautifulSoup

from sherdog_links import *

# We've now imported the two packages that will do the heavy lifting
# for us, reqeusts and BeautifulSoup

# Let's put the URL of the page we want to scrape in a variable
# so that our code down below can be a little cleaner
url_to_scrape = welter_link

# Tell requests to retreive the contents our page (it'll be grabbing
# what you see when you use the View Source feature in your browser)
r = requests.get(url_to_scrape)

# print(r)

# We now have the source of the page, let's ask BeaultifulSoup
# to parse it for us.
soup = BeautifulSoup(r.text, "html.parser")

# print(soup)

# Down below we'll add our inmates to this list
fighter_list = []

# BeautifulSoup provides nice ways to access the data in the parsed
# page. Here, we'll use the select method and pass it a CSS style
# selector to grab all the rows in the table (the rows contain the
# inmate names and ages).

for table_row in soup.select("table.fightfinder_result tr"):
    # Each tr (table row) has three td HTML elements (most people
    # call these table cells) in it (first name, last name, and age)
    cells = table_row.findAll('td')
    cell_link = table_row.findAll('a')

    # Our table has one exception -- a row without any cells.
    # Let's handle that special case here by making sure we
    # have more than zero cells before processing the cells
    if len(cells) > 0:
        # Our first name seems to appear in the second td element
        # that ends up being the cell called 1, since we start
        # counting at 0
        cell_zero = cells[0].text.strip()
        # Our last name is in the first (0 if we start counting
        # at 0 like we do in Python td element we encounter
        cell_one = cells[1].text.strip()
        # Age seems to be in the last td in our row
        cell_two = cells[2].text.strip()

        cell_three = cells[3].text.strip()
        cell_four = cells[4].text.strip()
        # Let's add our inmate to our list in case
        # We do this by adding the values we want to a dictionary, and
        # appending that dictionary to the list we created above
        fighter = {'cell0': cell_zero, 'cell1': cell_one, 'cell2': cell_two, 'cell3': cell_three, 'cell4': cell_four, 'cell_link': cell_link}
        fighter_list.append(fighter)

        # Let's print our table out.
        print("Added {0} {1}, {2}, {3}, {4}, {5}, to the list".format(cell_zero, cell_one, cell_two, cell_three, cell_four, cell_link))

print(fighter_list)
#
# # What if we want to do more than just print out all the names and
# # ages? Maybe we want to filter things a bit. Say, only we want to
# # only print out the inmates with an age between 20 and 30.
#
# # Let's keep track of the number of inmates in the 20s.
# inmates_in_20s_count = 0
#
# # Loop through the list of inmates we built
# for inmate in inmates_list:
# 		# The age we originally received from BeautifulSoup is a
# 		# string. We need it to be a number so that we can compare
# 		# it easily. Let's make it an integer.
# 		age = int(inmate['age'])
#
# 		if age > 19 and age < 31:
# 			# Let's print our table out.
# 			print "{0} {1}, {2} is in the 20 to 30 age range".format(inmate['first_name'], inmate['last_name'], age)
#
# 			# Add one to our inmates in their 20s count
# 			inmates_in_20s_count = inmates_in_20s_count + 1
#
# # How many inmates did we find in the page? Use the len funciton to find out.
# print "Found {0} in the page".format(len(inmates_list))
# print "Found {0} between age 20 and 30 in the page".format(inmates_in_20s_count)