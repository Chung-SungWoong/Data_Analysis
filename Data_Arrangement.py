"""
데이터 전처리에 기본이 되는 기능들
"""

t1 = "    hp010-0000-0000    "
print(t1)
t2 = t1.strip()             # 공백 제거
print(t2)
t3 = t2.replace('hp','')    # 문자열 교체
print(t3)
t4 = t3.split('-')          # 문자열 나누기 
print(t4)