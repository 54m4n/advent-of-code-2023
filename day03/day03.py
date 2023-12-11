import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day03-engine-input.txt','r',buffering=100000)
lines = f.readlines()
engine=[]

for lines in lines:
    engine.append(lines.strip())

actnum=""

for i in range(len(engine[0])):   
    if engine[0][i].isdigit():
        j=i
        while engine[0][j].isdigit():
            actnum=actnum+(engine[0][j])
            j=j+1
        print(actnum)
        actnum=""
    
    
    


