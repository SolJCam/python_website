from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import requests, bs4, time, pdb, os.path
from selenium import webdriver
from py_scraper.newscloud import wcgenerator

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# # Chromium Driver metadata for testing
# options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--test-type")
# options.add_argument("--headless")
# options.binary_location = "/Users/Sol/Applications/Chromium.app/Contents/MacOS/Chromium"
# # Chromium Driver for testing
# driver = webdriver.Chrome(chrome_options=options,executable_path='./drivers/chromiumdriver',service_args=["--verbose", "--log-path=selchrome.log"])

# Using requests for production

data = requests.get("https://www.msnbc.com/")
msnbcdata = bs4.BeautifulSoup(data.text, "html.parser")
data = requests.get("https://www.foxnews.com/")
foxnewsdata = bs4.BeautifulSoup(data.text, "html.parser")

def py_scraper(request):  
  return render(request, 'py_scraper.html')


def scrape_msnbc(request):
  classes = [
      {'span' : 'headline___38PFH'},
      {'span' : 'video-label'},
      {'a' : 'vilynx_disabled'},
  ]
  ele = []
  for cl in classes:
      try:
          ele.append(msnbcdata.find_all('span', attrs={"class":cl['span']}))
      except:
          ele.append(msnbcdata.find_all('a', attrs={"class":cl['a']}))

  msnbcfile = open(os.path.join(d, "scrapedata/msnbcnews.txt"), "w")
  for ec in ele:
      for text in ec:
          msnbcfile.write(text.text)
  msnbcfile.close()
  result = wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
  return result   # throws AttributeError on return command. May require render function to work  


  #   context = {
  #     'form': form,
  #     'add_word': add_word_form,
  #     'projects': projects,
  # }

  # return render(request, 'local_apps.html', context)







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