from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, FileResponse, HttpRequest, QueryDict
import requests, bs4, time, pdb, os, re, json, boto3
from selenium import webdriver

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

if os.environ["SOLS_MAC"]:
    os.environ['S3_BUCKET_NAME'] = "py-scraper"
    os.environ['AWS_ACCESS_KEY_ID'] = "AKIAJWRR7YIKJDE27N2Q"
    os.environ['AWS_SECRET_ACCESS_KEY'] = "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"

    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--test-type")
    options.add_argument("--headless")

    # Chrome Driver options
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    drive_path = os.path.join(d, 'drivers/chromedriver83')

    # Instanciate WebDriver
    driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path)
    

def s3_upload(request):

    # pdb.set_trace()
    file_name = request['txt']
    
    # for testing in browser with dev tools
    # file_name = json.loads(request.body)

    S3_BUCKET = os.environ.get('S3_BUCKET_NAME')

    file_type = "txt"

    s3 = boto3.client('s3')

    presigned_post = s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key = file_name,
        Fields = {"acl": "public-read", "Content-Type": file_type},
        Conditions = [
            {"acl": "public-read"},
            {"Content-Type": file_type}
        ],
        ExpiresIn = 3600
    ) 
    # pdb.set_trace()

    post_data = {}

    for k,v in presigned_post['fields'].items():
        post_data[k] = v

    post_data['news_file'] = open(os.path.join(d, "scrapedata/"+file_name), "rb")

    url = f'https://{S3_BUCKET}.s3.amazonaws.com/{file_name}'
    # pdb.set_trace()

    return HttpRequest.body(url, data=post_data)   
    # return requests.post(url, data=post_data)
    # return HttpResponse(post_data)
    # return json.dumps({ 'data': post_data })
    
    # for testing in browser with dev tools
    # return JsonResponse(post_data, safe=False)




''' 
File requests for testing in browser with dev tools
'''

def fetch_MSNBC_file(request):

    try:
        news_file = open(os.path.join(d, "scrapedata/msnbcnews.txt"), "rb")
        scrape_img = {}
        scrape_img['file'] = news_file
        return FileResponse(news_file)  
    except:
        return HttpResponseNotFound(status=500)




def fetch_CNN_file(request):

    try:
        news_file = open(os.path.join(d, "scrapedata/cnnnews.txt"), "rb")
        scrape_img = {}
        scrape_img['file'] = news_file
        return FileResponse(news_file)  
    except:
        return HttpResponseNotFound(status=500)




def fetch_FOX_file(request):

    try:
        news_file = open(os.path.join(d, "scrapedata/foxnews.txt"), "rb")
        scrape_img = {}
        scrape_img['file'] = news_file
        return FileResponse(news_file)  
    except:
        return HttpResponseNotFound(status=500)












