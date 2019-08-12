import requests
from requests import get
from contextlib import closing
from bs4 import BeautifulSoup
import mechanize

def simple_url(url):
    try:

        with get(url, stream = True) as response:
            if is_good_response(response):
                return response.content
            else:
                return None
    except Exception as err:
        error(err)
   

def is_good_response(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 and content_type is not None and content_type.find("html")>-1)


def error(e):
    f = open("error.log","a+")
    f.write(e + "\n")
    f.close()

if __name__ == "__main__":
    latitude = input("latitude: ")
    longitude = input("longitude: ")
    city = 'Enter Lat/Long -->'
    # https://suncalc.org/#/lat,lon,zoom/date/time/objectlevel/maptype


    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'),
    ('REFERER', 'http://www.google.com/')]
    print("added headers")
    noaa = br.open("http://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html")
    html = noaa.read()

    

    # resp = simple_url("http://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html")
    #print(html)