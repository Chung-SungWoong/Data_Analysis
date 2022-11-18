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



