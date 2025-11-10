import datetime
a = '14.02.2025'

date = datetime.datetime.strptime(a, '%d.%m.%Y').date()
format_date = datetime.datetime.strftime(date, '%d.%m.%Y')
print(type(date))
print(date)
print(date.weekday())
print('-----------------------------------------------')
print(type(format_date))
print(format_date)
print('-----------------------------------------------')
