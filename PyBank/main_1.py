import os 
import csv
import pandas as pd

# counter for rows 
count_rows=0
PL_col =[]
PL_date=[]
date_row=[]
PL_diff=[]
# file path 
csv_path=r"PyBank\Resources\budget_data.csv"
# open csv file and restore in csv_reader 
with open(csv_path, 'r') as csv_file: 
    csv_reader= csv.reader(csv_file , delimiter=',')
    #ignore first row 
    csv_header=next(csv_reader)
    row_dummy=0
    for row in csv_reader:
        count_rows+=1
        PL_col.append(float(row[1]))
        PL_date.append(row[0])
        next_row=int(row[1])

        change=next_row-row_dummy
     
        row_dummy=int(row[1])
       

        PL_diff.append(change)
    PL_col_total= sum(PL_col)
    average_PL=float((PL_col[-1] - PL_col[0])/(len(PL_col)-1))
    inex_max=PL_diff.index(max(PL_diff))
    inex_min=PL_diff.index(min(PL_diff))

print ('Financial Analysis')
print("-------------------------------------")     
print(f' Total months : {count_rows}')
print(f' Total : ${PL_col_total} ')
print(f' Average  Change: ${average_PL}')
print(f' Greatest Increase in Profits: {PL_date[inex_max] }  $({max(PL_diff)}) ')
print(f' Greatest Decrease in Profits: {PL_date[inex_min] }  $({min(PL_diff)}) ')

txt_path=r"PyBank\report1.txt"
with open(txt_path, 'w') as PyBank_result:
    
    PyBank_result.write('Financial Analysis ')
    PyBank_result.write('\n------------------------------------- ')
    PyBank_result.write(f' \nTotal months : {count_rows}')
    PyBank_result.write(f' \nTotal : ${PL_col_total} ')
    PyBank_result.write(f' \nAverage  Change: ${average_PL}')
    PyBank_result.write(f' \nGreatest Increase in Profits: {PL_date[inex_max] }  $({max(PL_diff)}) ')
    PyBank_result.write(f' \nGreatest Decrease in Profits: {PL_date[inex_min] }  $({min(PL_diff)}) ')
