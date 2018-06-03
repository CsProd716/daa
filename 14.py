completed=[]
n=input("Enter the number of place you want to visit: ")
ary=[[0 for rows in range(n)] for col in range(n)]
cost=0
def takeInput():   
    for i in range (n):
        for j in range (n):
            if (i!=j):
                ary[i][j]=input("Enter cost for %d to %d"%(i,j))
            else:
                ary[i][i]=0
        completed.append(0)
    print("\n\nAdjacency matrix is:")
    for i in range (n):
        print("\n")
        for j in range(n):
            print(ary[i][j],"\t",)
def the_min(c):
    nc=999
    mi=99999
    kmin=0
    global cost
    for i in range (n):
        if((ary[c][i]!=0) and (completed[i]==0)):
            if((ary[c][i]+ary[i][c]) < mi):
                mi=ary[i][0]+ary[c][i]
                kmin=ary[c][i]
                nc=i
    if(mi!=99999):
        cost=cost+kmin
    return nc
def lowest(city):
    global cost
    completed[city]=1
    print ("%d--->"%(city+1),)
    ncity=the_min(city)
    if(ncity==999):
        ncity=0
        print(ncity+1)
        cost+=ary[city][ncity]
        return #remove if error
    lowest(ncity)
def result_tsp():
    takeInput()
    print("\n\nThe Path is:\n")
    lowest(0)
    print("\n\nMinimum cost is ",cost)
result_tsp()
