from datetime import datetime

print(datetime.now())
print(f"hi = {datetime.now().year}" )

from datetime import timedelta



monthly = timedelta(days=30)
quarterly = timedelta(days=90)
yearly = quarterly * 4
print(yearly)