def timeInWords(h:int , m:int ) -> str:
	hours=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
	minutes=["o' clock","one minute","two minutes","three minutes","four minutes","five minutes", "six minutes","seven minutes","eight minutes","nine minutes","ten minutes","eleven minutes","twelve minutes","thirteen minutes","fourteen minutes","quarter","sixteen minutes","seventeen minutes","eighteen minutes", "nineteen minutes","twenty minutes","twenty one minutes","twenty two minutes","twenty three minutes","twenty four minutes","twenty five minutes","twenty six minutes", "twenty seven minutes", "twenty eight minutes", "twenty nine minutes", "half"]
	if m==0:
		TIW=hours[h]+" "+minutes[m]
	elif 1<=m<=30:
		TIW=minutes[m]+" past "+hours[h]
	else:
		TIW=minutes[60-m]+" to "+hours[h+1]
	return TIW

h=int(input())
m=int(input())
print(timeInWords(h,m))