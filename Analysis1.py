"""
Learn basic of the Pandas
The most common form of the data is table which composed with column and row.
pandas is the python library that helps to handle the table formed data
"""

import pandas as pd

sample1 = pd.read_excel('/Users/chung_sungwoong/Desktop/Practice/Data_Analysis/files/sample_1.xlsx', header = 1, skipfooter = 2, usecols = 'A:C')

"""
pd.read_excel = 파일을 불러오는 함수 
header = 칼럼명이 있는 위치를 나타냄
skipfooter = 2 => 마지막에 로우의 두 줄은 생략
usecols = 'A:C' => A칼럼부터 C칼럼까지 불러오기
"""

print(sample1.head(3))      # 처음부터 3 까지의 행을 보여주는 코드 (vs code 에서는 print()함수가 없으면 출력이 안되는듯함)

print(sample1.tail(3))      # 마지막에서 3번째 부터 마지막까지의 행을 보여주는 코드 (vs code 에서는 print()함수가 없으면 출력이 안되는듯함)

sample1.info()              # 데이터에 대한 요약 정보 제공

print(sample1.describe())   # 데이터의 기초 통계량 확인

# 입국객수에 대한 여러가지 통계량을 보여준다. 데이터의 개수, 평균값, 표준편차, 최솟값, 1사분위수, 2사분위수, 3사분위수, 최댓값


