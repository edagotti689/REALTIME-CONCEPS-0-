from datetime import datetime, timedelta

two_hours_from_now = datetime.now() + timedelta(hours=2)

print(datetime.now())
print(two_hours_from_now)
#print('{:%H:%M:%S}'.format(two_hours_from_now))

# use_date = use_date + datetime.timedelta(minutes=+10)
# use_date = use_date + datetime.timedelta(hours=+1)
# use_date = use_date + datetime.timedelta(days=+1)
# use_date = use_date + datetime.timedelta(weeks=+1)
# use_date = use_date+relativedelta(months=+1)
# use_date = use_date+relativedelta(day=31)
