import csv
import pandas
field_names=['Roll_No', 'Name', 'Age']
stud_dict=[{'Roll_No':'1', 'Name': 'Yadu','Age': 20},
{'Roll_No':'2', 'Name': 'Sherin','Age': 19},
{'Roll_No':'3', 'Name': 'Aparna','Age': 20},
]
with open('Names.csv','w') as f:
    writer=csv.DictWriter(f,fieldnames=field_names)
    writer.writeheader()
    writer.writerows(stud_dict)
    
data=pandas.read_csv("Names.csv")
print (data)
