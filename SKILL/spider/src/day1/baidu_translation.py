import requests
import json
if __name__ == "__main__":
    post_url = "https://fanyi.baidu.com/sug"
    kw = input()
    # POST request args
    param = {
        "keyword":kw,
    }
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    response = requests.post(url=post_url,params=param,headers=header,endonding="utf-8")
    dic_obj = response.json()
    print(dic_obj)

    # json store
    with open('./storage/dog.json','w',encoding='utf-8') as fp:
        json.dump(dic_obj,fp=fp,ensure_ascii=False)
        fp.close()
    print("Finish!")
    
