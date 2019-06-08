import requests
from bs4 import BeautifulSoup
def get_title(url):
    response = requests.get(url)	
    if response.status_code == 200:				# 성공적으로 GET 요청을 했다면,
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')	# BeautifulSoup로 HTML을 분석합니다.
        title = bs.select_one('title')			# 분석된 HTML에서 title 태그를 찾습니다
        return title.text						# 찾은 title 태그의 내용만 돌려줍니다.
    else:
        return None
if __name__ == "__main__":
    # KT는 안되덥니다!!!
    print(get_title('http://www.naver.com'))
    print(get_title('http://www.google.com'))

response = requests.get('http://www.google.com')
if response.status_code == 200:             # 성공적으로 GET 요청을 했다면,
    html = response.text
    bs = BeautifulSoup(html, 'html.parser')	# BeautifulSoup로 HTML을 분석합니다.
    title = bs.select_one('title')			# 분석된 HTML에서 title 태그를 찾습니다
    print(title)

html = '<div id="content"><p class="text world">Hello, World!</p><p class="text giga">Hello, Giga Genie!</p></div>'
bs = BeautifulSoup(html, 'html.parser')
p1 = bs.div.p
p2 = bs.select_one('#content > .text')
p3 = bs.select('p')
print(p1)
print(p2)
print(p3)

print(bs.div)
print(bs.div.p)

# p 태그들을 가져옵니다.
print(bs.select_one('p'))               

# 클래스가 giga 인 p 태그들을 가져옵니다.
print(bs.select('p.giga'))          

# 아이디가 content인 태그 내에 클래스가 world 인 태그들을 가져옵니다.
print(bs.select('#content .world')) 
