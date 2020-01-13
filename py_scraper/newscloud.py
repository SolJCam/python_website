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
    text = open(path.join(d, f'scrapedata/{newsfile}')).read()

    # read the mask image; an image (ideally stencil) used to define the size, shape, coutours etc of the wordcloud
    news_mask = np.array(Image.open(path.join(d, f"masks/{imgpath}")))

    # words to be ignored
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=30000, mask=news_mask,
                stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, f"wrdcldimgs/{wrdcld}"))

    # open and save file to variable
    # image = open(path.join(d, f"imgs/{wrdcld}")).read()

    return "success!"