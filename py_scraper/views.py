from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound
import requests, bs4, time, pdb, os.path, re
from selenium import webdriver
from py_scraper.newscloud import wcgenerator

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
    
    msnbc_wrd_hash = dict()      # dictionary to add words and number of occurences
    pattern = r"\b[a-z]+\b"   # pattern to find exact words so as to avoid duplicates due to punctuation (apostrophe's, colons etc) 
  # loop list of words in string_list to count occurences of ec word
    for ec_string in msnbc_string_list:
        lowercase_string = (ec_string).lower()
        match = re.search(pattern, lowercase_string)
        if match != None:
            if match[0] in msnbc_wrd_hash:
                msnbc_wrd_hash[match[0]] = msnbc_wrd_hash[match[0]]+1
            else:
                msnbc_wrd_hash[match[0]] = 1
        elif lowercase_string in msnbc_wrd_hash:
            msnbc_wrd_hash[lowercase_string] = msnbc_wrd_hash[lowercase_string]+1
        else:
            msnbc_wrd_hash[lowercase_string] = 1 

    sorted_msnbc_wrd_hash = sorted(msnbc_wrd_hash.items(), key=lambda x: x[1], reverse=True)   # sort words based off occurences recorded in values
    return_sorted = sorted_msnbc_wrd_hash[:5]
    pdb.set_trace()
    # run word cloud generator and return result or raise internal server error exception
    try:
        wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
        return HttpResponseNotFound(status=200), return_sorted
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
    try:
        wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")
        return HttpResponseNotFound(status=200)
    except:
        return HttpResponseNotFound(status=500)




def scrape_fox(request):
    all_a_tags = foxnewsdata.findAll('a')
    foxfile = open(os.path.join(d, "scrapedata/foxnews.txt"), "w")
    for tag in all_a_tags:
        if tag.text == '':
            continue
        else:
            foxfile.write(tag.text)
        pdb.set_trace()
        
    foxfile.close()
    try:
        wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")
        return HttpResponseNotFound(status=200)
    except:
        return HttpResponseNotFound(status=500)