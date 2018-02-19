def got13(a,grammata):
	for i in range(len(a)):
		if a[i] in grammata and a[i] <= "M":
			b = grammata.index(a[i])
			print(grammata[b+26], end="")
		elif a[i] in grammata and a[i] > "M":
			c = grammata.index(a[i])
			print(grammata[c-26], end="")
		else: 
			print(a[i], end="")

grammata = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
a = input("Εισαγωγή κειμένου: ")
print("ROT13:             ",end="")
got13(a,grammata);