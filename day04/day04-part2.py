import os
import math

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day04-cards-input.txt')

rows=f.readlines()
f.close()

win=[]
own=[]

for i in range(len(rows)):
    tempwin=[]
    tempown=[]
    newrow=rows[i].replace('  ',' ').split(" ")
    if "" in newrow:
        newrow.remove("")
    
    for j in range(len(newrow)):
        if j<=6 and j>=2:
        #if j<=1 and j>=2:
            tempwin.append(newrow[j])
        if j>=8:
        #if j>=13:
            tempown.append(newrow[j].replace("\n",""))
    win.append(tempwin)
    own.append(tempown)    

print(win)
print()
print(own)

cardnums=[]
wincardnums=[]
matches=0

for i in range(len(win)):
    for j in range(len(win[i])):    
        if win[i][j] in own[i]:
            matches=matches+1
    cardnums.append(matches)
    matches=0

print(cardnums)

