import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}day03-engine-input.txt')
engine=f.readlines()
f.close()


def numcount(xcord,ycord):
    #left
    nume=""
    numz=[]
    i=0
    while engine[xcord][ycord-i].isdigit():
        nume=nume+(engine[xcord][ycord-i])
        i=i+1
    
    
    numz.append(nume[::-1])
    print(numz)
    return

def asterisk(xcord,ycord):
    print(engine[xcord][ycord])
    valid=False
    #left
    try:
        if engine[xcord][ycord-1].isdigit():
            numcount(xcord,ycord-1)
    except:
        NameError
    
    print(xcord,ycord,valid)
    return


for i in range(len(engine)-135):
    for j in range(len(engine[i])):
        if (engine[i][j])=="*":
            asterisk(i,j)