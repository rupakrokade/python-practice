import sys

def draw(l):
	print "\n----- ----- -----"
	for k in range(3):
		for i in range(3):
			if k==0:
				i=i
			elif k==1:
				i=i+3
			elif k==2:
				i=i+6
			#print " --- ",
			print("| %s |")% l[i],
		print "\n----- ----- -----"

def check3(val):
		if ((val[1]-val[0])+val[1]==val[2]) and ((val[2]-val[1]==1) or (val[2]-val[1]==4) or (val[2]-val[1]==3)):
			return True	


def check4(vec):
	match=0
	dat1=[vec[0],vec[1],vec[2]]
	dat2=[vec[1],vec[2],vec[3]]
	dat3=[vec[0],vec[2],vec[3]]
	dat4=[vec[0],vec[1],vec[3]]

	for i in [dat1,dat2,dat3,dat4]:
		if check3(i)==True:
			match = 1

	if match ==1:
		return True
	else:
		return False

def check5(vec):
	match=0

	dat1=[vec[0],vec[1],vec[2]]
	dat2=[vec[1],vec[2],vec[3]]
	dat3=[vec[2],vec[3],vec[4]]
	dat4=[vec[0],vec[2],vec[3]]
	dat5=[vec[0],vec[3],vec[2]]
	dat6=[vec[0],vec[1],vec[3]]
	dat7=[vec[0],vec[2],vec[4]]
	dat8=[vec[1],vec[2],vec[4]]
	dat9=[vec[1],vec[3],vec[4]]

	return True

		for j in [dat1,dat2,dat3,dat4,dat5,dat6,dat7,dat8,dat9]:
			print j
			if check3(j)==True:
				match = 1

		if match == 1:
			return True
		else:
			return False



def player(l,mark):
	out=[]

	for i in range(len(l)):
		if l[i]==mark:
			out.append(i+1)
	return out


def winner(mark,vec):
	vec=player(vec,mark)
	#print vec

	if len(vec)<3:
		return False
	elif len(vec)==3:
		if check3(vec)==True:
			return True
	elif len(vec)==4:
		if check4(vec)==True:
			return True
	elif len(vec)==5:
		if check5(vec)==True:
			return True



def start(l):
	stack=[]
	for i in range(9):
		if i%2!=0:
			while True:
				data=raw_input("Player 2's turn to choose a position to put O: ")
				try:
					data=int(data)
				except:
					print "Please put a valid number between 1 to 9"
					continue
				else:
					if (data>0) & (data<10):
						if stack.count(data)==0:
							stack.append(data)
							l[data-1]='O'
							if winner('O',l)==True:
								draw(l)
								sys.exit("Player 2 with 'O'  wins the Game !!!")
							break
						else:
							print "You cannot overwrite a previous move"
							continue
					else:
						print "Please enter a number between 1 to 9"
		else:
			while True:
				data=raw_input("Player 1's turn to choose a position to put X: ")
				try:
					data=int(data)
				except:
					print "Please put a valid number between 1 to 9"
				else:
					if (data>0) & (data<10):
						if stack.count(data)==0:
							stack.append(data)
							l[data-1]='X'
							print winner('X',l)
							if winner('X',l)==True:
								draw(l)
								sys.exit("Player 1 with 'X' wins the Game !!!")
							break
						else:
							print "You cannot overwrite a previous move"
							continue
					else:
						print "Please enter a number between 1 to 9"		
		draw(l)
		print l

l=range(1,10)
#l[3]='X'
#l[4]='X'
#l[5]='X'
draw(l)
start(l)
