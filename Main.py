First_Number = 10
Second_Number = 100
Is_It_Prime = True
Prime_Numbers = []
for i in range (First_Number,Second_Number):
	Is_It_Prime = True
	for j in range (2,i):
		if (i%j==0):
			Is_It_Prime = False
			break
		Is_It_Prime = True
	if (Is_It_Prime):
		Prime_Numbers.append (i)

print (Prime_Numbers)
