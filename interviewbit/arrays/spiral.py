original_array = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9, 10, 11, 12 ],
    [ 13, 14, 15, 16 ],
]

print("original_array= \n",original_array)
top = 0
bt = len(original_array)-1
left = 0
right = len(original_array[0])-1
di = 0
new_list = []
while top<= bt and left <= right:
    if di==0:
        for i in range(left, right+1):
            new_list.append(original_array[top][i])
            print("append left - right :",original_array[top][i])
        top+=1
    elif di==1:
        for i in range(top, bt+1):
            new_list.append(original_array[i][right])
            print("append top - bt:",original_array[i][right])
        right -=1
    elif di==2:
        for i in range(right, left-1, -1):
            new_list.append(original_array[bt][i])
            print("append right - left:",original_array[bt][i])
        bt -=1
    elif di==3:
        for i in range(bt, top-1,-1):
            new_list.append(original_array[i][right])
            print("append bt - top:",original_array[i][left])
        left +=1
    di = (di + 1) % 4
        
print("Spiral new list = ",new_list)