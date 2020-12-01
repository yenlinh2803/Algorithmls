array_1 = [31,29,27,28,19,17,15]

def insertion_sort(array_1):
    for i in range(1,len(array_1)):
        current_number = array_1[i]
        j = i-1
        while j>=0 and current_number < array_1[j]:
            print("origin array",array_1)
            print("i: {} & j: {}".format(i,j))
            print("current_number: {} & array_1[{}]: {}".format(current_number,j,array_1[j]))
            array_1[j+1]= array_1[j]
            j -=1
            print("Change j: ",j)
            print("array: ",array_1)
            print("-"*30)
        print("array_1[{}] = {}".format(j+1,array_1[j+1]))
        array_1[j+1] = current_number
    print("Finish array_1:",array_1)
    return array_1

array_new = insertion_sort(array_1)

# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n)
# Average Time Complexity [Big-theta]: O(n2)