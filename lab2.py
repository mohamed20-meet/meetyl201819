#a = [1,2,3,4,5,6]

#def value():
	#newlist= [a[0],a[-1]]
	#return newlist


###for newlist in value():
	#if value > 5 :
		#print value
'''
a=[1,2,3,4,5,89,9,8]
def lessthan5():
	for number in a:
		if number < 5:
			print number

lessthan5()
'''
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
s=[]
def addlist ():
	for  number in a:
		if number in b :
			if number in s:
				pass
			else:
			    s.append(number)
	print s

addlist()


	
