#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 18:36:07 2017

@author: Juan
"""

import requests; import pandas as pd; import urllib.request; import time
from lxml import html; from lxml import etree; from bs4 import BeautifulSoup; 
from time import sleep; from datetime import datetime

import tmdbsimple as tmdb
tmdb.API_KEY = 'e833f1a8c681bdef2edc1be2572d28e7'

fictionalcharacters = pd.ExcelFile("fictionalcharacters.xlsx")
moviegenres = pd.ExcelFile("moviegenres.xls")
movies = pd.ExcelFile("movies.xls")
tvchannels = pd.ExcelFile("tvchannels.xls")
tvnetwork = pd.ExcelFile("tvnetwork.xls")
tvshows = pd.ExcelFile("tvshows.xls")

fictionalcharactersDF = fictionalcharacters.parse("Sheet1")
moviegenresDF = moviegenres.parse("fblmain2")
moviesDF = movies.parse("fblmain2")
tvchannelsDF = tvchannels.parse("fblmain2")
tvnetworkDF = tvnetwork.parse("fblmain2")
tvshowsDF = tvshows.parse("fblmain2")

fictionalcharacters = fictionalcharactersDF["object_name"].values.tolist()
moviegenres = moviegenresDF["object_name"].values.tolist()
movies = moviesDF["object_name"].values.tolist()
tvchannels = tvchannelsDF["object_name"].values.tolist()
tvnetwork = tvnetworkDF["object_name"].values.tolist()
tvshows = tvshowsDF["object_name"].values.tolist()

## Priority: movies, tv shows

len(movies) # 1075
len(tvshows) # 740

search = tmdb.Search()
response = search.movie(query='The Bourne')

response

#for s in search.results:
#    print(s['title'], s['id'], s['release_date'], s['popularity'])

for item in movies:
    print(item);
    movieslistLEN.append(len(response))
    sleep(0.26) # Time in seconds
    movieslist.append(dict(response))
 
 
    
'results': [{'adult': False,
   'backdrop_path': '/2Fr1vqBiDn8xRJM9elcplzHctTN.jpg',
   'genre_ids': [28, 18, 9648, 53],
   'id': 2501,
   'original_language': 'en',
   'original_title': 'The Bourne Identity',
   'overview': 'Wounded to the brink of death and suffering from amnesia, Jason Bourne is rescued at sea by a fisherman. With nothing to go on but a Swiss bank account number, he starts to reconstruct his life, but finds that many people he encounters want him dead. However, Bourne realizes that he has the combat and mental skills of a world-class spy – but who does he work for?',
   'popularity': 6.328566,
   'poster_path': '/bXQIL36VQdzJ69lcjQR1WQzJqQR.jpg',
   'release_date': '2002-06-14',
   'title': 'The Bourne Identity',
   'video': False,
   'vote_average': 7.3,
   'vote_count': 3428}    
    
    
def scrape_movies(masterlist,index):

    # Accumulator lists for final DF
    objectlist = list()
    movieslist = list()
    movieslistLEN = list()



    # Get all URLs from root URL
    index = index
    t0 = time.time()
    for item in masterlist:
        print(type(item))
        #if len(item) != 0:
        if type(item) == str:
        
            #Scrape
            try:
                print(item)
                response = search.movie(query=str(item))
                movieslistLEN.append(len(response))
                sleep(0.2501) # Time in seconds
                movieslist.append(list(dict(response)))

                # Rating10.append([str(vinod.findAll(True, {'class':'ratingNumber'})[9])])
    
                index += 1
                print(str(index) + ", Time elapsed:" + str(time.time() - t0))
                print("Time remaining (approx):  " + str((len(masterlist)-index )*((time.time() - t0)/(index+1))/60) + " mins"  )
                # datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
            except IndexError:
                print("ERROR: Check index below")
                print(index)
                print(str(index) + ", Time elapsed:" + str(time.time() - t0))
                print("Time remaining (approx):  " + str((len(masterlist)-index )*((time.time() - t0)/(index+1))/60) + " mins"  )

            #except HTTPError:
            #    continue;
        else:
            movieslistLEN.append(0)
            movieslist.append(list("NA"))
            index += 1
            print(str(index) + ", Time elapsed:" + str(time.time() - t0))
            print("Time remaining (approx):  " + str((len(masterlist)-index )*((time.time() - t0)/(index+1))/60) + " mins"  )

    
    # Fill dictionary with all values 
    moviesdict = {
            "object_id": objectlist,
            "movieslist": movieslist,
            "movieslistLEN": movieslistLEN}
    
    # Input dict to DF
    resultsDF = pd.DataFrame(moviesdict)
    print(Errorlog)
    return(resultsDF)

#moviesDF

movies_df = scrape_movies(movies,0) 

writer_moviesDF = pd.ExcelWriter('movies_df.xlsx')
movies_df.to_excel(writer_moviesDF,'Sheet1')
writer_moviesDF.save()


