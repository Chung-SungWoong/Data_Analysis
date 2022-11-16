"""

"""

import pandas as pd

sample = pd.read_excel('/Users/chung_sungwoong/Desktop/Practice/Data_Analysis/files/sample_2.xlsx', header = 1, skipfooter = 2)

sample_pivot = sample.pivot_table(values = '입국객수', index = '국적명',columns = '기준월일', aggfunc = 'mean')

sample_pivot