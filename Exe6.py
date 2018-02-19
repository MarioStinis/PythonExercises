import calendar

months = ["a","January","February","March","April","May","June","July","August","September","October","November","December"]
month = input("please isert month(January,February,March,etc...): ")
year = input("please isert year: ")

for i in range(13):
	if month == months[i]:
		a = i
		break;
print(i)

print (year,a)
cal = calendar.month(int(year),int(a))

print (cal)