list1=["sunflower", "daisy", "orchid, rose"]
list2=["rose", "Jasmine", "Lily"]
temp3=[]
for i in list1:
	if i not in list2:
		temp3.append(i)
print(temp3)
