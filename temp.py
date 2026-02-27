import csv

from utility import *
import chardet

data = read_csv_by_list('data/take_photo_data.csv')
print(data)

# with open('data/take_photo_data.csv','w',newline='',encoding='utf-8') as f:
#     writer = csv.DictWriter(f,fieldnames=['count'])
#     writer.writeheader()
#     writer.writerows([{'count':1},{'count':5},{'count':10}])