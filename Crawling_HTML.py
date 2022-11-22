"""
예제 HTML로 연습
"""

from bs4 import BeautifulSoup 

soup = BeautifulSoup(html, 'html.parser')           #html에 들어있는 문자열 정보를 HTML 형식에 맞게 해석

tags_span = soup.select('span')                     # select(Tag) 테그명에 겹치는 것을 모두 선택해서 변수에 저장
tags_p = soup.select('p')

ids_fruits1 = soup.select('#fruits1')               # 조건 뒤에 id 값에는 샵, class 값에는 점 (.)을 넣어서 조건 지정 가능
class_price = soup.select('.price') 
tags_span_class_price = soup.select('span.price')

tags_name = soup.select('span.name')                # 태그만으로 정보를 찾기 어려울때 어떠한 부모 태그를 활용하여 찾을 수 있다.

tags_banana = soup.select('#fruits1 > span.name')   # 위의 태그만으로는 파인애플과 바나나 둘 다 찾았지만, #fruits1이라는 조건을 더해줌으로써 banana만 나오게 되었다

tags_banana2 = soup.select('div.sale > #fruits1 > span.name')

tags_banana3 = soup.select('div.sale span.name')

tags = soup.select('span.name')
tag_1 = tags[0]




