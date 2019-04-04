from bs4 import BeautifulSoup
import requests
def genereWise(genre):
    sc = []
    dict = {'Fantasy':16190,'comedy':4460,'Science':2402297011,'Horror-Fiction':2402179011,'Humor':4456,'Romance':23,'Childrens':4}
    num = dict[genre]
    url = "https://www.amazon.com/Best-Sellers-Books-"+genre+"/zgbs/books/"+str(num)
    op = requests.get(url).text
    soup = BeautifulSoup(op, 'lxml')
    b = soup.find('ol', class_="a-ordered-list a-vertical")
    for li in b.find_all('li', class_= "zg-item-immersion"):
        all_a = li.find('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1")
        all_b = all_a.string
        sc.append(all_b)
    n = " ".join(sc[:5])
    return n