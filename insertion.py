my_list=[3,6,2,5,8,1,4,7]
print("unsorted list" , my_list)
temp = None 

for item in range(1,len(my_list)) :
    temp = my_list[item]
    j=item - 1
    while j >=0 and my_list[j] >temp :
        my_list[j+1] = my_list[j]
        j -= 1
    my_list[j+1] = temp

print("unsorted list" , my_list)