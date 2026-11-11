from bs4 import BeautifulSoup
import requests

url = 'https://github.com/google/j2cl'
res = requests.get(url)

print(f"ステータスコード：{res.status_code}")
print(f"ステータスメッセージ：{res.reason}")

# HTMLのソースコードをBeautifulSoupオブジェクトに変換する処理
# html_soup = BeautifulSoup(res.text, 'html.parser')
html_soup = BeautifulSoup(res.content, 'html.parser')
print(f"html_soupの型：{type(html_soup)}")


h2_all=html_soup.find_all('h2')
print(h2_all)
for h2 in h2_all:
     #print(type(h2))
    if h2.span is not None:
        print(h2.span.string)

print('aタグの場合')
a_list = html_soup.find_all('a',limit=5)

for a in a_list:
    print(a.string)


#5-3. 複数のタグで検索
tag_a_span_list = html_soup.find_all(['a','span'],limit=5)

for tag in tag_a_span_list:
    print(tag)

# 5-4. 任意の属性で検索
# hrefが'/'になっている部分を検索したい場合
tag_href_list = html_soup.find_all(attrs={"href":'/'})
for tag in tag_href_list:
    print(tag)

# 5-5. idやclass名で検索
print(html_soup.find_all(id='footer'))
print(html_soup.find_all(class_='l-header'))