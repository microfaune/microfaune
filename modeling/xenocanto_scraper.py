#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:25:20 2019

@author: pfarnole

updated version of the code presented here:
http://www.kscottz.com/web-scraping-with-beautifulsoup-and-python/

"""

from bs4 import BeautifulSoup
import urllib.request as urllib2
import os
import pandas as pd

# CHOOSE AND CREATE FOLDER WHERE TO SAVE THE SOUNDS ###########################
dataPath = 'rawData_citeU'
if not os.path.exists(os.path.join(os.getcwd(), dataPath)):
    os.mkdir(os.path.join(os.getcwd(),dataPath))
os.chdir(os.path.join(os.getcwd(),dataPath))

# LOAD LATIN NAMES OF THE BIRDS YOU ARE INTERESTED IN #########################
oiseaux_path = '/home/pfarnole/spyder_projects/microfaune/oiseaux.csv'
df = pd.read_csv(oiseaux_path)
birdList = list(df['Nom latin'].apply(lambda x: "+".join(x.split(" "))))

# CREATE INDIVIDUAL FOLDERS FOR EACH BIRD #####################################
paths = []
for bird in birdList:
    if not os.path.exists(os.path.join(os.getcwd(), bird)):
        os.mkdir(os.path.join(os.getcwd(),bird))
        print("Creating " + os.path.join(os.getcwd(),bird))
    else:
        print("Found " + os.path.join(os.getcwd(),bird))
    paths.append(os.path.join(os.getcwd(),bird))


# MAIN FUNCTION ###############################################################
def downloadBirdCalls(bird,path):
    """
    
    Input: bird latin name and a folder path
    
    Process:
        opens the URL of xeno-canto corresponding to that bird latin name
        organizes the content with BeautifulSoup
        searches for xc-button-audio in the html page
        then searches for 'data-xc-filepath' within (see html page structure)
        then from soundUrl, applies wget command to download the sound.
        
    Output: download all found files in directory passed in argument
    
    """
    stub = "http://www.xeno-canto.org/browse.php?species_nr=&query="
    print("#"*30)
    print("DOWNLOADING {0} to {1}".format(bird,path))
    os.chdir(path)
    n = 1
    page = '&pg='
    foundStuff = True
    while foundStuff:
        print("DOING PAGE {0}".format(n))
        url = stub+bird+page+str(n)
        n = n + 1
        url = urllib2.urlopen(url)
        content = url.read()
        soup = BeautifulSoup(content,features="lxml")
        found = soup.findAll("div", {"class": "xc-button-audio"})
        if( len(found) < 1 ):
            foundStuff = False
        for foundSound in found:
            subfound = foundSound.find("div", {"class": "jp-type-single"})
            soundUrl = subfound.attrs['data-xc-filepath']
            grabThis = "wget https:"
            grabThis = grabThis + soundUrl
            os.system(grabThis)

# ACTUALLY CALL THE FUNCTION ##################################################
for bird,path in zip(birdList,paths):
    downloadBirdCalls(bird,path)
