def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return("Leap year.")
      else:
        return("Not leap year.")
    else:
      return("Leap year.")
  else:
    return("Not leap year.")

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  leap=is_leap(year)
  month_to_find=month-1
  if leap=="Leap year." and month_to_find==1:
    return f'in year {year} febrery has 29 daye'
  else:
    days=month_days[month_to_find]

    return f'year {year} has {days}  in {month} month'



year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
