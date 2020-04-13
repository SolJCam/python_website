from django.http import FileResponse
import os, pdb, re
from os import path
from PIL import Image       # PIL: Python Imaging Library
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS


# stopwords to include in both wcgenerator and wrd_count functions
stopwrds_list = ["we", "will", "says", "view", "entertainment", "u", "news", "cnn", "fox", "/", "+", "&"] + list(STOPWORDS)

def wcgenerator(newsfile, imgpath, wrdcld):
    # get data directory (using getcwd() i.e, current working directory, is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, f'py_scraper/scrapedata/{newsfile}')).read()

    # read the mask image; an image (ideally stencil) used to define the size, shape, coutours etc of the wordcloud
    news_mask = np.array(Image.open(path.join(d, f"py_scraper/static/masks/{imgpath}")))

    wc = WordCloud(background_color="white", max_words=30000, mask=news_mask, stopwords=stopwrds_list, contour_width=3, contour_color='steelblue', relative_scaling='auto')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, f"py_scraper/static/imgs/{wrdcld}"))
    
    return "Success!"



def wrd_count(string_list, pattern):
    wrd_hash = dict()      # dictionary to add words and number of occurences

    # loop list of words in string_list to count occurences of ec word
    for ec_string in string_list:
        lower_strings = (ec_string).lower()
        match = re.search(pattern, lower_strings)
        if lower_strings not in stopwrds_list:
            if match != None and match[0] != 'u':
                if match[0] not in wrd_hash:
                    wrd_hash[match[0]] = 1
                else:
                    wrd_hash[match[0]] = wrd_hash[match[0]]+1
            elif lower_strings in wrd_hash:
                wrd_hash[lower_strings] = wrd_hash[lower_strings]+1
            else:
                wrd_hash[lower_strings] = 1 
    # pdb.set_trace()
    sorted_wrd_hash = sorted(wrd_hash.items(), key=lambda x: x[1], reverse=True)   # sort words based off occurences recorded in values
    return_sorted = sorted_wrd_hash[:5]
    
    return return_sorted