import datetime

def get_day_of_week(day, month, year):
  day_of_week = datetime.date(year, month, day).strftime('%A')
  return day_of_week

amount = 0

for i in range(1901, 2000):
  for j in range(1, 13):
    if get_day_of_week(1, j, i) == 'Monday':
      print(f"Year: {i}, Month: {j}")
      amount += 1

print("Amount of Mondays: ", amount)