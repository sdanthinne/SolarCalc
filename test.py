from mechanize import Browser
from bs4 import BeautifulSoup

b = Browser()
b.set_handle_robots(False)
b.addheaders = [('Referer', 'https://www.google.com'), ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

b.open('http://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html')
soup = BeautifulSoup(b.response().read(), "html.parser")
print(soup)