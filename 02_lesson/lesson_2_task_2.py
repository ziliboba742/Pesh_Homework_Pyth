def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


y = int(input("Введите год: "))
result = is_year_leap(y)
print(f"год {y}: {result}")
