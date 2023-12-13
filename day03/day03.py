import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day03-engine-input.txt','r',buffering=100000)
lines = f.readlines()
engine=[]

for lines in lines:
    engine.append(lines.strip())
f.close()

def numcheck(ycord,xcord,num):
    xcord=xcord-len(num)
    #print(ycord,xcord,num)

    checklist=[]

    #left
    try:
        checklist.append(engine[ycord][xcord-1])
    except:
        NameError
    #right
    try:
        checklist.append(engine[ycord][xcord+len(num)])
    except:
        NameError        
    
    #toprow
    for i in range(len(num)+2):
        if ycord-1>=0:            
            try:
                checklist.append(engine[ycord-1][xcord-1+i])
            except:
                NameError   
      
    #bottomrow
    for i in range(len(num)+2):
        if ycord+1<=139:
            try:
                checklist.append(engine[ycord+1][xcord-1+i])
            except:
                NameError
                
    valid=False
    for i in range(len(checklist)):
        if not checklist[i].isdigit() and checklist[i]!=".":
            #print(num,checklist[i])
            valid=True
    #print(num,checklist,valid)
    return valid


actnum=""
sumnum=0
i=0
j=0


for ycord in range(len(engine)):
    while j<(len(engine[ycord])):        
        if engine[ycord][j].isdigit():
            xcord=j
            while xcord<=139 and engine[ycord][xcord].isdigit():                
                actnum=actnum+(engine[ycord][xcord])
                xcord=xcord+1
                j=j+len(actnum)-1
                
            if (numcheck(ycord,xcord,actnum))==True:
                sumnum=sumnum+int(actnum)
            
            actnum=""
        j=j+1
    j=0

            
        
print(sumnum)