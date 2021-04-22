print("Bru_Coffee Machine\n\nWhat you preffer to drink?")
a={1:"Coffee", 2:"Tea"}
print(a)
b=int(input("Choose 1 or 2: "))
if b==1 or 2 :
	print("You choosed",a[b],":")
c={1:"Large Cup- Rs.20", 2:"Medium Cup- Rs.15", 3:"Small Cup- Rs.10"}
print("May I know which size of Cup, do you want?")
print(c)
e=int(input("Choose 1, 2 or 3: "))
if b==1 or 2 or 3:
	print("You choosed",c[b],":")
d={1:"Single cup", 2:"Double cup", 3:"More"}
print(d)
print("How many cups, You want?")
f=int(input("Choose 1, 2 or 3: "))
if f==1 or f==2:
	print("You choosed",d[f],":")
elif f==3:
	n=int(input("How many?: "))
	print("You Entered: ",n)
if e==1:
	if f==1:
		g=int(input("Please insert your coin: "))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-20))
	elif f==2:
		g=int(input("please insert your coin:"))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-40))
	elif f==3:
		g=int(input("please insert your coin:"))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-n*20))
elif e==2:
	if f==1:
		g=int(input("please insert your coin: "))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-15))
	elif f==2:
		g=int(input("please insert your coin: "))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-30))
	elif f==3:
		g=int(input("please insert your coin: "))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-n*15))
elif e==3:
	if f==1:
		g=int(input("please insert your coin: "))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-10))
	elif f==2:
		g=int(input("please insert your coin: "))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-20))
	elif f==3:
		g=int(input("please insert your coin: "))
		print("Here is your bill: "+"/n",c[e])
		print("it's your change: " + str(g-n*10))