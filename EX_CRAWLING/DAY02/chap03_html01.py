from bs4 import BeautifulSoup
from urllib.request import urlopen


#-------------------CSS 속성을 이용한 검색-------------------#
html_text='<span class="red">Heavens! what a virulent attack!</span>'
soup = BeautifulSoup(html_text,'html.parser')
object_tag = soup.find('span')
print('object_tag:',object_tag)
print('attr:',object_tag.attrs)
print('value:',object_tag.attrs['class'])
print('text:',object_tag.text)

#-------------------CSS 속성을 이용한 태그 검색 (등장 인물 검색)-------------------#
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html,"html.parser")

# 등장인물의 이름: 녹색
name_list = soup.find_all('span',{'class':'green'})
for name in name_list:
    print(name.string)

#-------------------특정 단어 찾기-------------------#
prince_list = soup.find_all(string='the prince')
print(prince_list)
print('the prince count: ',len(prince_list))

#-------------------트리 이동: 자식과 자손-------------------#
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,'html.parser')
# 자식
table_tage=soup.find('table',{'id':'giftList'})
print('children 개수: ', len(list(table_tage.children)))

index = 0
for child in table_tage.children:
    index +=1
    print(f'[{index}]: {child}')
    print('-'*30)
# 자손
desc = soup.find('table',{'id':'giftList'}).descendants
list_desc = list(desc)
print('descendants 개수: ',len(list_desc))

for tag in list_desc:
    print(tag)

# 형제 : next_siblings 속성

for sibling in soup.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)
    print('-'*30)

print('previous_siblings')
for sibling in soup.find('tr',{'id':'gift2'}).previous_siblings:
    print(sibling)

# 형제 다루기 #3
sibling1=soup.find('tr',{'id':'gift3'}).next_sibling
print('sibling1: ',sibling1)
print(ord(sibling1)) # '/n' 형태라서 화면에 출력되지 않음.

sibling2 =soup.find('tr',{'id':'gift3'}).next_sibling.next_sibling
print(sibling2)

# 부모 다루기
style_tag = soup.style
print(style_tag.parent)

img1 = soup.find('img',{'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)












