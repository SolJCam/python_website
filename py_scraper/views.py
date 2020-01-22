from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import requests, bs4, time, pdb, os.path, re
from selenium import webdriver
from py_scraper.newscloud import wcgenerator, wrd_count

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()




def py_scraper(request):  
  return render(request, 'py_scraper.html')





# Chromium Driver options
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.add_argument("--headless")
options.binary_location = "/Users/Sol/Applications/Chromium.app/Contents/MacOS/Chromium"
# Instanciate Chromium WebDriver
drive_path = os.path.join(d, 'drivers/chromiumdriver')
driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path,service_args=["--verbose", "--log-path=selchrome.log"])


# Using Chromium Driver to grab CNN html data
driver.get("https://www.cnn.com/")
cnndata = bs4.BeautifulSoup(driver.page_source, "html.parser")

# Using requests to grab html data
data = requests.get("https://www.msnbc.com/")
msnbcdata = bs4.BeautifulSoup(data.text, "html.parser") # Using beautiful soup to parse html data
data = requests.get("https://www.foxnews.com/")
foxnewsdata = bs4.BeautifulSoup(data.text, "html.parser")


pattern = r"\b[a-z]+\b"   # pattern to find exact words so as to avoid duplicates when counting words due to punctuation 


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
    try:
        wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
        return  JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)




def scrape_cnn(request):
    elements = [
        'span',
        'strong',
        'h2',
    ]
    cnnfile = open(os.path.join(d, "scrapedata/cnnnews.txt"), 'w')
    cnn_string_list = list()  
    for ele in elements:
        for cnnele in cnndata.find_all(ele):
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
    try:
        wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")
        return JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)




def scrape_fox(request):
    all_a_tags = foxnewsdata.findAll('a')
    foxfile = open(os.path.join(d, "scrapedata/foxnews.txt"), "w")
    fox_string_list = list() 
    for tag in all_a_tags:
        if tag.text == '':
            continue
        else:
            foxfile.write(tag.text)
            for string in tag.text.split():
                fox_string_list.append(string)
    foxfile.close()
    
    top_five_wrds = wrd_count(fox_string_list, pattern)
    try:
        wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")
        return JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)