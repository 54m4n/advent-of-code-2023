import os
import re

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day02-bag-input.txt','r')

rows=f.readlines()
srows=[]

for i in range(len(rows)):
    srows.append(re.split(': |; ',rows[i].replace("red","r").replace("blue","b").replace("green","g").replace(", ",",").replace("\n","")))

#print(srows[0])

valid=True
indexossz=0
summaxok=0
for i in range(len(srows)):
    print(f'#### {i+1} ####')
    aktlist=[]
    for j in range(1,len(srows[i])):
        aktlist.append(re.split(' |,',srows[i][j]))

    r=0
    g=0
    b=0
    maxr=0
    maxg=0
    maxb=0
    rvalid=True
    gvalid=True
    bvalid=True
    for k in range(len(aktlist)):
        print(aktlist[k])
        if "r" in aktlist[k]:
            r=r+int(aktlist[k][aktlist[k].index("r")-1])
            if r>=maxr:
                maxr=r
            if r>12:
                rvalid=False
            r=0
        if "g" in aktlist[k]:
            g=g+int(aktlist[k][aktlist[k].index("g")-1])
            if g>=maxg:
                maxg=g
            if g>13:
                gvalid=False
            g=0
        if "b" in aktlist[k]:
            b=b+int(aktlist[k][aktlist[k].index("b")-1])
            if b>=maxb:
                maxb=b
            if b>14:
                bvalid=False
            b=0
            
            
    summaxok=summaxok+(maxr*maxg*maxb)    
    
    if (rvalid==True) and (gvalid==True) and (bvalid==True):
        indexossz=indexossz+(i+1)
    
    print(f'maxok: {maxr} {maxg} {maxb} -> {maxr*maxg*maxb} -> {summaxok}')
    print("#########")
    #bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes
    print()
    

print(indexossz)
print(summaxok)