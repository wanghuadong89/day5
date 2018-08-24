import urllib.request
import urllib.parse
from lxml import etree
import os


headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',

}
def get_request(url,page):
    if page==1:
        url=format(url%'')
    else:
        pn='_'+str(page)
        url=format(url%pn)
    return urllib.request.Request(url,headers=headers)

def download_images(image_url_list):
    dir_name='性感美女'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    for image_url in image_url_list:
        request=urllib.request.Request(image_url,headers=headers)
        image_data=urllib.request.urlopen(request).read()
        image_name=os.path.basename(image_url)
        path=os.path.join(dir_name,image_name)
        with open(path,'wb') as fp:
            fp.write(image_data)




start_page=int(input('enter a start page:'))
end_page=int(input('enter a end page:'))
url='http://sc.chinaz.com/tupian/xingganmeinvtupian%s.html '
for page in range(start_page,end_page+1):
    request=get_request(url,page)
    response=urllib.request.urlopen(request)
    content=response.read().decode()
    tree=etree.HTML(content)
    image_url_list=tree.xpath('//div[@id="container"]//img/@src2')
    download_images(image_url_list)