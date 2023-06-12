from bs4 import BeautifulSoup as bs
import requests

if __name__ == "__main__":
    web = 'https://www.shicimingju.com'
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    response = requests.get(url=url,headers=header)
    print(response.encoding)
    response.encoding = 'utf-8'
    chapter = bs(response.text,"lxml")
    # print(chapter.select('.book-mulu li'))
    page_li = chapter.select('.book-mulu li')
    # print(page_li[0].a['href'])
    print(page_li[1].a.string)
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in page_li:
        title = li.a.string
        page_url = web+li.a['href']
        response = requests.get(url=page_url,headers=header)
        response.encoding = 'utf-8'
        page = bs(response.text,'lxml')
        content =page.find('div',class_='chapter_content').text
        fp.write(title+'\n'+content+'\n')
    fp.close()