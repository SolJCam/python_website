from django.http import FileResponse
import os, pdb
from os import path
from PIL import Image       # PIL: Python Imaging Library
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS



def wcgenerator(newsfile, imgpath, wrdcld):
    # get data directory (using getcwd() i.e, current working directory, is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, f'py_scraper/scrapedata/{newsfile}')).read()

    # read the mask image; an image (ideally stencil) used to define the size, shape, coutours etc of the wordcloud
    news_mask = np.array(Image.open(path.join(d, f"py_scraper/static/masks/{imgpath}")))

    wc = WordCloud(background_color="white", max_words=30000, mask=news_mask, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, f"py_scraper/static/imgs/{wrdcld}"))

    wrdcld = FileResponse(open(path.join(d, 'py_scraper/static/imgs/msnbcwrdcld.png'), "rb"))
    return wrdcld
    # return "success!"