import numpy as np
import pandas as pd

#Calculates the number of months between two specified dates
def month_difference(ima, kako):
    year1 = int(ima[0:4])
    year2 = int(kako[0:4])
    month1 = int(ima[5::])
    month2 = int(kako[5::])
    #print(kako,abs(month1))
    return (year1-year2)*12 + month1-month2
#Given a year and the number of data to produce
#the function will produce a list of times starting in January in this year  
def time_series(year,count_num):
    data_list = []
    count1 = 0
    temp = year*100 + 1                                                                           
    while(count1 < count_num):
        for i in range(12):
            data_list.append(str(temp)[:4] + '-' + str(temp)[4:])
            temp += 1
        temp += 100 - 12
        count1 += 12
    return data_list
#reorder
#this function get a sale_date array, change the data to start in January by adding 0
#and then, calculate the average by the original month
def re_sort(arr,kako_list):
    res = np.zeros(12)
    arr = list(arr)
    year1 = int(kako_list[-1][0:4])
    year2 = int(kako_list[0][0:4])
    month1 = int(kako_list[-1][5::])
    month2 = int(kako_list[0][5::])
    mat_all = (year1-year2+1)*12
    re_shape = np.zeros(mat_all)
    date_arr = time_series(year2, mat_all)
    #print(date_arr)
    count1 = 0
    for date_temp in kako_list:
        #print(date_temp)
        consur = date_arr.index(date_temp)
        re_shape[consur] = arr[count1]
        count1 += 1
    re_mat = re_shape.reshape((int(mat_all/12) , 12))
    res = np.sum(re_mat,axis=0)
    res_temp = np.ones(12) * int(mat_all/12)
    for i in range(month2 - 1):
        res_temp[i] -= 1
    for i in range(12 - month1):
        res_temp[11-i] -= 1
    for i in range(12):
        if res_temp[i] != 0:
            res[i] = res[i]/res_temp[i]
        else:
            res[i] = 0
    return res



time_set = '2022-03'
cols = ['date','L1','L2','L3',"amount"]
df = pd.read_csv('data.txt',delimiter='\t',names=cols,encoding='utf-8')
#del data after 2022-04
df = df[ ~ df['date'].str.contains('2022-04') ]
#different level
#The lowest order of direct data processing
#The highest-order data needs to be merged and sorted
line = list(set(df['L3']))

col = ['name','1','2','3','4','5','6','7','8','9','10','11','12','isactive']
df1 = pd.DataFrame(columns=col)
count3 = 1 
#collection of higher data
for line_name in line:
    #For higher-order data
    ########################################################
    temp = df[df['L3'] == line_name]
    date_list = list(set(temp['date']))
    #merge by month
    for date_name in date_list:
        temp2 = temp[temp['date'] == date_name]
        sum_amount_date =  temp2['amount'].sum() 
        temp.loc[(temp['date']== date_name),'amount'] = sum_amount_date
    temp.drop_duplicates('date',keep='first',inplace=True)
    temp.sort_values("date",inplace=True)
    #########################################################


    start_date  = temp['date'].iloc[0]
    end_date = temp['date'].iloc[-1]
    
    time_section = month_difference(end_date, start_date) + 1
    #time_section = (int(end_date[0:4]) - int(start_date[0:4]) + 1) * 12 

    #print(start_date,time_section,len(temp))
    sum_quantity = temp['amount'].sum()
    mean_total = sum_quantity / time_section
    amount_list = temp['amount'].values
    res = re_sort(amount_list,temp['date'].values) / mean_total
    isactive = 0
    if end_date == time_set:
        isactive = 1
    else:
        pass
    columns = [line_name] + list(res) + [str(isactive)]
    columns = pd.Series(columns,index=col,name=count3)
    df1=df1.append(columns)

df1.to_csv('test.csv',index=False,header=True,encoding='utf_8_sig') 