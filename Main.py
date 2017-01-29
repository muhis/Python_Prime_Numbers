def primes(first_number, second_number,method):
	if(method == 1):
		Prime_Numbers = []
		for i in range (first_number,second_number):
			is_it_prime = True
			for j in range (2,i):
				if (i%j==0):
					is_it_prime = False
					break
				is_it_prime = True
			if (is_it_prime):
				Prime_Numbers.append (i)
		return Prime_Numbers
	else:
		notprime = [j for i in range(first_number,8) for j in range(i*2,second_number,i)]
		prime = [i for i in range(first_number,second_number) if i not in notprime]
		return(prime)
print(primes(2,100,2))
