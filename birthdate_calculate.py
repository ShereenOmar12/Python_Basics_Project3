from datetime import date
import datetime
today=datetime.date.today()
birh_day=datetime.date(1996,4,13)
x = today -  birh_day
days=x.days
print(f'days left to birthday is {days} days')
