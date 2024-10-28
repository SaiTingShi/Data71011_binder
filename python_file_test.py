import pandas as pd
print('Hello World!')
data1 = [[1,2,3],
         [4,5,6],
         [3,6,8]]
table1 = pd.DataFrame(data1,columns = ['column1','column2','column3'], index = ['row1','row2',''row3])
print(table1)
