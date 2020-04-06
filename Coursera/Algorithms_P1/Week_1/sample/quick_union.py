def QuickFindUF(n):
    id_list = []
    for i in range(0,n):
        id_list.append(i)
    print("original list:\n",id_list)
    return(id_list)

def root(id_list,i):
    while i!=id_list[i]: i=id_list[i]
    #print(i)
    return(i)

def union(id_list,p,q):
    i = root(id_list,p);
    j = root(id_list,q);
    id_list[i] = j
    print("Union({},{}):  {}".format(p,q,id_list))
    return(id_list)
def connected(id_list,p,q):
    a = root(id_list,p) == root(id_list,q)
    return print("Connect {},{}: {}".format(p,q,a))

if __name__ == '__main__':
	id_list = QuickFindUF(10)
	#id_list = [0,1,9,4,9,6,6,7,8,9]
	union(id_list,4,3)
	union(id_list,3,8)
	union(id_list,6,5)
	union(id_list,9,4)
	union(id_list,2,1)
	connected(id_list,8,9)
	connected(id_list,5,4)
	union(id_list,5,0)
	union(id_list,7,2)
	union(id_list,6,1)
	union(id_list,7,3)