from django.http import FileResponse, HttpResponse, HttpRequest
import os, pdb, re, time, boto3
from os import path
from PIL import Image       # PIL: Python Imaging Library
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from rq import get_current_job


# get data directory (using getcwd() i.e, current working directory, is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

s3_resource = boto3.resource('s3')

# stopwords to include in both wcgenerator and wrd_count functions
stopwrds_list = ["we", "will", "says", "view", "entertainment", "u", "news", "cnn", "fox", "/", "+", "&"] + list(STOPWORDS)

def wcgenerator(newsfile, mskimg, wrdcld):
    
    start = time.time()
    # pdb.set_trace()
    
    # Download text from Amazon s3 bucket
    s3_resource.Object("py-scraper", newsfile).download_file(path.join(d, f"scrapedata/{newsfile}"))
    # Read the whole text.
    text = open(path.join(d, f'scrapedata/{newsfile}')).read()
    print(text)
    # read the mask image; an image (ideally stencil) used to define the size, shape, coutours etc of the wordcloud
    news_mask = np.array(Image.open(path.join(d, f"static/masks/{mskimg}")))
    wc = WordCloud(background_color="white", max_words=30000, mask=news_mask, stopwords=stopwrds_list, contour_width=3, contour_color='steelblue', relative_scaling='auto')
    # generate word cloud
    wc.generate(text)
    # store to file
    wc.to_file(path.join(d, f"static/imgs/{wrdcld}"))
    print(open(path.join(d, f"static/imgs/{wrdcld}")).read())
    # Upload image to Amazon s3 bucket      ## Curreently not working on heroku!!
    s3_resource.meta.client.upload_file(Filename=path.join(d, f"static/imgs/{wrdcld}"),Bucket="py-scraper",Key=wrdcld)

    end = time.time()
    time_elapsed = end - start
    
    # pdb.set_trace()
    print(f"Time elapsed to generate and save {wrdcld} word cloud: "+str(round(time_elapsed, 2))+" secs\n")

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