import random

def triada(lista):
	a = "false"
	aList = [];
	for i in range(30):
		for j in range(i+1,30):
			for k in range(j+1,30):
				if [lista[i],lista[j],lista[k]] not in aList and [lista[i],lista[k],lista[j]] not in aList and [lista[j],lista[i],lista[k]] not in aList  and [lista[j],lista[k],lista[i]] not in aList  and [lista[k],lista[i],lista[j]] not in aList  and [lista[k],lista[j],lista[i]] not in aList:
					if lista[i] + lista[j] + lista[k]  == 0:
						print(lista[i],lista[j],lista[k])
						aList.append([lista[i],lista[j],lista[k]]);
						#print (aList)
						a = "true"
	if a == "false":
		print("Δεν υπάρχει συνδυασμός τριάδων που να κάνει 0.")

lista = [random.randint(-29, 29) for k in range(30)]

print(lista)
triada(lista)