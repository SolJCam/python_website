from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import requests, bs4, time, pdb, os, re
from selenium import webdriver
from py_scraper.newscloud import wcgenerator, wrd_count
from py_scraper.rq_queue import q_scrape


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
        drive_path = os.path.join(d, 'drivers/chromedriver83')

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
    print("Time elapsed to scrape msnbc and count words: "+str(round(time_elapsed, 2))+" secs")
    
    # q_scrape(wcgenerator, ("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png"), 'msnbc')
    # pdb.set_trace()

    try:
        # wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
        q_scrape(wcgenerator, ("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png"), 'msnbc')
        return  JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)




def scrape_cnn(request):

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
    print("Time elapsed to scrape cnn and count words: "+str(round(time_elapsed, 2))+" secs")
    
    # q_scrape(wcgenerator, ("cnnnews.txt", "cnn.png", "cnnwrdcld.png"), 'cnn')
    
    try:
        # wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")
        q_scrape(wcgenerator, ("cnnnews.txt", "cnn.png", "cnnwrdcld.png"), 'cnn')
        return JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)




def scrape_fox(request):
            
    start = time.time()  

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
        
    end = time.time()
    time_elapsed = end - start
    print("Time elapsed to scrape fox and count words: "+str(round(time_elapsed, 2))+" secs")
       
    # pdb.set_trace()

    # q_scrape(wcgenerator, ("foxnews.txt", "fox.jpeg", "foxwrdcld.png"), 'fox')

    try: 
        # wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")
        q_scrape(wcgenerator, ("foxnews.txt", "fox.jpeg", "foxwrdcld.png"), 'fox')
        return JsonResponse(top_five_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)




def del_clds(request):      # may be unnecessary as wrdcld process rarely errors and virtually always saves the latest scraped wrdcld

    time.sleep(90)
    # pdb.set_trace()
    try:
        os.remove(os.path.join(d, "static/imgs","msnbcwrdcld.png"))
        print("deleted word cloud image msnbcwrdcld.png")
    except:
        print("no msnbc wrdcld")

    try:
        os.remove(os.path.join(d, "static/imgs","cnnwrdcld.png"))
        print("deleted word cloud image cnnwrdcld.png")
    except:
        print("no cnn wrdcld")
    
    try:
        os.remove(os.path.join(d, "static/imgs","foxwrdcld.png"))
        print("deleted word cloud image foxwrdcld.png")
    except:
        print("no fox wrdcld")

    return HttpResponse(status=200)


# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
# import pdb, os, time
# from py_scraper.rq_queue import q_scrape
# # from py_scraper.scrapenews import msnbc, cnn, fox
# from py_scraper.prod_views import msnbc, cnn, fox

# d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()



# def py_scraper(request):  
#   return render(request, 'py_scraper.html')



# def scrape_msnbc(request):

#     start = time.time()
#     # q_result = q_scrape(msnbc, 'msnbc')
#     # top_five_wrds = q_result[0][0]
#     # print(q_result)
#     # pdb.set_trace()
    
#     top_five_wrds = msnbc('request')[0]

#     end = time.time()
#     time_elapsed = end - start
#     print("Time elapsed to complete entire process for msnbc: "+str(round(time_elapsed, 2)))

#     try:
#         return  JsonResponse(top_five_wrds, safe=False)
#     except:
#         return HttpResponseNotFound(status=500)




# def scrape_cnn(request):

#     start = time.time()
#     # q_result = q_scrape(cnn, 'cnn')
#     # top_five_wrds = q_result[0][0]
#     # print(q_result)
    
#     top_five_wrds = cnn('request')[0]
    
#     end = time.time()
#     time_elapsed = end - start
#     print("Time elapsed to complete entire process for cnn: "+str(round(time_elapsed, 2)))
    
#     try:
#         return JsonResponse(top_five_wrds, safe=False)
#     except:
#         return HttpResponseNotFound(status=500)




# def scrape_fox(request):
            
#     start = time.time()
#     # q_result = q_scrape(fox, 'fox')
#     # top_five_wrds = q_result[0][0]
#     # print(q_result)
    
#     top_five_wrds = fox('request')[0]
    
#     end = time.time()
#     time_elapsed = end - start
#     print("Time elapsed to complete entire process for fox: "+str(round(time_elapsed, 2)))

#     try:
#         return JsonResponse(top_five_wrds, safe=False)
#     except:
#         return HttpResponseNotFound(status=500)