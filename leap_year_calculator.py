#Simple
# year = int(input("choose year"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")
#---------------------------------------------------------------
# year = int(input("choose year: "))

# def leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#              if year % 400 == 0:
#                   return True
#              else:
#                   return False
#         else:
#             return True
#     else:
#          return False
    
# if leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

  

#-------------------------------------------------------------------------
def is_leap(year):
  """checks if a year is a leap year"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(year1, month1):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    day= ""
    if is_leap(year1):
        month_days[1]= 29
    day = month_days[int(month1-1)]
    return day
  

year = int(input("enter a year: ")) # Enter a year
month = int(input("enter a month: ")) # Enter a month
days = days_in_month(year, month)
print(days)

