import requests
import json

if __name__ == "__main__":
    post_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    keyword=input("地点")
    parama = {
        "keyword":keyword,
        "pageIndex":1,
        "pageSize":10,
        "pid":"",
        "cname":""
    }
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    response = requests.post(url=post_url,params=parama,headers=header)
    result = response.text
    print(result)
    with open("./storage/zibo_kfc.json","w",encoding='utf-8') as fp:
        json.dumps(result,fp=fp,ensure_ascii=False)
        fp.close()