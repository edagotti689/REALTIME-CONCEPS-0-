from datetime import datetime


# To get current time
time = datetime.now()
print(time)

# To get only year
print(' \n YEAR ', time.strftime("%Y"))

# To get only month
print(' \n MONTH ', time.strftime("%B"))

# To get only DATE
print(' \n DATE ', time.strftime("%d"))

# To get only DATE, Month and year
print(' \n D M Y ', time.strftime("%d:%B:%Y"))

# To get only DAY OF WEEK
print(' \n DAY ', time.strftime("%a"))

# To get only HOUR IN TIME
print(' \n HOUR ', time.strftime("%H"))

# To get TIME
print(' \n TIME ', time.strftime("%H/%M/%S"))
print(' \n TIME ', time.strftime("%H:%M:%S"))

