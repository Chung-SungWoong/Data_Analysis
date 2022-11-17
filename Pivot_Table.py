"""

"""

import pandas as pd

sample = pd.read_excel('/Users/chung_sungwoong/Desktop/Practice/Data_Analysis/files/sample_index_false.xlsx')

sample_pivot = sample.pivot_table(values = '입국객수', index = '국적명', columns = '기준년월', aggfunc = 'mean')

print(sample_pivot)

sample_pivot2 = sample.pivot_table(values = '입국객수', index = '국적명', aggfunc = 'max')
print(sample_pivot2)