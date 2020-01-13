from django.test import TestCase
from py_scraper.models import 
from django.urls import reverse
import os, pdb, json
from os import path
from PIL import Image       # PIL: Python Imaging Library
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS


class ProjectTestCase(TestCase):
    multi_db = True
    # Test ability to retrieve Projects from db
    # def setUp(self):
    #     chat = Project.objects.create(title="Chat App", description="One to many online chat", technology="nodejs, socket.io and ExpressJS", github_url="https://github.com/SolJCam/socket.io")
    #     web_map = Project.objects.create(title="Folium Web Map", description="Beautiful animated web display of US gradient features", technology="python dateutil, MarkerCluster and Pandas", github_url="https://github.com/SolJCam/location_pyapp")
    #     site = Project.objects.create(title="Personal Webiste", description="My online project portfolio", technology="Django, Bootstrap4 and jQuery", github_url="https://github.com/SolJCam/python_website")

    # def retrieve_project_by_some_attribute(self):
    #     app1 = Project.objects.get(id=1)
    #     app2 = Project.objects.get(title="Folium Web Map")
    #     app3 = Project.objects.get(description="My online project portfolio")



    if __name__ == "__main__":

    # get data directory (using getcwd() i.e, current working directory, is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, 'scrapedata/foxnews.txt')).read()
    # joint_text = "".join(text)

    # read the mask image; an image (ideally stencil) used to define the size, shape, coutours etc of the wordcloud
    news_mask = np.array(Image.open(path.join(d, "images/fox.jpeg")))  # size of the mask, for pusposes of this app, appears to matter

    # pdb.set_trace()
    # For multi-colored masks
    transformed_mask = transform_mask(news_mask,transform_format)
    # pdb.set_trace()
    
    # words to be ignored
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_font_size=100, max_words=20000, mask=news_mask,
                   stopwords=stopwords, contour_width=1, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "wrdcldimgs/fox.jpg"))

    # show
    plt.imshow(wc, interpolation='bilinear')        # Display an image. Positional arg: array-like or PIL image, interpolation: used to make the image appear more smoothly; https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/interpolation_methods.html
    plt.axis("off")     # the axis limits to be set. Axis: the area (atop the figure) on which the data is plotted with functions such as plot() and scatter()
    plt.figure()        # create a new figure (the overall window or page that everything is drawn on. It is the top-level component for features such as the axis)
    plt.imshow(news_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()