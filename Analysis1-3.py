"""
데이터 통합
merge = 옆으로 통합
append = 아래로 통합
"""

import pandas as pd

sample1 = pd.read_excel('/Users/chung_sungwoong/Desktop/Practice/Data_Analysis/files/sample_1.xlsx', header = 1, skipfooter = 2)

print(sample1)

code_master = pd.read_excel('/Users/chung_sungwoong/Desktop/Practice/Data_Analysis/files/sample_codemaster.xlsx')
print(code_master)

sample1_code = pd.merge(left=sample1, right = code_master, how = 'left', left_on = '국적코드',right_on = '국적코드')
print(sample1_code)
# pd.merge 설명
# left 왼쪽 테이블 설정, right 오른쪽 테이블 설정, how = 'left' 왼쪽 테이블을 기준으로 두 테이블 결합, left_on 왼쪽 테이블의 기준 칼럼, right_on 오른쪽 테이블의 기준 칼럼
# 만약 왼쪽 오른쪽 모든 테이블에 공통으로 존재할 경우만 출력하고 싶다면

sample2_code = pd.merge(left = sample1, right = code_master, how = 'inner', left_on = '국적코드',right_on='국적코드')
print(sample2_code)
# how = 'inner'는 두 테이블의 기준 칼럼의 값이 서로 일치하는 경우에 사용하는 펑션

sample = sample1_code.append(sample2_code, ignore_index = True)
print(sample)

sample1_code.append(sample2_code)

sample.to_excel('/Users/chung_sungwoong/Desktop/Practice/Data_Analysis/files/sample.xlsx')


sample_pivot = sample.pivot_table(values = '입국객수', index = '국적명', columns = '기준년월', aggfunc = 'mean')