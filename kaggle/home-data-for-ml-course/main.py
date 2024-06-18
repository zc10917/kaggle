
import  pandas as pd


file_path = 'train.csv'
data = pd.read_csv(file_path)

d = data.groupby('SalePrice').LotArea.max()
print(d)


