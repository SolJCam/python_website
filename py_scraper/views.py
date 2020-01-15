from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound
import requests, bs4, time, pdb, os.path
from selenium import webdriver
from py_scraper.newscloud import wcgenerator





def py_scraper(request):  
  return render(request, 'py_scraper.html')


d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# # Chromium Driver metadata for testing
# options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--test-type")
# options.add_argument("--headless")
# options.binary_location = "/Users/Sol/Applications/Chromium.app/Contents/MacOS/Chromium"
# # Chromium Driver for testing
# driver = webdriver.Chrome(chrome_options=options,executable_path='./drivers/chromiumdriver',service_args=["--verbose", "--log-path=selchrome.log"])


# Using requests to grab html data
data = requests.get("https://www.msnbc.com/")
msnbcdata = bs4.BeautifulSoup(data.text, "html.parser") # Using beautiful soup to parse html data
data = requests.get("https://www.foxnews.com/")
foxnewsdata = bs4.BeautifulSoup(data.text, "html.parser")

def scrape_msnbc(request):
  # html elements where desired text data can be found
  classes = [
      {'span' : 'headline___38PFH'},
      {'span' : 'video-label'},
      {'a' : 'vilynx_disabled'},
  ]
  ele = []
  # retrieve all instances of elements and append to list 
  for cl in classes:
      try:
          ele.append(msnbcdata.find_all('span', attrs={"class":cl['span']}))
      except:
          ele.append(msnbcdata.find_all('a', attrs={"class":cl['a']}))

  msnbcfile = open(os.path.join(d, "scrapedata/msnbcnews.txt"), "w") # open text file to write scraped data to
  # loop through list of elements and retrieve inner text 
  for ec in ele:
      for text in ec:
          msnbcfile.write(text.text)
  msnbcfile.close()
  # run word cloud generator and return result or raise internal server error exception
  try:
    wrdcld = wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
    pdb.set_trace()
    return wrdcld
  except:
    return HttpResponseNotFound(status=500)







# def scrape_fox(request):
  # all_a_tags = foxnewsdata.findAll('a')
  # foxtext = []
  # foxfile = open("scrapedata/foxnews.txt", 'w')
  # for tag in all_a_tags:
  #     if tag.text == '':
  #         continue
  #     else:
  #         foxfile.write(tag.text)

  # foxfile.close()
  # wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")







# def scrape_cnn(request):
  # elements = [
  #     'span',
  #     'strong',
  #     'h2',
  # ]
  # cnntext = []
  # cnnfile = open("scrapedata/cnnnews.txt", 'w')
  # for ele in elements:
  #     for cnnele in cnndata.find_all(ele):
  #         try:
  #             if '(function' in cnnele.string: 
  #                 continue
  #             else:
  #                 cnnfile.write(cnnele.text)
  #         except:
  #             continue

  # cnnfile.close()
  # wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")