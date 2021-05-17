import urllib.request
import re
import random
import webbrowser

def WikiLeaks():
#user input
    user = input("where would you like to start? ")
#user jumps
    user_2 = input("How many jumps? ")
#for loop to loop over how many jumps the user wants
    for jump in range(int(user_2)):
#opens the starting link
        web_page = urllib.request.urlopen(user)
        contents = web_page.read().decode(errors = "replace")
        web_page.close()
#finds the body full of wiki links
        body = re.findall('(?<=<body).+?(?=</body>)',contents, re.DOTALL)[0]
#finds a random wiki link extension (/wiki/whatever/)
        random_website = random.choice(re.findall('(?<=href=")/wiki/.+?(?=")',body, re.DOTALL))
#makes it into a full wiki link
        wiki_website = "https://en.wikipedia.org" + random_website
        print("Jumping from:", user)
        print()
        print("To:", wiki_website)
        print()
#loops over so that for loop can continue
        user = wiki_website
#opens the wiki website everytime
        webbrowser.open(wiki_website)
WikiLeaks()
