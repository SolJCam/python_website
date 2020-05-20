from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import requests, bs4, time, pdb, os, re
from selenium import webdriver
from py_scraper.newscloud import wcgenerator, wrd_count


d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
driver = webdriver.Chrome(chrome_options=options,executable_path=os.environ.get('CHROMEDRIVER_PATH'))

# Using Chromium Driver to grab CNN html data
driver.get("https://www.cnn.com/")      # Using beautiful soup to parse html data
cnn_html = bs4.BeautifulSoup(driver.page_source, "html.parser")

# Using requests to grab html data; done upon reading of view file so as to minize pyscraper runtime 
msnbc_data = requests.get("https://www.msnbc.com/")
msnbc_html = bs4.BeautifulSoup(msnbc_data.text, "html.parser") 
foxnews_data = requests.get("https://www.foxnews.com/")
foxnews_html = bs4.BeautifulSoup(foxnews_data.text, "html.parser")



def py_scraper(request):  
  return render(request, 'py_scraper.html')



pattern = r"\b[a-z]+\b"   # pattern to find exact words and avoid duplicates due to punctuation for word count function 



def msnbc(request):

    start = time.time()

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
            ele.append(msnbc_html.find_all('span', attrs={"class":cl['span']}))
        except:
            ele.append(msnbc_html.find_all('a', attrs={"class":cl['a']}))

    msnbcfile = open(os.path.join(d, "scrapedata/msnbcnews.txt"), "w") # open text file to write scraped data to
    msnbc_string_list = list()  # list to append indv words created from splitting inner text of elements in ele
    # loop through list of elements and retrieve inner text 
    for ec in ele:
        for text in ec:
            msnbcfile.write(text.text)
            for string in text.text.split():
                msnbc_string_list.append(string)
    msnbcfile.close()
    
    top_five_wrds = wrd_count(msnbc_string_list, pattern)
    # pdb.set_trace()
    # run word cont and word cloud generator and return result of word count or raise internal server error exception
    
    end = time.time()
    time_elapsed = end - start
    print("Time elapsed to scrape page and count words: "+str(round(time_elapsed, 2))+" secs")

    return  top_five_wrds, wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
        




def cnn(request):    

    start = time.time()
    
    elements = [
        'span',
        'strong',
        'h2',
    ]
    cnnfile = open(os.path.join(d, "scrapedata/cnnnews.txt"), 'w')
    cnn_string_list = list()  
    for ele in elements:
        for cnnele in cnn_html.find_all(ele):
            try:
                if '(function' in cnnele.string: # for function instances that appear throughout cnn's html due to the abundance of script tags
                    continue
                else:
                    cnnfile.write(cnnele.text)
                    for string in cnnele.text.split():
                        cnn_string_list.append(string)
            except:
                continue
    cnnfile.close()

    top_five_wrds = wrd_count(cnn_string_list, pattern)
        
    end = time.time()
    time_elapsed = end - start
    print("Time elapsed to scrape page and count words: "+str(round(time_elapsed, 2))+" secs")

    return top_five_wrds, wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")




def fox(request):  

    start = time.time()
    
    all_a_tags = foxnews_html.findAll('a')
    foxfile = open(os.path.join(d, "scrapedata/foxnews.txt"), "w")
    fox_string_list = list() 
    for tag in all_a_tags:
        if tag.text == '':
            countinue
        else:
            foxfile.write(tag.text)
            for string in tag.text.split():
                fox_string_list.append(string)
                # pdb.set_trace()
    foxfile.close()
    
    top_five_wrds = wrd_count(fox_string_list, pattern)
        
    end = time.time()
    time_elapsed = end - start
    print("Time elapsed to scrape page and count words: "+str(round(time_elapsed, 2))+" secs")

    return top_five_wrds, wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")