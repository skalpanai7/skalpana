num1,num2=map(int,raw_input().split())
x=num1*num2
for i in range(x):
	if x==i*i:
		print "yes"
		break
else:
	print "no"
