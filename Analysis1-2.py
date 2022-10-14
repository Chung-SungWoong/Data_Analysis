""" 
데이터 선택 - 칼럼 기준 
"""

import pandas as pd

sample1 = pd.read_excel('/Users/chung_sungwoong/Desktop/Practice/Data_Analysis/files/sample_1.xlsx', header = 1, skipfooter = 2)

print(sample1['입국객수'])

print(sample1[['국적코드','입국객수']])     # 괄호 두개

sample1['기준년월'] = '2019-11'           # 칼럼 추가 후 2019-11 이라는 값을 추가

print(sample1)

"""
데이터 선택 - 로우 기준
"""

# 일반적으로 로우를 선택하는 경우는 특정 조건에 맞는 데이터를 필터링한 결과를 찾을 때

condition = (sample1['성별'] == '남성')
print(condition)                # 결과값이 boolean으로 출력
print(sample1[condition])       # 성별이 남성인 데이터가 출력

condition2 = (sample1['입국객수'] >= 150000)
print(condition2)
print(sample1[condition2])

condition3 = (sample1['성별'] == '남성') & (sample1['입국객수'] >= 150000)
print(sample1[condition3])

condition4 = (sample1['국적코드'] == 'A01') | (sample1['국적코드'] == 'A18')
print(sample1[condition4])

# or을 표현하는 다른 방법

condition5 = (sample1['국적코드'].isin(['A01','A18']))
print(sample1[condition5])
# 만약 국적코드 A01, A18을 제외한 내용을 보고 싶다면
print(sample1[condition5 == False])