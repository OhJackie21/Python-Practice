year = 1994
month = 4
month_key_val = 0
year_str = int(str(year)[-2:])
year_end_mod = year % 100
print (year_str)
print (year_end_mod)

def find_day_of_week(year_end_mod):
    num1 = int(year_end_mod * .25)
    num2 = num1 + year_end_mod
    num3 = num2 + month + month_key_val
    num4 = num3 % 7

    print(num1)
    print(num2)
    print(num3)

find_day_of_week(year_end_mod)