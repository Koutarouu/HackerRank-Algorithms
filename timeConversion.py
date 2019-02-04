"""def timeConversion(h,m,s,pe):
  horas=h
  minutos=m
  segundos=s
  periodo=pe
  periodo.upper()
  hora = "%d:%d:%d%s"%(horas,minutos,segundos,periodo.upper())
  if periodo=="PM":
    horas+=12
    hora="%d:%d:%d%s"%(horas,minutos,segundos,periodo)
  else:
    hora=hora
  return hora

print(timeConversion(12,22,11,"pm"))"""

def timeConversion(s):
  hours=s[0:2]
  minutes=s[3:5]
  seconds=s[6:8]
  time=s[8:10]
  if time.upper()=="PM" and hours=="12":
    hours=hours
  elif time.upper()=="PM":
    hours=str(int(hours)+12)
  elif time.upper()=="AM" and hours=="12":
    hours="00"
  return "%s:%s:%s"%(hours,minutes,seconds)


print(timeConversion("12:45:54PM"))