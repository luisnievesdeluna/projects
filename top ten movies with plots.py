import urllib.request
import re

def wikilinks(url):
    #empty list
    films = []
    web_page = urllib.request.urlopen(url)
    contents = web_page.read().decode(errors = "replace")
    web_page.close()
    #looks in the table that links are in
    table = re.findall('(?<=films of 2019\n</caption>).+?(?=</table>)', contents, re.DOTALL)[0]
    #looks for the links that are inside of table
    links = re.findall('(?<=<i><a href=").+?(?=")', table, re.DOTALL)
    user = input("Search a movie: ")
    for link in links:
        if user in link:
            web_page = urllib.request.urlopen('https://en.wikipedia.org' + link)
            contents_v2 = web_page.read().decode(errors = "replace")
            web_page.close()
        
            plot = re.findall('(?<= id="Plot">Plot</span>).+?(?=<span class="mw-headline")', contents_v2, re.DOTALL)
            print(plot)
         

wikilinks('https://en.wikipedia.org/wiki/2019_in_film')
