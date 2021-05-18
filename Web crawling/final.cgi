#!/usr/bin/env python3
print('Content-type: text/html\n')

from coding_assignment_2 import read_file, common_words, file_os, inv_indexer, TF_IDF, URL_search, web_crawling, PageRank
import cgi
from nltk.tokenize import word_tokenize

file = read_file("pagerank.txt")
pagerank = PageRank(file)
map_dictionary = {}
inv_diction = {}
diction = (file_os("folder"))
inv_index = inv_indexer(map_dictionary, diction , inv_diction)
tf_idf_func = TF_IDF(inv_index[0])
def query(user, tf_idf_diction, map_dictionary, pagerank_diction):
#empty dictionary
    diction = {}
#empty list for keys
    key_list = []
#empty list for file names
    file_list = []
#lowering the words
    user = user.lower()
#toeknizing the words
    user = word_tokenize(user)
#looping through the words 
    for word in user:
#looping through the terms
        for key in tf_idf_diction[word]:
#making a new spot if the term doesn't exists in the new dictionary
                if key not in diction:
                    for key2 in pagerank_diction:
                        diction[key] = tf_idf_diction[word][key] * pagerank_diction[key2]
#if it does exist, adding the TF-IDF scores from the other files
                else:
                    diction[key] += tf_idf_diction[word][key]
        
#looping through the sorted dictionary
#https://stackoverflow.com/questions/40496518/how-to-get-the-3-items-with-the-highest-value-from-dictionary
#learned how to sort through a dictionary
    for key in diction:
#adding key to the key list
        key_list.append(key)
        
    for key in key_list:
        file_list.append(map_dictionary[key])
#returning the first three elements
    for file in sorted(file_list, reverse = True):    
        return file_list[:25]

form = cgi.FieldStorage()
url = form.getfirst('url', 'nothing')
search = form.getfirst('query', 'nothing')
type_search = form.getfirst('search_method', "bfs")

html = """
<!doctype html>
<html>
<head><meta charset = "utf-8">
<title>Search Queries</title></head>
<body>
<p>{content}</p>
</body>
</html>"""

if search != "nothing" and url != "nothing":    
    crawling = web_crawling(url, 5, (str(type_search) + "folder"),type_search)
    result = query(search, tf_idf_func, inv_index[1])
    #result = ["string"]
    print(html.format(content = result))
else:
    error = "Please try again"
    print(html.format(content = error))
    
    