#proj2.py
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
url1 = 'http://nytimes.com'
html1 = urllib.request.urlopen(url1).read()
soup1 = BeautifulSoup(html1, 'html.parser')
for story_heading in soup1.find_all(class_ = 'story-heading', limit = 10):
    if story_heading.a:
        print(story_heading.a.text.replace('\n', ' ').strip())
    else:
        print(story_heading.contents[0].strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
url2 = 'https://www.michigandaily.com'
html2 = urllib.request.urlopen(url2).read()
soup2 = BeautifulSoup(html2, 'html.parser')
for most_read in soup2.find_all(class_ = 'panel-pane pane-mostread'):
    for li in most_read.div.div.ol.find_all('li'):
        if li.a:
            print(li.a.text.replace('\n', ' ').strip())
        else:
            print(li.contents[0].strip())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
url3 = 'http://newmantaylor.com/gallery.html'
html3 = urllib.request.urlopen(url3).read()
soup3 = BeautifulSoup(html3, 'html.parser')
for img in soup3.find_all('img'):
    if 'alt' in img.attrs:
        print(img['alt'])
    else:
        print('No alternative text provided!!')

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
url4 = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
html4 = urllib.request.urlopen(url4).read()
soup4 = BeautifulSoup(html4, 'html.parser')
count = 1
while True:
    for a in soup4.find_all('a', text = 'Contact Details'):
        contact_url = urllib.parse.urljoin(url4, a['href'])
        contact_html = urllib.request.urlopen(contact_url).read()
        contact_soup = BeautifulSoup(contact_html, 'html.parser')
        for div in contact_soup.find_all('div', class_ = 'field field-name-field-person-email field-type-email field-label-inline clearfix'):
            print(count, div.a.text.replace('\n', ' ').strip())
            count += 1
    next_page = soup4.find_all('a', title = "Go to next page")
    if next_page:
        next_url = urllib.parse.urljoin(url4, next_page[0]['href'])
        next_html = urllib.request.urlopen(next_url).read()
        soup4 = BeautifulSoup(next_html, "html.parser")
    else:
        break
