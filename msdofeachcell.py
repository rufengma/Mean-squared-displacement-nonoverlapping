import csv
import math
#program for put all x and y in a list, and count how many cells we are using
f = open('Breast_10um_200nm.csv')
csv_f = csv.reader(f)
dictrows={}
csv_list=[]
for row in csv_f:
    csv_list.append(row) #have a list contains all rows
length=len(csv_list) #how many rows in this csv

for i in range(1,30):  #how many cells you want
    dictrows[i]=[[],[]]#2 empty lists, #0 contains x, #1 contains y.
    for j in range(length): # loop over all rows in the csv
        #print(csv_list[j][1])
        if csv_list[j][1]!='' and int(csv_list[j][1])==i:
            dictrows[i][0].append(int(csv_list[j][2])) #x
            dictrows[i][1].append(int(csv_list[j][3])) #y
#===============================================Make a new dictionary just contains cells have data.
s=0
cells={}#the new dictionary's name!!

for i_1 in range(1,30):
    if dictrows[i_1][0]!=[]:
        a=dictrows[i_1][0]
        b=dictrows[i_1][1]
        cells[s]=[a,b] #a new dictionary keys are from 0 to 18
        s+=1
print(s)
print(cells[5])
print(cells)
# s is the number of cells we finally got, and the cells matrix only have their [x0,x1,x2...] and [y0,y1,y2,...]

#program for calculate the MSD for a time difference t.
#Here we can insert the t we would like to use
 #a dictionary for save all msdsall
all_cell_msd=[] #a list saves all cells' msd
all_cell_msd_ave=[]
for m in range(s): #loop over all cells in cells dictionary
    msd={}
    ave={}
    frame_numb=len(cells[m][0])
    for t_single in range(1,frame_numb): #t_single=1 means time difference is 10. like this
        t=t_single*10  
        n=0
        temp_msd_list=[]
        while n < frame_numb: #frames this cell has been recorded
            if n+t_single <frame_numb:
                temp=math.pow((cells[m][0][n]-cells[m][0][n+t_single]),2)+math.pow((cells[m][1][n]-cells[m][1][n+t_single]),2)
                temp_msd_list.append(temp/(2.95*2.95))  #MSD equation
            n+=t_single
        msd[t]=temp_msd_list
        ave[t]=sum(temp_msd_list)/float(len(temp_msd_list))
    all_cell_msd.append(msd)  #list[dictionary1[time1:list,time2:list,time3:list...], dictionary2...] [cell,cell,cell...]
    all_cell_msd_ave.append(ave) #list[dictionary1[time1:number,time2:number,...], dictionary2...]

print(all_cell_msd_ave[5])

#======================================================output csv
out_file = open('Breast_10um_200nm_out.csv','w')
title="cell number"
for i in range(1,60):
    title+=','+str(i*10)
title+='\n'
print(title)

out_file.write(title)

cell_tmp = 1
for dict_x in all_cell_msd_ave:
    out_file.write('%s,'%cell_tmp)
    for tmp_t in dict_x.keys():
        out_file.write('%s,'%dict_x[tmp_t])
    out_file.write('\n')
    cell_tmp+=1
    
out_file.close()

