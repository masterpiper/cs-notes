import requests
from bs4 import BeautifulSoup as bs
import io

if __name__ == "__main__":
    web = 'http://chriszheng.science/pua-books/'
    url = "http://chriszheng.science/pua-books/"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    responses = requests.get(url=web,headers=header)
    responses.encoding = 'utf-8'
    book_url = bs(responses.text,"lxml")
    book_tag = book_url.select('a')
    # print(book_tag[1].string)
    # print(book_tag[1]['href'])
    book_url_list = []
    for i in range(1,len(book_tag)):
        name = book_tag[i].string.replace(" ","_")
        burl = url + book_tag[i]['href']
        book_url_list.append([name,burl])
    for item in book_url_list:
        r = requests.get(url=item[1],headers=header)
        dirs = './book/' + item[0]
        fp = open(dirs,'wb')
        fp.write(r.content)
        fp.close()
        print(item[0]+" download finish.")
    print("Download Finish!")
    
    