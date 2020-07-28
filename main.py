import json
import pandas as pd
from tqdm import tqdm

import seaborn as sns
import matplotlib.pyplot as plt

import datetime
import os.path
from os import path
import csv

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from google_play_scraper import Sort, reviews, app, reviews_all

# %matplotlib inline
# %config InlineBackend.figure_format='retina'

sns.set(style='whitegrid', palette='muted', font_scale=1.2)


def main():
    app_domain = 'com.grubhub.android'

    date_range = ['2020-05-01', '2020-05-02', '2020-05-03', '2020-05-04', '2020-05-05', 
    '2020-05-06', '2020-05-07', '2020-05-08', '2020-05-09', '2020-05-10']

    app_reviews = []

    if (not path.exists('data.json')):
        result = reviews_all(
            app_domain,
            sleep_milliseconds=0, # defaults to 0
            lang='en', # defaults to 'en'
            country='us', # defaults to 'us'
            sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
            filter_score_with=1 # defaults to None(means all score)
        )

        for review in result:
            temp = review['at']
            temp = temp.strftime('%Y-%m-%d')
            
            for date in date_range:
                print(temp, date)
                if temp == date:
                    print("True")
                    app_reviews.append(review)
            
                    

        with open('data.json', 'w') as outfile:
            json.dump(app_reviews, outfile, default = myconverter)


    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    # now we will open a file for writing 
    csv_file = open('data.csv', 'w') 
    
    # create the csv writer object 
    csv_writer = csv.writer(csv_file) 
    
    # Counter variable used for writing  
    # headers to the CSV file 
    count = 0
    
    for review in data: 
        if count == 0: 
            # Writing headers of CSV file 
            header = review.keys() 
            csv_writer.writerow(header) 
            count += 1
    
        # Writing data of CSV file 
        csv_writer.writerow(review.values()) 
    csv_file.close() 



def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


if __name__ == '__main__':
    main()