#!/usr/bin/env python3
print('Content-type: text/html\n')
#importing modules
import urllib.request
import re
from collections import deque
import os
from collections import Counter
from nltk.tokenize import word_tokenize
import nltk.stem.porter as p
import math

def read_file(file_name):
#opens file 
    file = open(file_name, "r", encoding = "utf-8")
    lines = file.readlines()
    file.close()
#strips and splits with a space
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = lines[i].split(" ")
#returns content
    return lines

#functiion that returns a list of urls
def URL_search(URL, filename):
    file = open(filename, "a")    
#empty yurl list
    url_list = []
#reauesting to open the webpage
    req = urllib.request.Request(URL, headers={'User-Agent': 'IUB-I427-nievesl'})
#opens up the URL contents
    fileobj = urllib.request.urlopen(req)
#getting the contents of the page
    contents = fileobj.read().decode(errors = "replace")
#closing the page
    fileobj.close()
#getting the body of the page
    body = re.findall('(?<=<body).+?(?=</body>)',contents, re.DOTALL)[0]
#getting the resource 
    websites = (re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',body, re.DOTALL))
#appending the resource with the scheme and hostname
    for website in websites:
        url_list.append(website)
        file.writelines(str(URL) + " " + str(website))
        file.write("\n")
    file.close()
#returning the list      
    return url_list

#web crawling function that takes a URL, # of crawls, the directory for the files to be saved, and crawling type
def web_crawling(url, num_crawls, directory, crawl_type):
#opening up index.dat for write the file name, and the corresponding URL
    file = open("index.dat", "w")
#empty counter
    count = 0
#calling the URL search function 
    search = URL_search(url, "pagerank.txt")
#converting the list into a deque
    url_deque = deque(search)
#if clause for breadth first search
    if crawl_type == "bfs" or crawl_type == "breadth-first search":  
#for loop for the amount of crawls
        for i in range(num_crawls):
#looping through all the lists for FIFO
            for url in URL_search(url_deque.popleft(), "pagerank.txt"):
#if URL isnt in the deque, it will be appended to it
                if url not in url_deque:
#try statement
                    try:
                        url_deque.append(url)
#opening up the web page
                        web_page = urllib.request.urlopen(url)
#getting the contents of web page
                        contents = web_page.read().decode(errors = "replace")
#closing the web page
                        web_page.close()
#var name to determine where to save the file
                        complete_name = os.path.join(directory, str(count) + ".html")
#saving the HTML code of the web page
                        sub_file = open(complete_name, "w", encoding = "utf-8")
                        sub_file.write(contents)
                        sub_file.close()
  #adding 1 to the counter
                        print(count)
                        count += 1
#except statement in case something wrong happens
                    except urllib.error.HTTPError:
                        print("Sorry, cannot find URL")
#writng the name of the of file and url to index.dat
                file.write(str(complete_name) + " " + str(url))
#closing the file
        file.close()
#elif clause for depth first search
    elif crawl_type == "dfs" or crawl_type == "depth-first search":
#looping through the amount of crawls
        for i in range(num_crawls):
#for loop for LIFO
            for url in URL_search(url_deque.pop(), "pagerank.txt"):
#if url is not in the deque, it will be appended to the deque
                if url not in url_deque:
#try statement 
                    try:
                        url_deque.append(url)
    #opening up the web page
                        web_page = urllib.request.urlopen(url)
    #getting the contents
                        contents = web_page.read().decode(errors = "replace")
    #closing the web page
                        web_page.close()
    #saving the file to the correct directory
                        complete_name = os.path.join(directory, str(count) + ".html")
                        sub_file = open(complete_name, "w", encoding = "utf-8")
                        sub_file.write(contents)
                        sub_file.close()
                        count += 1 
#except statement to skip over invalid urls or cant find url
                    except urllib.error.HTTPError:
                        print ("Sorry, Cannot find URL")
                file.write(str(complete_name) + " " + str(url))
        file.close()
        
def common_words(file_name):
#opening a file with its contents
    file = open(file_name, "r", encoding = "utf-8")
    lines = file.read()
    file.close()
#reading in the stopwords file to remove from the text    
    stop_file = open("stopwords.txt", "r", encoding = "utf-8")
    stop_lines = stop_file.read()
    stop_file.close()
#converting the list into a set 
    stop_lines = set(stop_lines)
#a list to get the stems from words
    new_list = []
#tokenizing the words
    lists_of_strings = word_tokenize(lines) 
#assigning a variable for a method needed to tokenize words
    stemmer = p.PorterStemmer()
#looping through each word and getting the stem of it while
#also appending it to a list
    for string in lists_of_strings:
        if string in stop_lines:
            lists_of_strings.remove(string)
            
    for string in lists_of_strings:
        new_list.append(stemmer.stem(string))
#getting the count of the new list
    lines_ct = Counter(new_list)
#making an empty dictionary for terms and relative frequencies
    diction = {}
#for loop to turn item into a frequency
    for item in lines_ct:
        diction[item] = lines_ct[item]/len(lists_of_strings)
#returning the dictionary
    return diction

#function that loops over text files in a folder
def file_os(folder_name):
#getting the current working directory
    home = os.getcwd()
#getting the contents of the CWD
    contents = os.listdir(os.path.join(home,folder_name))
#empty file list 
    file_list = []
    
#for loop to loop over the contents and appending text files into the file_list list
    for item in contents:
        if os.path.isfile(folder_name + "/" + item):
            file_list.append(item)
#empty dictionary
    diction = {}
#looping over every file and adding it into the dictionary
    for file in file_list:
        #if "Lab" in file:
        diction[file] = (common_words(folder_name + "/" + file))
        
#returning the dictionary
    return diction

def inv_indexer(mapping_dict, value_dict, inv_index):
    #adding a counter for IDs
    count = 0
    #looping over the file names
    for file_name in value_dict:
        #checking to see if the file name is in map_dictionary
        if file_name in mapping_dict.values():
            pass
        else:
        #if it isn't, it will be given an id
            mapping_dict[count] = file_name
        #looping over the terms from each file
        for term in value_dict[file_name]:
            #if it is in inv_diction, it's value will be added by 1
            if term in inv_index:
                inv_index[term][count] = value_dict[file_name][term]
            #else, it will be given a new entry
            else:
                inv_index[term] = {count: value_dict[file_name][term]}
        count += 1
    #returning the new dictionaries

    return inv_index, mapping_dict


def TF_IDF(inverted_diction):
    #empty dictionary
    diction = {}
    #counter for document frequency
    count = 0
    #looping through the terms in inverted dictionary
    for term in inverted_diction:
    #if term doesn't exist in the new dictionary, make a new spot for it
        if term not in diction:
            diction[term] = {}
        #getting the DF for the term
        count = len(inverted_diction[term])
        #looping through the NTF for the term
        for key in inverted_diction[term]:
        #making the TF-IDF score
            tf_idf = (1/(1+(math.log(count)) * inverted_diction[term][key]))
            #making the score the value for the inner dictionary
            diction[term][key] = tf_idf
    #returning the dictionary
    return diction
        
def PageRank(lines):
#empty key list and dictionaries
    keys = []
    temp_diction = {}
    ranks = {}
    out_diction = {}
    in_diction = {}
#empty counter
    count = 0
#p value 
    p = 0.2
#getting the dictionaries for in degrees
    for line in lines:
        if line[0] not in out_diction:
            out_diction[line[0]] = [line[1]]
        else:
            out_diction[line[0]].append(line[1])
#getting the dictionaries for out degrees
    for line in lines:
        if line[1] not in in_diction:
            in_diction[line[1]] = [line[0]]
        else:
            in_diction[line[1]].append(line[0])
#getting all keys 
    for key in out_diction:
        keys.append(key)
    for key in in_diction:
        keys.append(key)
#turing it into a set
    keys = set(keys)
#getting the default value 
    for key in keys:
        if key not in ranks:
            ranks[key] = 1/len(keys)
            
#while loop
    while True:
#adding 1 to counter
        count += 1
#making a copy of rank dictionary
        temp_diction = ranks.copy()
#page rank algorithm
        for key in temp_diction:
            temp_diction[key] = p/(len(keys)) + (1-p) * temp_diction[key]
#if they are the same dictionaries, return temp_diction
        if temp_diction == ranks:
            return temp_diction

        
            
