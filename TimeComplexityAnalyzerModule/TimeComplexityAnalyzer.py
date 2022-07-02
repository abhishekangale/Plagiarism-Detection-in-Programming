from tkinter import *
from tkinter import filedialog
import re
import os				#importing all the required library
root = Tk()
root.title('Time Complexity Analyzer!')
root.geometry('1920x1080')
root.configure(bg='white')		#creating the window of specified size and color

def resfun():			#reset function 
	pathlabel.config(text="Please click on the browse button to select a file")

	loopenclabel.config(text="Total loop count")

	fname.config(text="Name of the file")
	
	fext.config(text="Extension of the file")

	ftime.config(text="Time complexity in higher order")
	

def browsefunc():		#main module of the code
	try:
		absfile=""
		s4=os.pardir
		filename = filedialog.askopenfilename(initialdir=os.pardir,filetypes =(("C File", "*.c"),("All Files","*.*")),title = "Choose a file.")
		pathlabel.config(text="Full path = {}".format(filename))	
		absfile=os.path.basename(filename)
		extension = os.path.splitext(filename)[1]
		fname.config(text="File name = {}".format(absfile))
		fext.config(text="File Extension = {}".format(extension))		#getting filenamem extension and displaying
		
		s=""
		k=""
		l=""
		count=0
		
		file = open(filename,'r')
		for line in file.readlines():
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
		loopenclabel.config(text="total number of loop encountered = {}".format(count1))	#for displaying total count of loop
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
		print(temp2)
		ftime.config(text="Higher order time complexity is = {}".format(temp2))	#displaying result
		#print(temp2)
		
		if(extension == '.java' or extension == '.py' or extension == '.pdf'):				#if irrelevant extension is selected
			pathlabel.config(text=" file format not supported")
			loopenclabel.config(text="Nothing to show")
			fname.config(text="File name = {}".format(absfile))
			fext.config(text="File Extension = {}".format(extension))
			ftime.config(text="Unsupported file")
	except:															#if no file is selected
		pathlabel.config(text="No file chosen Please select a file")
		loopenclabel.config(text="Nothing to show")
		fname.config(text="Nothing selected")
		ftime.config(text="Nothing to display")
		fext.config(text="Nothing selected")
	
		
		#print("no file chosen")

titlelabel = Label(root,text="Time Complexity Analyzer Module",fg='gray3' ,bg='palegreen',font=('Arial', 12, 'bold', 'italic'))
titlelabel.pack()
titlelabel.place(x=16,y=20)

pathlabel = Label(root,height=2,width=50,fg='gray3' ,bg='azure',font=('Arial', 9, 'bold'),text="Please click on the browse button to select a file")
pathlabel.pack()
pathlabel.place(x=16,y=60)
    
browsebutton = Button(root, text="Browse", width='7',command=browsefunc,fg='gray3' ,bg='azure',font=('Arial', 12, 'bold'))
browsebutton.pack()
browsebutton.place(x=390,y=60)

reset = Button(root, text="Reset", command=resfun,fg='gray3' ,bg='azure',font=('Arial', 12, 'bold'))
reset.pack()
reset.place(x=16,y=120)

quitw = Button(root, text="quit", width='7',command=quit,fg='gray3' ,bg='azure',font=('Arial', 12, 'bold'))
quitw.pack()
quitw.place(x=390,y=120)


loopenclabel = Label(root,height=2,width=30,fg='gray3' ,bg='azure',font=('Arial', 10, 'bold', 'italic'),text="Total loop count")
loopenclabel.pack()
loopenclabel.place(x=120,y=120)


fname = Label(root,height=3,width=20,fg='gray3' ,bg='azure',font=('Arial', 10, 'bold', 'italic'),text="Name of the file")
fname.pack()
fname.place(x=16,y=180)

fext = Label(root,height=1,width=20,fg='gray3' ,bg='azure',font=('Arial', 10, 'bold', 'italic'),text="Extension of the file")
fext.pack()
fext.place(x=16,y=240)

ftime = Label(root,height=6,width=38,fg='gray3' ,bg='azure',font=('Arial', 8, 'bold', 'italic'),text="Time complexity in higher order")
ftime.pack()
ftime.place(x=198,y=180)

mainloop()




