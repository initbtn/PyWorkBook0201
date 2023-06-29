import pandas as pd
from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

inFilename = 'Excel/singer.xlsx'
outFilename = 'Excel/singer_over6.xlsx'

df_seniro = pd.read_excel(inFilename, 'senior', index_col=None)
df_junior = pd.read_excel(inFilename, 'junior', index_col=None)

df_singer = pd.concat( [df_seniro, df_junior] )
df_singer_over6 = df_singer[df_singer['인원'] >= 6]
df_singer_over6 = df_singer_over6.sort_values(by=['인원'], axis=0, ascending=False)

df_singer_over6 = df_singer_over6.loc[:, ['아이디', '이름', '인원', '유튜브 조회수']]

 
## DataFrame 만들기
df = DataFrame({"Temp": [20.1, 22.3, 21.5, 20.7, 21.2]})
 
## XlsxWriter 엔진으로 Pandas writer 객체 만들기
writer = pd.ExcelWriter('pandas_xlsxWriter.xlsx', engine='xlsxwriter')
 
## DataFrame을 xlsx에 쓰기
df_singer_over6.to_excel(writer, sheet_name='Sheet1')
 
## Pandas writer 객체 닫기
writer.close()