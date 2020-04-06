def QuickFindUF(n):
    id_list = []
    sizes = [1] * n
    for i in range(0,n):
        id_list.append(i)
    print("original list:\n",id_list)
    print("original size:\n",sizes)
    return(id_list, sizes)

def find(id_list,i):
    while i!=id_list[i]: i=id_list[i]
    #print(i)
    return(i)

def union(id_list,p,q):
    i = find(id_list,p);
    j = find(id_list,q);
    if (i == j): return
    if (sizes[i] < sizes[j]):
        print("before plus size:sizes[i]={}  , sizes[j]={}".format(sizes[i],sizes[j]))
        id_list[i] = j
        sizes[j] += sizes[i]
        print("After plus size:sizes[i]={}  , sizes[j]={}".format(sizes[i],sizes[j]))
    else: 
        print("before plus size:sizes[i]={}  , sizes[j]={}".format(sizes[i],sizes[j]))
        id_list[j] = i
        sizes[i] += sizes[j]
        print("After plus size:sizes[i]={}  , sizes[j]={}".format(sizes[i],sizes[j]))
    print("Union({},{}):  {}".format(p,q,id_list))
    print("Size({},{}):  {}".format(p,q,sizes))
    return(id_list)
def connected(id_list,p,q):
    a = root(id_list,p) == root(id_list,q)
    return print("Connect {},{}: {}".format(p,q,a))lst


(id_list, sizes) = QuickFindUF(10)
union(id_list,4,3)
union(id_list,3,8)
union(id_list,6,5)
union(id_list,9,4)
union(id_list,2,1)
union(id_list,5,0)
union(id_list,2,1)
union(id_list,7,2)
union(id_list,6,1)
union(id_list,7,3)