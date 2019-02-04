def solve(year):
  day=0
  month="09"
  #if year%1800 or year == 1700 or year == 1900 or year == 1700:
  if year==1918:
    day=26
  elif year==1800 or year == 1700 or year == 1900:
    day=12
  elif year%100==0 and year%400==0: 
    day=12
  elif year%4==0 and year%100!=0:
    day=12
  else:
    day=13

  return "%d.%s.%d"%(day,month,year)


print(solve(2016))
print(solve(1918))

print(solve(1800))

print(solve(2100))