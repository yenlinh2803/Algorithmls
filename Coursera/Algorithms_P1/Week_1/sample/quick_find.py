def QuickFindUF(n):
    id_list = []
    for i in range(0,n):
        id_list.append(i)
    return(id_list)

def connected(id_list,p,q):
    return id_list[p] == id[q]


def union(id_list,p,q):
    pid = id_list[p];
    qid = id_list[q];
    for i in range(0,len(id)):
        if (id_list[i] == pid): id_list[i] = qid
    print(id_list)
    return(id_list)

def main():
    id_list = QuickFindUF(5)
    print(id_list)
    id_list = union(id_list, 0,1) #Create connection between 0 and 1
    id_list = union(id_list, 2,3) #Create connection between 2 and 3
    id_list = union(id_list, 3,4) #Create connection between 3 and 4
    print(connected(id_list,0,1)) #Check connection between 0 and 1
    print(connected(id_list, 1,2)) 


if __name__ == '__main__':
         #mongodb_to_bigquery()
    main()

