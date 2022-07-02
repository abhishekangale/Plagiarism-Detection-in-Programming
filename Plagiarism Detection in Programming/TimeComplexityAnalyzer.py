import re
import os				#importing all the required library

def browsefunc(file):		#main module of the code
	file.splitlines()
	s = ""
	for line in file:
		if re.search('\s*for\s*\((.*)\)(.*)',line):
			s=s+line
		if re.search('\s*while\s*\((.*)\)(.*)',line):
			s=s+line
		if re.search('^\s*\{',line):
			s=s+line
		if re.search('\}',line):
			s=s+line											#performing pattern match and storing is string s
	#print(s)


	k=s.split('\n')												#splitting string with line by line
	count1=0
	for line1 in range(len(k)):
		if re.search('\s*for\s*\((.*)\)(.*)',k[line1]):
			#print(k[line1])
			count1=count1+1
		if re.search('\s*while\s*\((.*)\)(.*)',k[line1]):
			#print(k[line1])
			count1=count1+1
	# loopenclabel.config(text="total number of loop encountered = {}".format(count1))	#for displaying total count of loop
	#print(count1)
	
	
	a=1
	temp1=""
	temp2=""
	count=0
	operator = ['+', '-', '*', '/']
	list1 = []
	for text in range(len(k)):
		temp=k[text]
		for subtext in range(0,len(temp)):
			if(k[text][subtext] == '{'):
				count=1
			if(k[text][subtext] == '}'):
				count=0
			# print(count)
			if(count!=0):
				# print(k[text])
				if(k[text][subtext]=='<' or k[text][subtext]=='>'):
					temp1=temp1+k[text][subtext+a]
					while(temp1 == ' ' or temp1 == '='):
						a=a+1
						temp1=k[text][subtext+a]
						if(temp1 != ' ' and temp1 != '='):
							break
					# print("here")
					var = subtext
					while(k[text][var] != ';'):
						var = var + 1
					while(k[text][var] not in operator):
						var = var + 1
					# print(k)
					init = 0
					while(k[text][init] != '=' and init < len(temp)):
						init = init + 1
					
					# print(k[text][init])
					init = init + 1
					rev = ''
					while(k[text][init] != ';'):
						if k[text][init] != ' ':
							rev = rev + (k[text][init])
						init = init + 1

					# print(k[text])
					# temp1 = temp1[:-1]
					if k[text][var] == '+' or k[text][var] == '-':
						if k[text][var] == '+':
							list1.append(k[text][subtext + a])
						else :
							list1.append(rev)
					else :
						xd = "log("
						if k[text][var] == '*':
							xd = xd + k[text][subtext + a]
						else :
							xd = xd + rev
						xd = xd + ')'
						list1.append(xd)
					# print(rev)
																	#calculating and manipulating the time complexity
							
	# list1=list(temp1)			#storing the result in list
	# print(list1)

	for i in range(len(list1)-1):
		if(list1[i] == '='):
			del(list1[i])		#correcting irrelevant complexity
		
			
	list1=list('*'.join(list1))		
	temp2=''.join(list1)		#converting list to string
	return temp2
