import calendar

days_list = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
month, day, year = map(int, input().split())
day_of_week = calendar.weekday(year, month, day)
print(days_list[day_of_week])