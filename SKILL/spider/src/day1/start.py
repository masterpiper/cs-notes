import requests

if __name__ == "__main__":
    # step1:set url
    url = "https://www.sogou.com/"
    # step2:send requests
    response = requests.get(url=url)
    # step3:get respond data
    page_txt = response.text
    print(page_txt)
    # step4:store
    with open("./sogou.html",'w',encoding='utf-8') as fp:
        fp.write(page_txt)
        fp.close()
    print("Finish!")

