import csv,sys
from typing import List,Dict
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
#csv file to dictionary mapping
filename='testdata.csv'

#opening csv file in read mode
file= open(filename,"r",encoding="utf-8")
csv_reader=csv.DictReader(file)

#list (table) containing dictionary of each row of csv file
table: List[Dict[str,str]]=[]
for row in csv_reader:
    r1:Dict[str,str]={}
    for column in row:
        r1[column]=row[column]
    table.append(r1)
print(table)
file.close()

print("Reversing Bangala->English to English->Bangala")

#new table list containing english word to list of Bangala mapping
newtable : List[Dict[str,List]]=[]
newdict={}
for dict in table:
    for key,value in dict.items():
        if(len(value)!=0):
            if(key=="Bengala"):
                 v = value
            else:
                if value in newdict.keys():
                    newdict[value].append(v)
                else:
                    newdict[value]=[v]

print(newdict)
print("List of dictionary having fieldname map to each row value")
#converting list into CSV file standard format (field name to its value from each row mapping)
reslist=[]
for key,value in newdict.items():
    resdict={}
    resdict["English"]=key
    count=1
    for s in value:
        resdict['B'+str(count)]=s
        count=count+1
    reslist.append(resdict)
print(reslist)

##Transforming Dictionary back to CSV file with English word map to multiple corresponding Bangala word
print("Resultant CSV File created !!")

field_names=['English','B1','B2','B3','B4','B5','B6']
with open('ReverseMapping.csv','w',encoding="utf-8") as file:
    writer=csv.DictWriter(file,fieldnames=field_names)
    writer.writeheader()
    writer.writerows(reslist)

#A csv file named ReverseMapping.csv has been created which contains English->Bangala 
#word mapping (One to many)