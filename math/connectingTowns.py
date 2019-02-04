for _ in range(int(input())):
	_,towns,mul=input(),map(int,input().split()),1
	for i in towns: mul*=i #%1234567
	print(mul%1234567)


#from functools import reduce
	#print(reduce(lambda x,y: (x*y)%1234567 , towns))