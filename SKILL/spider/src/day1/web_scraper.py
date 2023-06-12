import requests

# UA disguise(User-Agent):
# Server will check if the requests UA is a browser.

if __name__ == "__main__":
    # UA disguise
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    url = "https://www.sogou.com/web"
    # deal with url args:encapsulation to dirctory
    kw = input("enter a word:")
    param = {
        'query':kw
    }
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName = "./storage/"+kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
        fp.close()
    print("Finish!")