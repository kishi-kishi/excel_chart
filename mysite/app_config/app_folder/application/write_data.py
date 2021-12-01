# coding:utf-8
# import xlwings as xw
# from xlwings.constants import AxisType

# import os
# import csv
# htmlからのデータをcsvファイルに記録
# def write_csv(data):
#     datas = [data]
#     with open(os.getcwd()+'/app_folder/application/'+'data.csv','a') as f:
#         writer = csv.writer(f, lineterminator='\n')
#         writer.writerow(datas)

# coding:utf-8
import xlwings as xw
from xlwings.constants import AxisType
import json

# def deco(data):
#     global data_table
#     data_table = json.loads(data)

# htmlからのデータをcsvファイルに記録
def save(data):
    global x
    x = data

def save2(data):
    global y
    y = data

def save3(data):
    global x_uni
    x_uni = data

def save4(data):
    global y_uni
    y_uni = data

def save5(data):
    global tbl
    table = json.loads(data)

    return print(table)



    # l = len(table)
    # tbl = [[0] * 2 for i in range(l-1)]
    # for i in range(1,l):
    #     for j in range(1,3):
    #         tbl[i-1][j-1] = int(table[i][j].replace(",",""))

def write_csv():
    print(save5)
