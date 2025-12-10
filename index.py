from datetime import date,time,datetime
today=date.today()
now=datetime.now()
print("Today's date:", today)
print("Current time is : ",now)
print("All the date components together are:", today.year, today.month, today.day)