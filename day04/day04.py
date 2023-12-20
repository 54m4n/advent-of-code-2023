import os
import math

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day04-cards-input.txt')

rows=f.readlines()

win=[]
own=[]

for i in range(len(rows)):
    tempwin=[]
    tempown=[]
    newrow=rows[i].replace('  ',' ').split(" ")
    if "" in newrow:
        newrow.remove("")
    
    for j in range(len(newrow)):
        if j<=11 and j>=2:
            tempwin.append(newrow[j])
        if j>=13:
            tempown.append(newrow[j].replace("\n",""))
    win.append(tempwin)
    own.append(tempown)


pwr=0
points=0

for i in range(len(win)):    
    for j in range(len(win[i])):
        if win[i][j] in own[i]:
            pwr=pwr+1
    print(i,pwr)
    if pwr==1:        
        points=points+1
        
    if pwr>=2:
        points=points+round(math.pow(2,pwr-1))
    pwr=0

print(points)

