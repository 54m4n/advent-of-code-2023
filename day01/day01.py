import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day01-puzzle-input.txt','r')
lines=f.readlines()
f.close()
ossz=0
firstint=0
secondint=0
finalint=0

for i in range(len(lines)):
    szo=lines[i].strip()
    print(szo)
    for j in range(len(szo)):
        if szo[j].isdigit():            
            firstint=szo[j]
            szo=szo[j+1:len(szo):1]
            break
    for k in range(len(szo)):
        if szo[k].isdigit():            
            secondint=szo[k]
    finalint=int(f'{firstint}{secondint}')
    ossz=ossz+finalint
    print(finalint)
    firstint=""
    secondint=""
    
print(ossz)
        
