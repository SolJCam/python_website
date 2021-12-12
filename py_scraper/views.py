from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import requests, bs4, time, pdb, os, re
from selenium import webdriver
from py_scraper.newscloud import wcgenerator, wrd_count
# from py_scraper.rq_queue import q_scrape


d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

try:
    if os.environ["SOLS_MAC"]:
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--test-type")
        options.add_argument("--headless")

        # # Backup Chromium Driver options
        # options.binary_location = "/Users/Sol/Applications/Chromium.app/Contents/MacOS/Chromium"
        # drive_path = os.path.join(d, 'drivers/chromiumdriver')

        # Chrome Driver options
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        drive_path = os.path.join(d, 'drivers/chromedriver96')

        # Instanciate WebDriver
        driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path)
        # # Driver for testing (Includes log)
        # driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path,service_args=["--verbose", "--log-path=selchrome.log"])

except Exception as e:
    # Chrome/Selenium configuration for Heroku
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



def scrape_msnbc(request):

    # q_result = q_scrape(scrape_msnbc, 'msnbc')
    # print(q_result)

    # html elements where desired text data can be found
    ele = []
    a_tag = msnbc_html.find_all('a')
    span_tag = msnbc_html.find_all('span')
    h2_tag = msnbc_html.find_all('h2')
    h3_tag = msnbc_html.find_all('h3')
    h4_tag = msnbc_html.find_all('h4')
    all_tags = [
        a_tag,
        span_tag,
        h2_tag,
        h3_tag,
        h4_tag,
    ]
    
    def get_contents(html_tag):
        for tag in html_tag:
            try:
                if tag.contents and tag.contents[0].__class__.__name__ == 'Tag' and tag.get_text() != '':
                    ele.append(tag.get_text())
                    # pdb.set_trace()
            except:
                pdb.set_trace()
                print(tag)

    for diff_tags in all_tags:
        get_contents(diff_tags)

    # pdb.set_trace()

    msnbcfile = open(os.path.join(d, "scrapedata/msnbcnews.txt"), "w") # open text file to write scraped data to
    msnbc_string_list = list()  # list to append indv words created from splitting inner text of elements in ele
    # loop through list of elements and retrieve inner text 
    for text in ele:
        # pdb.set_trace()
        msnbcfile.write(text)
        for string in text.split():
            msnbc_string_list.append(string)
    msnbcfile.close()
    top_five_wrds = wrd_count(msnbc_string_list, pattern)
    # run word cont and word cloud generator and return result of word count or raise internal server error exception
    try:
        wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
        return  JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)




def scrape_cnn(request):

    # q_result = q_scrape(scrape_cnn, 'cnn')
    # print(q_result)    

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
    try:
        wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")
        return JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)




def scrape_fox(request):
            
    # q_result = q_scrape(scrape_fox, 'fox')
    # print(q_result)    

    all_a_tags = foxnews_html.findAll('a')
    foxfile = open(os.path.join(d, "scrapedata/foxnews.txt"), "w")
    fox_string_list = list() 
    for tag in all_a_tags:
        if tag.text == '':
            continue
        else:
            foxfile.write(tag.text)
            for string in tag.text.split():
                fox_string_list.append(string)
                # pdb.set_trace()
    foxfile.close()
    
    top_five_wrds = wrd_count(fox_string_list, pattern)
    try:
        wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")
        return JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)