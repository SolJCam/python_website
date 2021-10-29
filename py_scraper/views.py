from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, FileResponse, HttpRequest, QueryDict
import requests, bs4, time, pdb, os, re, json, boto3
from selenium import webdriver
from py_scraper.newscloud import wcgenerator, wrd_count
from py_scraper.rq_queue import q_scrape


d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
s3_resource = boto3.resource('s3')

try:
    if os.environ["SOLS_MAC"]:
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--test-type")
        options.add_argument("--headless")

        # Chrome Driver options
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        drive_path = os.path.join(d, 'drivers/chromedriver94')
        # options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
        # drive_path = os.path.join(d, 'drivers/chromedriver')

        # Instanciate WebDriver
        driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path)

        # # Chromium Driver backup options
        # options.binary_location = "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
        # options.binary_location = "/Applications/Chromium.app/Contents/MacOS/Chromium"
        # drive_path = os.path.join(d, 'drivers/chromedriver81')

        # # Driver for testing (Includes log)
        # driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path,service_args=["--verbose", "--log-path=selchrome.log"])

except Exception as e:
    # Chrome/Selenium configuration for Heroku
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    driver = webdriver.Chrome(chrome_options=options,executable_path=os.environ.get('CHROMEDRIVER_PATH'))       # to update driver version: heroku config:set CHROMEDRIVER_VERSION=

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




def scrape_msnbc(request):

    start = time.time()

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

    # pdb.set_trace()
    # herokuS3 functionality    
    # s3request = QueryDict('txt=msnbcnews.txt')
    # s3 = s3_upload(s3request)

    # some_top_wrds = wrd_count(msnbc_string_list)

    # Upload text file to Amazon s3 bucket
    s3_resource.meta.client.upload_file(Filename=os.path.join(d, "scrapedata/msnbcnews.txt"),Bucket="py-scraper",Key="msnbcnews.txt")

    # pdb.set_trace()
    # success = wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
    success = q_scrape(wcgenerator, ("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png"), 'msnbc')
    # wcgenerator("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png")
    # q_scrape(wcgenerator, ("msnbcnews.txt", "msnbc.jpg", "msnbcwrdcld.png"), 'msnbc')

    end = time.time()
    time_elapsed = end - start
    print("Time elapsed to scrape msnbc and count words: "+str(round(time_elapsed, 2))+" secs")
    
    try:
        # Download image from Amazon s3 bucket
        if success == "success":
            return JsonResponse(msnbc_string_list, safe=False)
            # return HttpResponse(status=200)
        # return JsonResponse(msnbc_string_list, safe=False)
        # return JsonResponse(some_top_wrds, safe=False)
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
    # cnn_string_list.append("CNNFILE.TXT")
    cnnfile.close()
    
    # some_top_wrds = wrd_count(cnn_string_list)

    s3_resource.meta.client.upload_file(Filename=os.path.join(d, "scrapedata/cnnnews.txt"),Bucket="py-scraper",Key="cnnnews.txt")

    # pdb.set_trace()
    # success = wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")
    success = q_scrape(wcgenerator, ("cnnnews.txt", "cnn.png", "cnnwrdcld.png"), 'cnn')
    # wcgenerator("cnnnews.txt", "cnn.png", "cnnwrdcld.png")
    # q_scrape(wcgenerator, ("cnnnews.txt", "cnn.png", "cnnwrdcld.png"), 'cnn')

    end = time.time()
    time_elapsed = end - start
    print("Time elapsed to scrape cnn and count words: "+str(round(time_elapsed, 2))+" secs")

    try:
        if success == "success":
            return JsonResponse(cnn_string_list, safe=False)
            # return HttpResponse(status=200)
        # return JsonResponse(cnn_string_list, safe=False)
        # return JsonResponse(some_top_wrds, safe=False)
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
    # fox_string_list.append('FOXFILE.TXT')
    foxfile.close()
    
    # some_top_wrds = wrd_count(fox_string_list)
    
    s3_resource.meta.client.upload_file(Filename=os.path.join(d, "scrapedata/foxnews.txt"),Bucket="py-scraper",Key="foxnews.txt")
        
    # pdb.set_trace()
    # success = wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")
    success = q_scrape(wcgenerator, ("foxnews.txt", "fox.jpeg", "foxwrdcld.png"), 'fox')
    # wcgenerator("foxnews.txt", "fox.jpeg", "foxwrdcld.png")
    # q_scrape(wcgenerator, ("foxnews.txt", "fox.jpeg", "foxwrdcld.png"), 'fox')
    
    end = time.time()
    time_elapsed = end - start
    print(f"Time elapsed to queue fox word cloud: "+str(round(time_elapsed, 2))+" secs\n")
 
    try:
        if success == "success":
            return JsonResponse(fox_string_list, safe=False)
            # return HttpResponse(status=200)
        # return JsonResponse(fox_string_list, safe=False)
        # return JsonResponse(some_top_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)    




''' DOWNLOAD TOP WRDS PASSED THROUGH BROWSER ''' 




def top_fox_wrds(request):

    words = request.body.decode().strip('][').split(',')
    word_list = list()
    nu_word = ''
    for word in words:
        if word == '"':
            pass
        elif word != '"':
            nu_word = word.replace('"','')
            if nu_word == 'u.s.' or nu_word == 'U.S.':
                pass
            elif nu_word != 'u.s.' or nu_word != 'U.S.':
                word_list.append(nu_word)
    # pdb.set_trace()
    some_top_wrds = wrd_count(word_list)
    try:
        return JsonResponse(some_top_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500) 




def top_cnn_wrds(request):

    words = request.body.decode().strip('][').split(',')
    word_list = list()
    nu_word = ''
    for word in words:
        if word == '"':
            pass
        elif word != '"':
            nu_word = word.replace('"','')
            word_list.append(nu_word) 
    # pdb.set_trace()
    some_top_wrds = wrd_count(word_list)
    try:
        return JsonResponse(some_top_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500) 




def top_msnbc_wrds(request):
    # time.sleep(15)    
    # try:
    #     s3_resource.Object("py-scraper", "msnbcwrdcld.png").download_file(os.path.join(d, "static/imgs/msnbcwrdcld.png")) # Wordcld process needs to compelte first, otherwise throws internal server error
    # except Exception as e:
    #     print(f'wcgenerator img upload incomplete/failed: {e.__class__} (Unable to download)')

    words = request.body.decode().strip('][').split(',')
    word_list = list()
    nu_word = ''
    for word in words:
        if word == '"':
            pass
        elif word != '"':
            nu_word = word.replace('"','')
            word_list.append(nu_word)     
    # pdb.set_trace()
    some_top_wrds = wrd_count(word_list)
    try:
        return JsonResponse(some_top_wrds, safe=False)
    except:
        return HttpResponseNotFound(status=500)    




''' DOWNLOAD WRDCLD IMGS '''




def msnbc_img(request):

    exists = ''

    try:
        s3_resource.Object("py-scraper", "msnbcwrdcld.png").download_file(os.path.join(d, "static/imgs/msnbcwrdcld.png")) # Wordcld process needs to compelte first, otherwise throws internal server error
        exists = 'True'
    except Exception as e:
        print(f'wcgenerator img upload incomplete/failed: {e.__class__} (Unable to download)')

    # time.sleep(20)
    
    if exists == 'True':
        # os.path.join(d, "static/imgs","msnbcwrdcld.png")
        print("msnbc word_cloud image downloaded")
        return HttpResponse(status=200)
    else:
        print("no msnbc word_cloud img")
        return HttpResponse(status=500)




def cnn_img(request):

    exists = ''

    try:
        s3_resource.Object("py-scraper", "cnnwrdcld.png").download_file(os.path.join(d, "static/imgs/cnnwrdcld.png")) # Wordcld process needs to compelte first, otherwise throws internal server error
        exists = 'True'
    except Exception as e:
        print(f'wcgenerator img upload incomplete/failed: {e.__class__} (Unable to download)')

    # time.sleep(20)
    
    if exists == 'True':
        # os.path.join(d, "static/imgs","cnnwrdcld.png")
        print("cnn word_cloud image downloaded")
        return HttpResponse(status=200)
    else:
        print("no cnn word_cloud img")
        return HttpResponse(status=500)




def fox_img(request): 

    exists = ''

    try:
        s3_resource.Object("py-scraper", "foxwrdcld.png").download_file(os.path.join(d, "static/imgs/foxwrdcld.png")) # Wordcld process needs to compelte first, otherwise throws internal server error
        exists = 'True'
    except Exception as e:
        print(f'wcgenerator img upload incomplete/failed: {e.__class__} (Unable to download)')

    # time.sleep(20)
    
    if exists == 'True':
        # os.path.join(d, "static/imgs","foxwrdcld.png")
        print("fox word_cloud image downloaded")
        return HttpResponse(status=200)
    else:
        print("no fox word_cloud img")
        return HttpResponse(status=500)    




''' FUNCTIONS TO DELETE SAVED SCRAPED FILES MAY BE UNNECESSARY IN PRODUCTION '''




def del_msnbc_files(request):

    # time.sleep(20)
    # pdb.set_trace()

    try:
        os.remove(os.path.join(d, "scrapedata","msnbcnews.txt"))
        os.remove(os.path.join(d, "static/imgs","msnbcwrdcld.png"))
        print("deleted scrapedata file and word_cloud image for msnbc")
    except:
        print("no msnbc scrapedata word_cloud files")

    return HttpResponse(status=200)




def del_cnn_files(request):

    # time.sleep(20)
    # pdb.set_trace()

    try:
        os.remove(os.path.join(d, "scrapedata","cnnnews.txt"))
        os.remove(os.path.join(d, "static/imgs","cnnwrdcld.png"))
        print("deleted scrapedata file and word_cloud image for cnn")
    except:
        print("no cnn scrapedata word_cloud files")

    return HttpResponse(status=200)




def del_fox_files(request): 

    # time.sleep(25)
    # pdb.set_trace()

    try:
        os.remove(os.path.join(d, "scrapedata","foxnews.txt"))
        os.remove(os.path.join(d, "static/imgs","foxwrdcld.png"))
        print("deleted scrapedata file and word_cloud image for fox")
    except:
        print("no fox scrapedata word_cloud files")

    return HttpResponse(status=200)