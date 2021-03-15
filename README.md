# PythonCSV

FlowChart or steps in Reversing Mapping of Bengala->English to English->Bengala (CSV File)

1. First convert csv file to dictionary mapping
2. Opening csv file in read mode
3. Using csv reader convert it into list (say table) containing dictionary of each row of csv file
4. Now converting table list to new table list which contains english word to list of Bangala mapping i.e. mapping of english word as key and list of all corresponding Bangala word as value in dictionary.
5. Making a List of dictionary having fieldname map to each row value"). In other words converting new table list into CSV file standard format (i.e field name to its value from each row mapping).
6. Transforming this list of Dictionary mapping back to CSV file where English word map to multiple corresponding Bangala word 
7. Opening created CSV File in write mode.
8. A csv file named ReverseMapping.csv has been created which contains English->Bangala word mapping (One to many type mapping)

Input CSV File format : Fieldname: [Bengala,E1,E2,E3,E4,E5,E6] where 'E' corresponds to English 

Resultant CSV File format : Fieldname: [English,B1,B2,B3,B4,B5,B6] where 'B' corresponds to Bengala 
Here one english word maps to multiple Bengala words
 
-> Execute code with Python 3 Interpretor
