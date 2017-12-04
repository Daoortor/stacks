program=[]         
custom = [][]
for i in range(65536):

	custom[i-1]=0

def prints(a,b):
	if b="$":

		print(a)

	if b="#":
		print(custom[a])
def setstack(int(a),b,c):

	if c="%":

		custom[a]=b

	elif c="#":

		custom[a]=custom[b]

	elif c="input":
		custom[a]=input()
def let(int(left),typeright,int(right),oper="+",arg=0,typearg):

	if typearg="%":	
		if typeright="#":
    			if oper="+":

				custom[int(left)]=custom[int(right)]+arg

			if oper="-":

				custom[int(left)]=custom[int(right)]-arg
        
        	if oper="*":

				custom[int(left)]=custom[int(right)]*arg

			if oper="/":

				custom[int(left)]=custom[int(right)]/arg

			if oper="mod":

				custom[int(left)]=custom[int(right)]%arg

			if oper="/int":
            
				custom[int(left)]=custom[int(right)]//arg
        
			if oper="^":
            
				custom[int(left)]=custom[int(right)]**arg
        
			if oper="!^":
            
				custom[int(left)]=custom[int(right)]**(1/arg)
    
		if typeright="%":
        
			if oper="+":
            
				custom[int(left)]=int(right)+arg
        
			if oper="-":
            
				custom[int(left)]=int(right)-arg        
        
			if oper="*":
            
				custom[int(left)]=int(right)*arg
        
			if oper="/":
            
				custom[int(left)]=int(right)/arg
        
			if oper="mod":
            
				custom[int(left)]=int(right)%arg
        
			if oper="/int":
            
				custom[int(left)]=int(right)//arg
        
			if oper="^":
            
				custom[int(left)]=int(right)**arg
        
			if oper="!^":
            
				custom[int(left)]=int(right)**(1/arg)
    
		if typeright="$":
        
			if oper="+":
            
				custom[int(left)]=right+arg
        
			if oper="-":
            
				custom[int(left)]=right-arg        
        
			if oper="*":
            
				custom[int(left)]=right*arg
        
			if oper="/":
            
				custom[int(left)]=right/arg
        
			if oper="mod":
            
				custom[int(left)]=right%arg
        
			if oper="/int":
            
				custom[int(left)]=right//arg
        
			if oper="^":
            
				custom[int(left)]=right**arg
        
			if oper="!^":
            
				custom[int(left)]=right**(1/arg)
		if typeright="input":
			if oper="+":
            
				custom[int(left)]=right+input
()        
			if oper="-":
            
				custom[int(left)]=right-input()      
        
			if oper="*":
                                   
				custom[int(left)]=right*input()      
			if oper="/":
            
				custom[int(left)]=right/input()       
			if oper="mod":
            
				custom[int(left)]=right%input()
        
			if oper="/int":
            
				custom[int(left)]=right//input()        
			if oper="^":
            
				custom[int(left)]=right**input
        
			if oper="!^":
            
				custom[int(left)]=right**(1/input())
	if typearg="#":	
		if typeright="#":
    			if oper="+":

				custom[int(left)]=custom[int(right)]+custom[arg]

			if oper="-":

				custom[int(left)]=custom[int(right)]-custom[arg]
        
        	if oper="*":

				custom[int(left)]=custom[int(right)]*custom[arg
]
			if oper="/":

				custom[int(left)]=custom[int(right)]/custom[arg
]
			if oper="mod":

				custom[int(left)]=custom[int(right)]%custom[arg]

			if oper="/int":
            
				custom[int(left)]=custom[int(right)]//custom[arg
]        
			if oper="^":
            
				custom[int(left)]=custom[int(right)]**custom[arg]
        
			if oper="!^":
            
				custom[int(left)]=custom[int(right)]**(1/custom[arg])
    
		if typeright="%":
        
			if oper="+":
            
				custom[int(left)]=int(right)+custom[arg
]       
			if oper="-":
            
				custom[int(left)]=int(right)-custom[arg]        
        
			if oper="*":
            
				custom[int(left)]=int(right)*custom[arg]
        
			if oper="/":
            
				custom[int(left)]=int(right)/custom[arg
]        
			if oper="mod":
            
				custom[int(left)]=int(right)%custom[arg]
        
			if oper="/int":
            
				custom[int(left)]=int(right)//custom[arg]
        
			if oper="^":
            
				custom[int(left)]=int(right)**custom[arg]
        
			if oper="!^":
            
				custom[int(left)]=int(right)**(1/custom[arg])
    
		if typeright="$":
        
			if oper="+":
            
				custom[int(left)]=right+custom[arg
]        
			if oper="-":
            
				custom[int(left)]=right-custom[arg]        
        
			if oper="*":
            
				custom[int(left)]=right*custom[arg
]        
			if oper="/":
            
				custom[int(left)]=right/custom[arg
]       
			if oper="mod":
            
				custom[int(left)]=right%custom[arg
]        
			if oper="/int":
            
				custom[int(left)]=right//custom[arg
]        
			if oper="^":
            
				custom[int(left)]=right**custom[arg]
        
			if oper="!^":
            
				custom[int(left)]=right**(1/cusyom[arg])
		if typeright="input":
			if oper="+":
            
				custom[int(left)]=right+custom[input
()]        
			if oper="-":
            
				custom[int(left)]=right-custom[input()]      
        
			if oper="*":
                                   
				custom[int(left)]=right*custom[input()]      
			if oper="/":
            
				custom[int(left)]=right/custom[input()]       
			if oper="mod":
            
				custom[int(left)]=right%custom[input()]
        
			if oper="/int":
            
				custom[int(left)]=right//custom[input()]        
			if oper="^":
            
				custom[int(left)]=right**custom[input()]
        
			if oper="!^":
            
				custom[int(left)]=right**(1/custom[input()])
def command:
	for i in range(0,999999)
		program.append(input().split)
		if program[i][1]="run":
			goto 1
	1
	for i in range(0,999999):
		if program[i][1]="prints":
			prints(program[i][2],program[i][3])
		elif program[i][1]="setstack":
			setstack(program[i][2],program[i][3],program[i][4]
		elif program[i][1]="let":
			let(program[i][2],program[i][3],program[i][4],program[i][5],program[i][6])
		elif program[i][1]="end":
			goto 2
	2
open("stacksdata.txt","a")
stacksdata.txt.write(txt(program[][]))
stacksdata.txt.write(txt(custom[][]))
