import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day03-engine-input.txt')
engine=f.readlines()
f.close()


def numcount(sor,oszlop):    
    numz=[]
    nume=""
    sum=0
    #top
    if (engine[sor-1][oszlop].isdigit()):
        #left
        i=0
        nume=""
        while engine[sor-1][oszlop-i].isdigit():
            nume=(engine[sor-1][oszlop-i])+nume
            i=i+1
        #right
        i=1        
        while engine[sor-1][oszlop+i].isdigit():
            nume=nume+(engine[sor-1][oszlop+i])
            i=i+1
    if nume!="":
        numz.append(nume)    
    nume=""
    
    #top-rest
    if not (engine[sor-1][oszlop].isdigit()):
        #left
        i=1
        nume=""
        while engine[sor-1][oszlop-i].isdigit():
            nume=(engine[sor-1][oszlop-i])+nume
            i=i+1
        if nume!="":
            numz.append(nume)    
        nume=""        
        #right
        i=1
        while engine[sor-1][oszlop+i].isdigit():
            nume=nume+(engine[sor-1][oszlop+i])
            i=i+1
    if nume!="":
        numz.append(nume)    
    nume=""
    
    #bottom
    if (engine[sor+1][oszlop].isdigit()):
        #left
        i=0
        nume=""
        while engine[sor+1][oszlop-i].isdigit():
            nume=(engine[sor+1][oszlop-i])+nume
            i=i+1
        #right
        i=1        
        while engine[sor+1][oszlop+i].isdigit():
            nume=nume+(engine[sor+1][oszlop+i])
            i=i+1
    if nume!="":
        numz.append(nume)    
    nume=""
    
    #bottom-rest
    if not (engine[sor+1][oszlop].isdigit()):
        #left
        i=1
        nume=""
        while engine[sor+1][oszlop-i].isdigit():
            nume=(engine[sor+1][oszlop-i])+nume
            i=i+1            
        if nume!="":
            numz.append(nume)    
        nume=""
        #right
        i=1
        while engine[sor+1][oszlop+i].isdigit():
            
            nume=nume+(engine[sor+1][oszlop+i])
            i=i+1
    if nume!="":
        numz.append(nume)    
    nume=""
    #left
    i=1
    while engine[sor][oszlop-i].isdigit():
        nume=engine[sor][oszlop-i]+nume
        i=i+1
    if nume!="":
        numz.append(nume)    
    nume=""

    #right
    i=1
    while engine[sor][oszlop+i].isdigit():
        nume=nume+engine[sor][oszlop+i]
        i=i+1
    if nume!="":
        numz.append(nume)    
    nume=""
        
        
        
        
    
    
    if len(numz)==2:
        sum=int(numz[0])*int(numz[1])
        print(numz[0],numz[1],sum)
    return sum





ossz=0
for sor in range(len(engine)):
    for oszlop in range(len(engine[sor])):
        if (engine[sor][oszlop])=="*":
            ossz=ossz+numcount(sor,oszlop)
            print(ossz)
print(ossz)