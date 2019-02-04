def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0 and year%100==0:
      leap=True
    elif year%100==0:
      leap=False
    elif year%4==0:
      leap=True
    else:
      leap=False
    return leap

print(is_leap(1800))
print(is_leap(1990))
print(is_leap(2400))
print(is_leap(2500))