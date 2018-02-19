import random
a = input("insert file name(.txt): ")
f = open(a, 'r')
list1 = list(f.read().split())

f.close()

a = len(list1) -1 
	
for i in range(a,-1,-1):	
	for c in list1[i]:
		if c.isupper():
			list1.pop(i)
			break;			
	
StartList = [[0 for x in range(3)] for y in range(len(list1)//3)] 
k = 0
for i in range(0,len(list1),3):
	if i < len(list1)-2:
		for j in range(0,3):
			StartList[k][j] = list1[i+j]
		k += 1	

randStartList = random.choice(StartList)
list3 = []
FinaList = []
rand3 = []
FinaList.append(randStartList)

def Exercise10(StartList,randStartList,list3,rand3):
	for i in range(67):
		for i in range(len(StartList)):
			if randStartList == StartList[i]:
				continue;
			elif randStartList[1] == StartList[i][0] and randStartList[2] == StartList[i][1]:
				list3.append(StartList[i])
				rand3 = random.choice(list3)
				FinaList.append(rand3)
				randStartList = rand3
				del list3[:]
	for i in range(len(FinaList)):
		for j in range(3):
			print(FinaList[i][j],end=' ')
			
Exercise10(StartList,randStartList,list3,rand3);